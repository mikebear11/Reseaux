#!/usr/bin/env python3
"""
hookscore.py - score the first line of a Reel on the five things strong hooks
have in common, and rank a batch of them against each other.

What this is:  five local heuristics, computed on your machine from the text
alone. They measure properties that hooks which hold attention tend to share -
a length you can say in under three seconds, a concrete marker, something at stake,
the payload at the front rather than the back, and a viewer to aim it at.

What this is NOT:  a view predictor. It was tested against 74 real short-form
hooks, transcribed from the first three seconds of the top eight and bottom
eight performers on five channels. Separating a real hook from a deliberately
bad one it does well: AUC 0.83, and 9 of 10 written-to-be-bad hooks scored
below the real median. Separating a good creator's hits from that same
creator's misses it barely does at all: AUC 0.56, where 0.50 is a coin flip.

So use it for what it measured well. It catches greetings, preambles, hooks
with nothing concrete in them and hooks that take five seconds to say. It will
not tell you which of two decent hooks will travel, and nothing that reads text
can, because that is decided by your face, your edit, your audio and who
Instagram shows it to. Trust the retention graph over this script.

Each check returns 0 to 100. Higher is better.

Usage
  python3 hookscore.py hooks.txt              # one hook per line, ranked
  python3 hookscore.py --hook "I lost $18,000 on one missing contract."
  pbpaste | python3 hookscore.py -
  python3 hookscore.py hooks.txt --json
  python3 hookscore.py --hook "On a raté 3 brassins avant la bonne." --lang fr

French: --lang auto (the default) picks French or English per hook. The French
word lists below are an editorial transposition of the English ones. The
thresholds (5 to 12 words, ~165 wpm) are the author's English calibration and
have not been re-measured on French hooks.
"""

import argparse
import json
import re
import statistics
import sys

WORD_RE = re.compile(r"[\w$%€'’-]+")
NUMBER_RE = re.compile(
    r"[$€]\s?\d[\d,]*(?:\.\d+)?"                     # money, whole
    r"|\b\d[\d,]*(?:\.\d+)?\s?"                      # a figure, with or
    r"(?:%|€|k\b|x\b|hrs?\b|hours?\b|mins?\b|minutes?\b"  # without a unit
    r"|days?\b|weeks?\b|months?\b|years?\b"
    r"|h\b|heures?\b|jours?\b|semaines?\b|mois\b|ans?\b|années?\b"
    r"|litres?\b|l\b|hl\b|°)?",
    re.IGNORECASE)
PROPER_RE = re.compile(r"(?<!^)\b[A-ZÀ-ÖØ-Þ][a-zà-öø-ÿ]{2,}\b")
ELISION_RE = re.compile(r"^(?:[cdjlmnst]|qu)['’]", re.IGNORECASE)
HASHTAG_RE = re.compile(r"(?:^|\s)#\w+")
EMOJI_RE = re.compile(r"[\U0001F300-\U0001FAFF☀-➿]")

# Spoken hooks say their numbers out loud. "Zero dollars" and "twenty grand"
# are as concrete as "$0" and "$20,000", and counting only digits missed them.
# "one" and "first" are deliberately absent: they are filler far more often
# than they are a quantity.
SPOKEN_NUMBERS = {
    "zero", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "ten", "eleven", "twelve", "fifteen", "twenty", "thirty", "forty", "fifty",
    "sixty", "seventy", "eighty", "ninety", "hundred", "thousand", "million",
    "billion", "dozen", "half", "twice", "triple",
}
MONEY_WORDS = {
    "dollars", "dollar", "bucks", "grand", "percent", "cents",
    "millionaire", "billionaire", "revenue", "profit", "salary", "rent",
}

# Words that put something on the line. A hook with none of these is a
# statement; a hook with one is a reason to keep watching.
STAKES = {
    "stop", "never", "wrong", "mistake", "mistakes", "lost", "lose", "losing",
    "cost", "costs", "broke", "broken", "failed", "failure", "fail", "nobody",
    "no", "not", "don't", "dont", "doesn't", "didn't", "can't", "won't",
    "quit", "quitting", "fired", "deleted", "delete", "killed", "kills", "kill",
    "replaced", "replaces", "cut", "beat", "free", "paid", "charged", "hired",
    "saved", "first",
    "banned", "illegal", "worst", "hate", "hated", "wasted", "waste", "scam",
    "lie", "lied", "lying", "truth", "secret", "hidden", "stole", "stolen",
    "before", "until", "instead", "but", "except", "unless", "problem",
    "risk", "danger", "warning", "regret", "wish", "should", "shouldn't",
    "still", "already", "only", "without", "versus", "vs", "actually",
}

