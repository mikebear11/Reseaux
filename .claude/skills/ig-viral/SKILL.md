---
name: ig-viral
description: >-
  Aller chercher les Reels qui marchent vraiment en ce moment dans la niche de
  l'utilisateur, les classer selon l'écart avec leur propre compte, nommer la
  formule d'accroche de chacun et en faire un fichier d'inspiration (swipe
  file) à partir duquel tourner. À utiliser quand l'utilisateur dit « trouve
  des vidéos virales », « qu'est-ce qui marche en ce moment », « qu'est-ce que
  les gens postent dans ma niche », « décortique ce compte », « fais-moi un
  swipe file », « pourquoi ce reel cartonne », ou demande quoi faire ensuite
  sans avoir de preuve pour répondre.
---

# ig-viral

Le skill de recherche. Tout le reste de ce pack écrit ; celui-ci va regarder.
Lancez-le une fois par mois, pas tous les jours. Les formules durent une
saison.

Un outil vit dans ce dossier et il fonctionne :

```bash
python3 swipe.py captured.tsv --out "$(git rev-parse --show-toplevel)/instagram/swipe.md"
```

Il accepte `--lang auto|fr|en` (par défaut `auto`) et classe les accroches avec
les expressions régulières anglaises et françaises de `hooks.json`.

## Langue et ton

- Rédigez en français : rapport, analyse, et les accroches « votre version ».
  Les accroches relevées sont citées mot pour mot, dans leur langue d'origine.
- Respectez le tutoiement ou le vouvoiement indiqué dans `voice.md`. S'il n'y
  est pas, demandez une fois ; sans réponse, vouvoiement par défaut.
- Typographie française correcte : « guillemets », espace avant ; : ! ?
  acceptable. Pas de tiret cadratin.

Les comptes étrangers analysés ne sont pas soumis à la Loi Évin : leurs formats
ne sont pas transposables tels quels pour de l'alcool en France (voir
`../ig-caption/loi-evin.md` avant de les confier à `/ig-reel`).

## La seule idée qui rend l'exercice utile

**Les vues brutes ne sont pas une preuve.** Un compte de deux millions
d'abonnés qui fait 400 000 vues a eu un mardi tranquille. Un compte de quatre
mille abonnés qui fait 400 000 vues a trouvé quelque chose, et ce quelque chose
se copie.

Donc tout ici se classe sur le **multiple de surperformance** : les vues
divisées par la médiane récente de ce compte. Tout ce qui dépasse 3x est un
signal. Tout ce qui est sous 1,5x est une journée normale pour ce compte et
n'apprend rien, aussi gros que paraisse le chiffre.

Retenez des comptes **à environ 10x de la taille de l'utilisateur au plus**.
Une formule qui marche à 2 M d'abonnés marche souvent parce qu'elle est à 2 M
d'abonnés.

## Étape 1 : choisir les comptes

Demandez à l'utilisateur 6 à 12 comptes, ou proposez-les et faites-les valider :

- **4 directs** : même niche, même offre, un peu en avance.
- **4 voisins** : autre niche, même public. C'est là qu'on emprunte des formats
  avant que quiconque dans la niche les ait.
- **2 à 4 surdimensionnés** : des comptes bien plus gros, pour le format
  uniquement, jamais pour le rythme de publication ni le ton.

Demandez-lui aussi d'ouvrir sa propre **collection Enregistrements**. C'est le
corpus le plus rapide et le plus pertinent qui existe, et il est déjà filtré
par son goût.

## Étape 2 : aller regarder

Utilisez l'outil de navigation dont cette session dispose réellement : un
navigateur intégré, une extension connectée au Chrome de l'utilisateur, ou un
outil de contrôle de l'ordinateur. Il n'y a pas d'API pour ça et il n'en faut
pas, parce que le volume est assez petit pour être lu.

**Règles non négociables :**

- **Ne vous connectez jamais à Instagram à la place de l'utilisateur et ne
  demandez jamais de mot de passe.** Si une page exige une connexion, c'est
  l'utilisateur qui est déjà connecté. Pilotez son navigateur en sa présence,
  ou demandez-lui de coller le contenu.
- **C'est de la lecture, pas de l'aspiration.** Dix comptes, une douzaine de
  Reels chacun, à vitesse humaine. La collecte automatisée en volume enfreint
  les Conditions d'utilisation d'Instagram et fait bloquer les comptes. Ne
  construisez pas de robot d'indexation, n'utilisez pas de service
  d'extraction, et ne faites pas tourner ça en boucle en arrière-plan.
- **Copiez la formule, jamais la vidéo.** La forme de l'accroche, la
  structure, la durée, le rythme des coupes. Pas leur script, pas leur voix,
  pas leur montage. Attribuez chaque ligne du fichier d'inspiration au compte
  dont elle vient.

**Ce qu'il faut relever par Reel**, dans les mots du créateur :

