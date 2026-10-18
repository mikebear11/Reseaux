---
name: ig-profile
description: >-
  Noter un profil Instagram sur 100 selon une grille en 12 points et réécrire
  les parties qui perdent des points : champ nom, bio, lien, stories à la une,
  les trois épinglés, grille. À utiliser quand l'utilisateur dit « optimise mon
  profil », « corrige ma bio », « note mon Instagram », « pourquoi les gens ne
  s'abonnent pas ? », ou colle son profil et demande comment il se lit.
---

# ig-profile

Presque tout le monde optimise la mauvaise chose ici. Le profil n'est pas une
vitrine qu'on parcourt. C'est un **écran de décision**, où l'on arrive depuis un
seul Reel, et il a environ trois secondes pour répondre à une question : est-ce
qu'il y a d'autres choses comme ça ici, et est-ce que c'est pour moi.

## Langue et ton

- Rédigez en français, réécritures comprises.
- Respectez le tutoiement ou le vouvoiement indiqué dans
  `~/.claude/instagram/voice.md`. S'il n'y est pas, demandez une fois ; sans
  réponse, vouvoyez. La bio suit le même choix.
- Typographie française : « guillemets », espace avant ; : ! ? acceptée. Pas de
  tiret cadratin. Le français est plus long : les limites de 30 et 150
  caractères ne bougent pas, comptez-les.

## Loi Évin

Lisez `../ig-caption/loi-evin.md` avant de réécrire le profil d'une brasserie.

- La bio, le champ nom et les noms des stories à la une s'appuient sur ce que
  L3323-4 autorise : nom et adresse de la brasserie, origine, mode de brassage,
  médailles, où acheter.
- Si le profil montre ou nomme une bière (bio, couvertures, épinglés), prévoyez
  le message sanitaire « L'abus d'alcool est dangereux pour la santé » sur les
  posts concernés.
- Tout le reste (promesse d'ambiance, de fête, humour) est signalé « À FAIRE
  VALIDER (Loi Évin) » dans le récapitulatif. Pas de mineur sur la photo ni sur
  les couvertures, pas de parrainage, collaboration d'influenceur payée à faire
  valider.
- Ne dites jamais qu'un profil « respecte la Loi Évin ».

## Entrée

Demandez à l'utilisateur de coller ou de capturer : le champ nom, le nom de
compte, la bio, la destination du lien, les noms des stories à la une, ce qui
est épinglé, et les neuf premières couvertures de la grille. Une capture du haut
du profil plus les deux premières lignes de la grille suffit pour un premier
passage.

Ne vous connectez pas à Instagram à sa place.

## Notez-le

Lisez `rubric.json` dans ce dossier. Douze critères, 100 points, chacun avec ce
à quoi ressemble la note maximale et comment il échoue d'habitude. Notez chaque
critère, montrez le tableau, donnez le total. Soyez honnête. La plupart des
profils tombent entre 30 et 49 au premier passage, et une note généreuse ne sert
à rien.

```
NOTE DU PROFIL  38/100

  champ nom          2/12   un nom seul, aucun mot que quelqu'un recherche
  bio, ligne 1       3/12   trois noms communs et un emoji de chope
  les trois épinglés 0/10   rien d'épinglé
  stories à la une   2/8    « Divers », « La vie », « 2023 »
  lisibilité grille  4/8    six couvertures sur neuf sont un visage en pleine phrase
  ...
```

## Puis réécrivez, dans cet ordre

Corrigez par ordre décroissant de points perdus. Ne réécrivez pas tout d'un
coup : l'utilisateur doit réellement aller changer chacun de ces champs.

**1. Le champ nom (30 caractères).** La ligne en gras sous la photo, pas le nom
de compte. C'est le champ qu'interroge la recherche Instagram, et la plupart des
comptes n'y mettent qu'un nom. Format qui fonctionne :
`{Nom} | {ce que vous faites, avec les mots recherchés}`. Donnez trois options.

**2. La ligne 1 de la bio.** Pour qui c'est, et ce qui change. Pas un intitulé
de poste, pas des adjectifs, pas une liste d'identités séparées par des barres.
Le reste des 150 caractères porte une preuve ou une offre claire.

**3. Les trois épinglés.** Trois emplacements, trois rôles différents : la
meilleure preuve, l'explication la plus claire de l'offre, la meilleure
présentation de la personne (ou de la brasserie). C'est la correction qui a le
plus d'effet sur tout le profil, et elle prend quatre taps. Une grille sans
épinglés montre ce qui a été publié en dernier, autant jouer à pile ou face.

**4. Les stories à la une.** Quatre à six, nommées d'après les questions que
pose un acheteur : Tarifs, Résultats, Comment ça marche, À propos (pour une
brasserie, par exemple : Où nous trouver, Nos bières, Le brassage, À propos).
Pas « Divers ». Supprimez le reste.

**5. Le lien.** Une seule destination, qui correspond à ce que la bio vient de
promettre. Cinq sont autorisés ; deux, c'est déjà un menu, et un menu convertit
moins bien qu'une porte.

**6. Les couvertures de la grille.** Les neuf premières, en vignette. Les
couvertures de Reels se choisissent, on ne laisse pas la première image par
défaut. Quatre mots de texte sur une couverture rendent une grille lisible d'un
coup d'œil.

## Sortie

Le tableau de notes, puis les réécritures en blocs prêts à copier, dans l'ordre
des corrections, chacune passée dans `/ig-human`. Renotez à la fin et montrez
l'écart honnêtement. Si la réécriture atteint 84 et pas 98, dites 84, et dites
ce qu'il faut pour le reste : en général une grille, une habitude de stories et
un post épinglé qui n'existe pas encore. Rien de tout cela n'est une
réécriture.

Terminez par la ligne Loi Évin, par exemple :

```
loi Évin :  message sanitaire à ajouter sur 2 épinglés · 1 élément À FAIRE VALIDER (bio : « l'apéro du vendredi »)
```

Ce skill n'enregistre rien sur Instagram. L'utilisateur modifie chaque champ
lui-même.