# Openers that spend the first second saying nothing.
WEAK_OPENERS = [
    "so", "ok", "okay", "hey", "hi", "hello", "guys", "yo", "alright",
    "welcome", "today", "basically", "honestly", "look", "listen", "um",
    "just", "let", "lets", "let's", "i wanted", "i want", "one of",
    "have you", "did you", "do you", "are you", "in this", "in today",
    "the thing", "a lot", "there is", "there are", "this is", "it is",
    "as a", "when it", "if you've", "you know",
]

# Imperatives that earn the front position.
IMPERATIVES = {
    "stop", "steal", "copy", "delete", "try", "watch", "read", "save",
    "use", "build", "make", "write", "send", "take", "start", "quit",
    "never", "always", "don't", "dont", "do", "put", "run", "check",
}

# French. Same jobs as the English sets above, written for spoken French.
# "un", "une" and "premier" are left out of the numbers for the same reason
# "one" and "first" are: they are filler far more often than a quantity.
SPOKEN_NUMBERS_FR = {
    "zéro", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf",
    "dix", "onze", "douze", "quinze", "vingt", "trente", "quarante",
    "cinquante", "soixante", "cent", "cents", "mille", "million", "millions",
    "milliard", "milliards", "douzaine", "moitié", "demi", "double", "triple",
}
MONEY_WORDS_FR = {
    "euros", "euro", "balles", "centimes", "pourcent", "bénéfice", "bénéfices",
    "salaire", "loyer", "prix", "marge", "facture",
}
STAKES_FR = {
    "arrête", "arrêtez", "arrêter", "stop", "jamais", "faux", "fausse", "erreur",
    "erreurs", "perdu", "perdue", "perdus", "perdre", "perd", "coûte", "coûté",
    "coûtent", "raté", "ratée", "ratés", "rater", "échec", "échoué", "ruiné",
    "cassé", "viré", "quitté", "supprimé", "tué", "remplacé", "remplace",
    "gratuit", "gratuite", "payé", "payée", "facturé", "sauvé", "premier",
    "première", "interdit", "interdite", "illégal", "pire", "déteste", "détesté",
    "gâché", "gaspillé", "arnaque", "mensonge", "menti", "vérité", "secret",
    "secrète", "caché", "cachée", "volé", "avant", "jusqu'à", "jusqu’à", "sauf",
    "problème", "risque", "danger", "attention", "regret", "regrette",
    "regretté", "devrais", "dois", "encore", "déjà", "seulement", "uniquement",
    "sans", "contre", "vraiment", "personne", "rien", "pas", "mais", "pourtant",
}
WEAK_OPENERS_FR = [
    "alors", "bon", "donc", "bref", "voilà", "voila", "salut", "coucou",
    "bonjour", "bonsoir", "hello", "hey", "yo", "aujourd'hui", "aujourd’hui",
    "en fait", "en gros", "du coup", "écoutez", "écoute", "euh", "bah", "ben",
    "je voulais", "je vais", "on va", "dans cette", "dans ce", "vous savez",
    "tu sais", "est-ce que", "il y a", "y a", "c'est", "c’est", "ceci est",
    "voici", "petit", "petite",
]
IMPERATIVES_FR = {
    "arrête", "arrêtez", "vole", "volez", "copie", "copiez", "supprime",
    "supprimez", "essaie", "essaye", "essayez", "regarde", "regardez", "lis",
    "lisez", "enregistre", "enregistrez", "sauvegarde", "utilise", "utilisez",
    "fais", "faites", "écris", "écrivez", "envoie", "envoyez", "prends",
    "prenez", "commence", "commencez", "jamais", "toujours", "ne", "mets",
    "mettez", "goûte", "goûtez", "viens", "venez", "teste", "testez", "oublie",
    "oubliez", "achète", "achetez",
}
YOU_FR = re.compile(r"(?:^|[^\w])(?:(?:tu|toi|ton|ta|tes|te|vous|votre|vos)(?=[^\w]|$)|t['’])",
                    re.IGNORECASE)
