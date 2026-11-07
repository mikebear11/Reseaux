# Reseaux

Outils pour gérer les réseaux sociaux de la Brasserie de Sulauze (`@sulauze`).
Le contexte du compte et les règles sont dans `CLAUDE.md` ; le profil de ton
pré-rempli est dans `instagram/voice.md`.

## Skills Instagram (`.claude/skills/ig-*`)

13 skills Claude Code copiés tels quels depuis
[Jakeschincariol/instagram-agent-skill](https://github.com/Jakeschincariol/instagram-agent-skill)
(commit `d03c56b`, licence MIT, voir `.claude/skills/LICENSE-instagram-agent-skill`).

Ils sont chargés automatiquement quand Claude Code est ouvert dans ce dépôt :
`/ig-reel`, `/ig-caption`, `/ig-carousel`, `/ig-story`, `/ig-profile`, `/ig-plan`,
`/ig-human`, `/ig-comment`, `/ig-reply`, `/ig-dm`, `/ig-repurpose`, `/ig-audit`, `/ig-viral`.

Aucun skill ne publie sur Instagram : ils rédigent, vous publiez.
Les scripts Python n'utilisent que la bibliothèque standard et n'accèdent pas au réseau.

### Adaptation française

Les 13 skills sont traduits et adaptés au français. Les 6 scripts détectent la
langue du texte (`--lang auto|fr|en`) ; sur un texte anglais, ils donnent
exactement le même résultat que l'original (vérifié sur les exemples de l'auteur).

- `hookscore.py`, `beats.py` : listes de mots françaises (enjeux, ouvertures
  faibles, impératifs, nombres dits à l'oral), montants en €, « 18 000 € »
  compté comme un mot, élisions (« l'erreur », « j'ai »).
- `hooks.json` : chaque formule a un nom, un modèle, un exemple et une regex
  de détection en français (`*_fr`). Les exemples sont fictifs.
- `caption.py` : appels à l'action français, hashtags accentués
  (`#bièreartisanale`), et contrôle **ÉVIN** : échec si la légende parle
  d'alcool sans « L'abus d'alcool est dangereux pour la santé ».
- `humanize.py`, `detect.py` : lexique français `slop.fr.json` ; la
  typographie française (’, « », espace avant ; : ! ?) n'est plus comptée
  comme empreinte machine ; la voix est mesurée sur les marques de l'oral.
- `ig-caption/loi-evin.md` : ce que dit la Loi Évin pour un post de brasserie,
  avec les articles sourcés. Les skills qui produisent du contenu s'y réfèrent.

### Limites connues

- **Rien n'est calibré sur du français réel.** Les seuils (5 à 12 mots,
  165 mots/min, scores de passage) sont ceux de l'auteur, mesurés en anglais.
  Le lexique `slop.fr.json` et les regex `match_fr` sont écrits à la main,
  pas mesurés sur un corpus.
- **La sortie des scripts reste en anglais** (PASS, STRONG, weakest…). Claude
  la résume en français.
- **Le contrôle ÉVIN ne vérifie qu'une phrase**, le message sanitaire. Il ne
  dit pas qu'un post est conforme. Ce n'est pas un avis juridique.
- Les fichiers de travail (`voice.md`, `log.md`, `swipe.md`, `plan.md`) sont
  dans `instagram/` à la racine du dépôt : à commiter après chaque
  modification, sinon une session cloud les perd.

## Skills Google (`.claude/skills/avis-google`, `.claude/skills/seo-local`)

Adaptés de deux skills de
[OneWave-AI/claude-skills](https://github.com/OneWave-AI/claude-skills)
(commit `b2267d9`, licence MIT, voir `.claude/skills/LICENSE-onewave-claude-skills`) :
`review-response-writer` → `/avis-google`, `local-seo-optimizer` → `/seo-local`.
Ce ne sont pas des copies : réécrits en français, avec les règles de la
brasserie (message sanitaire, pas de « bio », rien d'inventé) et les règles
Google et françaises sourcées dans `avis-google/regles-google.md` (consultées
le 07/11/2026). Retiré de l'original : les chiffres sans source, et le conseil
de faire citer des mots-clés aux clients dans leurs avis (interdit par Google).

Aucun des deux ne publie ni ne modifie la fiche Google : ils rédigent et
auditent, la brasserie applique. Fichiers de travail : `google/` à la racine
(à créer à la première utilisation, à commiter).

Non repris : les 227 autres skills du dépôt (hors sujet ou en doublon avec
les `ig-*`), et `hyperframes-local-promo`, qui dépend des skills HyperFrames
non installés ici.

### Démarrer

Compléter et valider `instagram/voice.md` (les lignes « À CONFIRMER » et les
cases vides). `templates/voice.md` reste le modèle vierge.

## Skill `karpathy-guidelines` (`.claude/skills/karpathy-guidelines`)

`SKILL.md` traduit en français et adapté au contenu à partir de
[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)
(commit `2c60614`). Licence MIT déclarée dans l'en-tête du skill et dans
`.claude-plugin/plugin.json` du dépôt d'origine (auteur : forrestchang) ; ce
dépôt ne contient pas de fichier LICENSE.

Quatre règles de comportement pour Claude : réfléchir avant d'agir (dire ses
hypothèses, demander si c'est flou), faire simple, ne toucher que ce qui est
demandé, fixer un critère de réussite vérifiable. L'original ne vise que le code ;
cette version l'étend aux légendes, Reels et fichiers de travail, avec des
exemples propres à la brasserie, les citations de Karpathy reprises par le dépôt
d'origine, un tableau des erreurs à éviter et les signes que les règles
marchent. Le résumé est aussi dans `CLAUDE.md` (chargé à chaque session).
Les « Règles qui priment sur tout » de `CLAUDE.md` restent prioritaires.
