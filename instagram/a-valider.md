# File de validation @sulauze

Contenus prêts qui attendent un « oui » de la brasserie (Reel, légende,
carrousel, story, commentaire, DM, réponse d'avis). Idée reprise de la
validation humaine de Paperclip (paperclipai/paperclip, MIT).

Statuts : `brouillon` → `relu` (verdict du `relecteur`) → `validé` (« oui »
explicite sur ce texte exact) → `publié` ou `abandonné`.

- Un contenu prêt est ajouté ici avec son texte exact, puis commité.
- Si le texte change après `relu` ou `validé`, il repasse en `brouillon`.
- `validé` ne vaut que pour le texte et le compte écrits ici.
- Une fois `publié` (ligne ajoutée dans `log.md`) ou `abandonné`, retirer
  l'entrée de cette file.

| date | format | compte | statut | titre |
| --- | --- | --- | --- | --- |

<!-- Une section par contenu, sous le tableau :

## {{titre}}

Texte exact :

> …

Faits utilisés (source) :
-->