| champ | notes |
| --- | --- |
| account | le @ du compte |
| followers | depuis le profil |
| median | parcourez les 12 derniers Reels à l'œil et prenez le nombre de vues du milieu |
| views | ce Reel |
| hook | la première phrase, parlée ou à l'écran, mot pour mot, fautes comprises |
| on-screen | la première carte de texte à l'écran, si elle diffère |
| length | en secondes |
| cta | ce qu'ils demandent à la fin |

La médiane est le champ important. Sans elle, on revient au classement par
nombre d'abonnés, ce que ce skill existe précisément pour empêcher.

**Quand Instagram ne montre pas assez :** la même grammaire d'accroche tourne
sur YouTube Shorts, où les nombres de vues et les transcriptions sont publics
et où aucune connexion n'est nécessaire. C'est un second corpus légitime, et
l'accroche parlée y est plus facile à obtenir :

```bash
# nombres de vues des Shorts d'une chaîne
python3 -m yt_dlp --flat-playlist --playlist-end 40 -J \
  "https://www.youtube.com/@HANDLE/shorts" > channel.json

# la première phrase parlée d'un Short, depuis ses sous-titres automatiques
# (comptes français : "fr.*" ; comptes anglophones : "en.*")
python3 -m yt_dlp --skip-download --write-auto-subs --sub-langs "fr.*" \
  --sub-format json3 -o hook "https://www.youtube.com/watch?v=VIDEO_ID"
```

Prenez chaque mot des sous-titres horodaté sous 3,0 secondes. C'est
l'accroche, telle qu'elle est dite, pas telle qu'elle est écrite.

## Étape 3 : classer

Remplissez un fichier séparé par des tabulations avec une ligne d'en-tête (les
noms de colonnes restent en anglais, le script les attend ainsi) et lancez le
script :

```
account	followers	median	views	hook
@brasserie_exemple	48000	11000	412000	personne ne vous dit que vos 30 premiers brassins vont rater
```

```bash
python3 swipe.py captured.tsv --out "$(git rev-parse --show-toplevel)/instagram/swipe.md"
```

Il calcule le multiple de surperformance, nomme la formule d'accroche à partir
des 26 formules que `/ig-reel` utilise, note chaque accroche avec
`hookscore.py`, et affiche ce qui sépare le tiers supérieur du tiers inférieur.

## Étape 4 : dire ce que ça veut dire, prudemment

Rapportez trois choses, pas plus :

1. **Quelles formules sont surreprésentées** dans le tiers supérieur, avec les
   effectifs. Deux formules apparaissant chacune quatre fois sur six comptes,
   c'est un résultat. Une qui apparaît deux fois, non.
2. **Ce que le tiers supérieur a en commun sur le plan de la structure** et
   que le tiers inférieur n'a pas : longueur de l'accroche, chute visuelle ou
   non, première image en mouvement ou non, place de la demande.
3. **Les lignes non classées.** Chaque accroche que le classificateur n'a pas
   pu nommer est soit du bruit, soit une formule qui n'est pas encore dans
   `hooks.json`. Lisez-les à la main. C'est la colonne la plus précieuse de la
   sortie, et c'est pour ça que le script en affiche le nombre.

Puis donnez la taille de l'échantillon et le niveau de confiance en mots
simples. Quarante Reels sur six comptes appuient une affirmation. Douze, non,
et le dire, c'est la différence entre de la recherche et un horoscope.

## Étape 5 : en faire quelque chose à tourner

Pour les trois meilleures formules, écrivez **la version de l'utilisateur** :
son histoire, son chiffre, dans la forme qui marche. Confiez chacune à
`/ig-reel` avec l'identifiant de formule déjà choisi.

Ne rendez jamais « faites un Reel comme celui-ci ». Rendez une accroche qu'il
pourrait dire demain.

## Sortie (exemple fictif)

```
FICHIER D'INSPIRATION  ·  38 Reels  ·  7 comptes  ·  référence : médiane du compte

SURPERFORMANCES (au-dessus de 3x)
  38,4x  accroche 86  #3  Personne ne vous dit   @compte_a    412 000  (médiane 10 700)
  11,2x  accroche 79  #9  À voler                @compte_c    180 000  (médiane 16 100)
  ...

CE QUI EST SURREPRÉSENTÉ
  #3 Personne ne vous dit   x5 dans le tiers supérieur, 0 dans le tiers inférieur
  #2 L'ordre négatif        x4
  longueur médiane d'accroche   8 mots en haut, 19 en bas

NON CLASSÉES (6)
  Deux d'entre elles ont la même forme et elle n'est pas dans hooks.json :
  une accroche qui commence par le commentaire de quelqu'un d'autre lu à voix
  haute. À ajouter.

VOTRE VERSION
  #3  « Personne ne vous dit que les 20 premiers brassins sont faits pour rater. »
  ...
```

Écrivez le fichier d'inspiration dans `instagram/swipe.md`.
`/ig-reel` et `/ig-plan` le lisent tous les deux, et c'est tout l'intérêt :
après un premier passage, le reste du pack travaille à partir des preuves de
l'utilisateur et non plus de valeurs par défaut.

Ce skill ne publie rien, ne suit personne, n'aime rien et n'envoie aucun
message. Il lit.
