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

### Démarrer

Compléter et valider `instagram/voice.md` (les lignes « À CONFIRMER » et les
cases vides). `templates/voice.md` reste le modèle vierge.