ME_FR = re.compile(r"(?:^|[^\w])(?:(?:je|moi|mon|ma|mes|nous|notre|nos|on)(?=[^\w]|$)|[jm]['’])",
                   re.IGNORECASE)

FR_MARKERS = {
    "le", "la", "les", "des", "une", "est", "et", "pas", "que", "qui", "pour",
    "dans", "avec", "sur", "ce", "cette", "je", "vous", "nous", "du", "au",
    "aux", "mais", "ou", "tu", "mon", "ma", "mes", "il", "elle", "sont", "très",
    "plus", "sans", "chez", "c'est", "j'ai", "on", "ça",
}
EN_MARKERS = {
    "the", "and", "is", "are", "to", "of", "you", "your", "it", "that", "this",
    "with", "for", "in", "my", "we", "was", "have", "not", "but", "what", "how",
    "i", "be", "me",
}


def detect_lang(text):
    """'fr' or 'en'. Function words plus accented letters, nothing cleverer."""
    low = text.lower().replace("’", "'")
    toks = re.findall(r"[^\W\d_]+(?:'[^\W\d_]+)?", low)
    fr = sum(t in FR_MARKERS for t in toks) + 2 * len(re.findall(r"[àâçéèêëîïôûùüœ]", low))
    en = sum(t in EN_MARKERS for t in toks)
    return "fr" if fr > en else "en"


DEALBREAKERS_FR = [
    (re.compile(r"(?i)^\s*(?:arr[êe]te[sz]? de scroller|ne scrolle[sz]? pas|stop,? ne scrolle)"),
     "Opens with \"arrête de scroller\". Asking for attention proves you have not earned it."),
    (re.compile(r"(?i)\b(?:dans (?:cette|la) vidéo|dans ce reel|aujourd['’]hui,? je vais (?:vous|te)"
                r"|je vais (?:vous|te) (?:montrer|expliquer|apprendre)|je vous montre comment)"),
     "Video preamble. Delete it and open on the payoff."),
    (re.compile(r"(?i)^\s*(?:salut|coucou|bonjour|bonsoir|hello|hey)\b"),
     "Greeting. Nobody came to the feed to be greeted."),
]

DEALBREAKERS = [
    (re.compile(r"(?i)^\s*(?:stop scrolling|don'?t scroll)"),
     "Opens with \"stop scrolling\". Asking for attention proves you have not earned it."),
    (re.compile(r"(?i)\b(?:in (?:this|today'?s) (?:video|reel)|i'?m going to show you|i'?ll show you how)\b"),
     "Video preamble. Delete it and open on the payoff."),
    (re.compile(r"(?i)^\s*(?:hey |hi |what'?s up |welcome )"),
     "Greeting. Nobody came to the feed to be greeted."),
    (HASHTAG_RE,
     "Hashtag in the hook. Hashtags belong at the bottom of the caption, if anywhere."),
    (EMOJI_RE,
     "Emoji in the hook. On-screen text at hook size has room for words or for an emoji, not both."),
]


def clamp(n):
    return max(0.0, min(100.0, n))


def words(text):
    # "$18,000" and "18 000 €" are one word when spoken, so one word here too.
    text = re.sub(r"(?<=\d),(?=\d)", "", text)
    text = re.sub(r"(?<=\d)[ \u00a0\u202f](?=\d{3}\b)", "", text)
    return [w for w in WORD_RE.findall(text) if w.strip("-'’")]


def norm(token):
    """Lower case, with a French elision ("l'erreur", "j'ai") taken off."""
    return ELISION_RE.sub("", token.lower()).strip("'’")


def is_number_word(token, t):
    """"six", and the hyphenated ones: "quarante-huit", "twenty-five"."""
    return token in t["numbers"] or (
        "-" in token and any(p in t["numbers"] for p in token.split("-")))


