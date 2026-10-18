# Reseaux

Outils pour gérer les réseaux sociaux.

## Skills Instagram (`.claude/skills/ig-*`)

13 skills Claude Code copiés tels quels depuis
[Jakeschincariol/instagram-agent-skill](https://github.com/Jakeschincariol/instagram-agent-skill)
(commit `d03c56b`, licence MIT, voir `.claude/skills/LICENSE-instagram-agent-skill`).

Ils sont chargés automatiquement quand Claude Code est ouvert dans ce dépôt :
`/ig-reel`, `/ig-caption`, `/ig-carousel`, `/ig-story`, `/ig-profile`, `/ig-plan`,
`/ig-human`, `/ig-comment`, `/ig-reply`, `/ig-dm`, `/ig-repurpose`, `/ig-audit`, `/ig-viral`.

Aucun skill ne publie sur Instagram : ils rédigent, vous publiez.
Les scripts Python n'utilisent que la bibliothèque standard et n'accèdent pas au réseau.

### Limites connues

- **Tout est en anglais.** Les scripts `hookscore.py`, `detect.py`, `humanize.py`
  et la détection des appels à l'action de `caption.py` reposent sur des listes de
  mots anglais. Sur un texte français, leurs scores sont faussés (ex. « raté »
  n'est pas reconnu comme enjeu, « on / vous » ne comptent pas comme adresse).
  `caption.py` reste fiable pour la longueur, la troncature à 125 caractères,
  les hashtags (plafond de 5 depuis le 18/12/2025) et les liens.
- Les fichiers de travail (`voice.md`, `log.md`, `swipe.md`, `plan.md`) sont
  écrits dans `~/.claude/instagram/`, qui n'est pas conservé dans une session
  cloud éphémère. Copiez-les dans le dépôt si vous voulez les garder.

### Démarrer

Remplir `templates/voice.md` (votre ton, votre cible, vos chiffres réels), puis
le copier dans `~/.claude/instagram/voice.md`.
