# Collection de skills VoltAgent : où piocher

Copie de la liste `VoltAgent/awesome-agent-skills` (licence MIT, voir `LICENSE`),
prise au commit `6d483e2` du 05/11/2026 :
https://github.com/VoltAgent/awesome-agent-skills

`README.md` est la liste complète, environ 2 000 lignes. Elle ne contient que
des liens : les skills restent chez leurs auteurs.

## Avant d'installer quoi que ce soit

- La liste est **triée, pas auditée** (c'est écrit dans sa section
  « Security Notice »). Une skill peut contenir des injections de prompt ou du
  code malveillant, et son auteur peut la modifier à tout moment. Lire chaque
  fichier avant de l'ajouter dans `.claude/skills/`.
- Une skill importée ne remplace pas les règles de `CLAUDE.md` : message
  sanitaire, pas de « bio », rien d'inventé, pas de publication sans « oui ».
- La plupart de ces skills sont écrites pour des SaaS américains et en anglais.
  Il faudra les adapter.

## Repérées pour @sulauze (descriptions lues dans la liste, skills pas testées)

| Skill | Ligne du README | Intérêt possible | Réserve |
|---|---|---|---|
| `coreyhaines31/social` | 931 | Contenus réseaux, Instagram compris | Recoupe nos `ig-*` |
| `coreyhaines31/copywriting`, `copy-editing` | 909-910 | Textes du site, fiches produit | Écrit pour le SaaS |
| `coreyhaines31/content-strategy` | 908 | Choix des sujets et des formats | Recoupe `ig-plan` |
| `coreyhaines31/ads` | 918 | Campagnes Meta | Pub pour l'alcool soumise à la loi Évin |
| `coreyhaines31/seo-audit`, `ai-seo` | 903, 928 | Site sulauze.com | Hors Instagram |
| `blader/humanizer` | 1539 | Retirer l'effet « texte d'IA » | En anglais ; `ig-human` existe déjà |
| `remotion-dev/remotion` | 397 | Montage vidéo en code (Reels) | Demande Node et du développement |
| `anthropics/canvas-design` | 119 | Visuels PNG ou PDF | Déjà disponible ici |

## À ne pas utiliser sans vérification

- `dreammis/instagram-upload` (ligne 1582) et `taisly/agent` (ligne 1545)
  publient sur Instagram. Notre seul canal autorisé est vidIQ, qui passe par
  l'API officielle de Meta. Je n'ai pas vérifié comment ces deux-là publient.
  Si c'est par automatisation du navigateur, c'est interdit (`CLAUDE.md`).