def tables(lang):
    if lang == "fr":
        return {"numbers": SPOKEN_NUMBERS_FR, "money": MONEY_WORDS_FR,
                "stakes": STAKES_FR, "weak": WEAK_OPENERS_FR,
                "imperatives": IMPERATIVES_FR, "you": YOU_FR, "me": ME_FR,
                "dealbreakers": DEALBREAKERS_FR + DEALBREAKERS[3:]}
    return {"numbers": SPOKEN_NUMBERS, "money": MONEY_WORDS, "stakes": STAKES,
            "weak": WEAK_OPENERS, "imperatives": IMPERATIVES,
            "you": re.compile(r"\b(you|your|you're|youre|yourself)\b", re.IGNORECASE),
            "me": re.compile(r"\b(i|my|me|we|our)\b", re.IGNORECASE),
            "dealbreakers": DEALBREAKERS}


def check_length(text):
    """A hook has to land before the thumb moves. Roughly two seconds."""
    w = words(text)
    n = len(w)
    secs = n / 2.75                      # ~165 words per minute, spoken
    chars = len(text.strip())
    if 5 <= n <= 12:
        score = 100.0
    elif n < 5:
        score = clamp(100 - (5 - n) * 20)
    else:
        score = clamp(100 - (n - 12) * 11)
    if chars > 60:                       # two lines of big on-screen text
        score -= 12
    return clamp(score), f"{n} words, {chars} chars, ~{secs:.1f}s spoken (want 5-12 words)"


def check_specificity(text, t):
    """One concrete thing beats three abstract ones."""
    nums = [n.strip() for n in NUMBER_RE.findall(text) if n.strip()]
    propers = set(PROPER_RE.findall(text))
    low = [norm(w) for w in words(text)]
    spoken = [w for w in low if is_number_word(w, t) or w in t["money"]]
    hits = len(nums) + len(propers) + len(spoken)
    score = 15.0 if hits == 0 else clamp(45 + hits * 30)
    found = ", ".join(nums[:2] + sorted(propers)[:2] + spoken[:2])
    return score, (f"{hits} concrete marker(s)" + (f": {found}" if found else
                   " - no number, no name, nothing checkable"))


def check_stakes(text, t):
    """Tension, cost, negation. Something the viewer might lose."""
    w = [norm(x) for x in words(text)]
    hits = [x for x in w if x in t["stakes"]]
    markers = sorted(set(hits))
    if re.search(r"\$\s?\d|\d\s?€|€\s?\d", text):
        markers.append("a price")
    n = len(markers)
    score = {0: 20.0, 1: 70.0}.get(n, 100.0)
    detail = f"{n} tension marker(s)" + (f": {', '.join(markers[:4])}" if markers else
                                         " - nothing is at stake in this line")
    return clamp(score), detail


def check_frontload(text, t):
    """The interesting word cannot be in position nine."""
    w = words(text)
    if not w:
        return 0.0, "empty"
    raw = [x.lower().replace("’", "'").strip("'") for x in w]
    low = [norm(x) for x in w]
    # Whole words only: "so" must not match "soon".
    opener = " ".join(raw[:3]) + " "
    penalty = 0
    hit_opener = None
    for weak in t["weak"]:
        if opener.startswith(weak.replace("’", "'") + " "):
            penalty, hit_opener = 30, weak
            break
    payload = None
    for i, token in enumerate(low):
        if (token in t["stakes"] or is_number_word(token, t) or token in t["money"]
                or NUMBER_RE.match(w[i]) or (i and PROPER_RE.match(w[i]))):
            payload = i
            break
    if payload is None:
        base = 30.0
        where = "no payload word anywhere in the line"
    elif payload <= 3:
        base = 100.0
        where = f"payload at word {payload + 1}"
    elif payload <= 6:
        base = 70.0
        where = f"payload at word {payload + 1}, could move forward"
    else:
        base = 40.0
        where = f"payload at word {payload + 1}, too late"
    detail = where + (f"; weak opener \"{hit_opener}\"" if hit_opener else "")
    return clamp(base - penalty), detail


def check_address(text, t):
    """Aimed at one viewer, or floating in the air."""
    w = [norm(x) for x in words(text)]
    if t["you"].search(text):
        return 100.0, "speaks to the viewer"
    if w and w[0] in t["imperatives"]:
        return 90.0, f"imperative opener (\"{w[0]}\")"
    if t["me"].search(text):
        return 70.0, "first person, no viewer named"
    return 35.0, "third person, nobody in the room"


CHECKS = ["LENGTH", "SPECIFICITY", "STAKES", "FRONTLOAD", "ADDRESS"]


def run(text, lang="auto"):
    if lang == "auto":
        lang = detect_lang(text)
    t = tables(lang)
    results = {
        "LENGTH": check_length(text),
        "SPECIFICITY": check_specificity(text, t),
        "STAKES": check_stakes(text, t),
        "FRONTLOAD": check_frontload(text, t),
        "ADDRESS": check_address(text, t),
    }
    flags = [msg for pattern, msg in t["dealbreakers"] if pattern.search(text)]
    scores = [results[c][0] for c in CHECKS]
    # The weakest property caps the hook, same logic as detect.py: one bad
    # property is enough for the thumb to keep moving.
    overall = statistics.mean(scores) * 0.6 + min(scores) * 0.4 - len(flags) * 15
    overall = clamp(overall)
    verdict = "STRONG" if overall >= 70 and min(scores) >= 55 and not flags else (
        "OK" if overall >= 50 else "WEAK")
    return results, overall, verdict, flags


def bar(score, width=24):
    filled = round(score / 100 * width)
    return "#" * filled + "." * (width - filled)


def render_one(text, results, overall, verdict, flags, out=sys.stdout):
    print("\nHOOK SCORE", file=out)
    print("=" * 62, file=out)
    print(f"  \"{text.strip()}\"\n", file=out)
    for name in CHECKS:
        score, detail = results[name]
        print(f"  {name:<13} {bar(score)} {score:5.1f}", file=out)
        print(f"  {'':<13} {detail}", file=out)
    print("-" * 62, file=out)
    print(f"  {'HOOK SCORE':<13} {bar(overall)} {overall:5.1f}   {verdict}", file=out)
    for f in flags:
        print(f"\n  DEALBREAKER  {f}", file=out)
    if verdict != "STRONG":
        weakest = min(CHECKS, key=lambda c: results[c][0])
        print(f"\n  Weakest property: {weakest}. Fix that one and re-run.", file=out)
    print("", file=out)


def render_table(rows, out=sys.stdout):
    print("\nHOOK RANKING\n" + "=" * 78, file=out)
    for i, r in enumerate(rows, 1):
        mark = "->" if i == 1 else "  "
        hook = r["hook"] if len(r["hook"]) <= 62 else r["hook"][:59] + "..."
        print(f"{mark} {r['score']:5.1f} {r['verdict']:<7} {hook}", file=out)
        print(f"        weakest: {r['weakest']} ({r['checks'][r['weakest']]['score']:.0f})", file=out)
        for f in r["flags"]:
            print(f"        dealbreaker: {f}", file=out)
    print("\nShoot the top one. If the top one is under 50, none of these are the hook.\n",
          file=out)


def main():
    ap = argparse.ArgumentParser(description="Score a Reel hook on five properties.")
    ap.add_argument("input", nargs="?", default="-", help="file with one hook per line, or -")
    ap.add_argument("--hook", help="score a single hook given on the command line")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--lang", choices=["auto", "fr", "en"], default="auto",
                    help="word lists to score against (default: detect per hook)")
    args = ap.parse_args()

    if args.hook:
        lines = [args.hook]
    else:
        raw = sys.stdin.read() if args.input == "-" else open(args.input, encoding="utf-8").read()
        lines = [l.strip() for l in raw.splitlines() if l.strip()]
    if not lines:
        print("nothing to score", file=sys.stderr)
        sys.exit(2)

    payload = []
    for line in lines:
        results, overall, verdict, flags = run(line, args.lang)
        payload.append({
            "hook": line,
            "lang": detect_lang(line) if args.lang == "auto" else args.lang,
            "checks": {k: {"score": round(v[0], 1), "detail": v[1]} for k, v in results.items()},
            "weakest": min(CHECKS, key=lambda c: results[c][0]),
            "flags": flags,
            "score": round(overall, 1),
            "verdict": verdict,
        })

    if args.json:
        print(json.dumps(payload if len(payload) > 1 else payload[0], indent=2, ensure_ascii=False))
        return

    if len(payload) == 1:
        results, overall, verdict, flags = run(lines[0], args.lang)
        render_one(lines[0], results, overall, verdict, flags)
    else:
        render_table(sorted(payload, key=lambda r: -r["score"]))

    sys.exit(0 if max(p["score"] for p in payload) >= 70 else 1)


if __name__ == "__main__":
    main()
