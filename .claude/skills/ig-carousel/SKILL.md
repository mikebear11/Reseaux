---
name: ig-carousel
description: >-
  Construire un carrousel Instagram : la couverture qui mérite le swipe, le
  texte slide par slide et les fichiers 1080x1350 à publier. À utiliser quand
  l'utilisateur dit « carrousel », « fais-moi un carrousel sur… », « des
  slides », « un post à faire défiler », « transforme ça en carrousel », ou a
  une idée en forme de liste ou d'étapes qui mourrait en image seule.
---

# ig-carousel

Les carrousels sont le format de la grille où l'on reste le plus longtemps,
parce qu'un swipe est une interaction et qu'un défilement n'en est pas une. Ils
ont aussi une deuxième chance : Instagram peut remontrer un carrousel en
commençant par une slide plus loin à quelqu'un qui n'a pas interagi la première
fois. La slide 2 doit donc tenir debout toute seule elle aussi.

Le format récompense une idée découpée en étapes. Il punit une légende coupée en
morceaux.

## Langue et ton

- Rédigez en français.
- Respectez le tutoiement ou le vouvoiement indiqué dans
  `instagram/voice.md`. S'il n'y est pas, demandez une fois ; sans
  réponse, vouvoyez.
- Typographie française : « guillemets », espace avant ; : ! ? acceptée. Pas de
  tiret cadratin. Le français est plus long que l'anglais : comptez les mots,
  les limites ci-dessous ne bougent pas.

## Loi Évin

**Règle absolue de la brasserie.** Dès qu'un contenu parle d'alcool, ou que
sa photo ou sa vidéo s'y rapporte (bière, verre, bouteille, canette, fût,
tireuse, cuve, comptoir, dégustation, brassage…), il porte la phrase
**« L'abus d'alcool est dangereux pour la santé. »** Sans exception, même quand
le texte ne nomme aucune bière. Dans le doute, mettez-la. Elle s'ajoute en fin
de texte, ne compte pas comme appel à l'action, et `/ig-human` ne la retire
jamais. Si `voice.md` donne une formule plus longue (par exemple « …, à
consommer avec modération »), utilisez celle-là.

Lisez `../ig-caption/loi-evin.md` avant tout carrousel de brasserie.

- Toute slide qui parle d'alcool ou dont l'image s'y rapporte porte le message sanitaire
  « L'abus d'alcool est dangereux pour la santé », en petit mais lisible, et
  la légende le porte aussi.
- Un carrousel en étapes se prête bien à ce que L3323-4 autorise : brassage,
  ingrédients, origine, degré, arômes, couleur, médailles, où acheter.
  Construisez d'abord là-dessus.
- Tout le reste (fête, trinquer, humour, séduction, sport) est signalé « À
  FAIRE VALIDER (Loi Évin) » dans le récapitulatif.
- Pas de mineur sur aucune slide, pas de parrainage. Un carrousel fait avec un
  influenceur payé se fait valider avant.
- Ne dites jamais que le carrousel « respecte la Loi Évin ».

## Quand le préférer à un Reel

Choisissez un carrousel quand l'idée a **une séquence et doit être relue** : des
étapes, une méthode en plusieurs parties, un avant / après, une liste qui mérite
une capture d'écran. Choisissez un Reel quand l'idée a du mouvement, un visage,
ou une chute qu'il faut voir se produire.

Si l'idée tient en une seule affirmation, ce n'est ni l'un ni l'autre.
Passez-la à `/ig-reel` et dites-le.

## Structure

6 à 10 slides. Le maximum est 20, et 20, c'est presque toujours un livre que
personne ne finit. Sous 5, le swipe ne démarre jamais.

```
1         COUVERTURE  l'accroche. 6 mots maximum, à une taille lisible dans la
                      grille en vignette. Une ligne de promesse en dessous.
2         L'ENJEU     pourquoi ça compte, en une phrase. Cette slide est aussi
                      une deuxième couverture, elle ne peut donc pas être de la
                      mise en place.
3 à N     UNE IDÉE PAR SLIDE. Un titre de 3 à 7 mots, 25 mots au plus en
                      dessous. Si une slide demande un paragraphe, ce sont
                      deux slides.
N+1       RÉCAP       le tout sous forme de liste. C'est la slide de la
                      capture d'écran.
DERNIÈRE  APPEL       une seule action. Enregistrer, commenter un mot-clé, ou
                      s'abonner. Une.
```

## Règles pour le texte des slides

- **La couverture fait 80 % du résultat.** Six mots. En gros. Rien dans le reste
  du carrousel ne sauve une couverture que personne ne fait défiler.
- **Concevez pour le recadrage de la grille.** La grille du profil recadre en un
  rectangle portrait, plus haut que large, et le rapport exact a changé plus
  d'une fois. Construisez en 1080x1350 et gardez le texte de la couverture bien
  au centre, à l'écart des 120 pixels extérieurs de chaque côté : le recadrage
  cesse alors de compter.
- **Numérotez les slides** (3/8). Les gens vont plus souvent au bout quand ils
  voient la fin.
- **Aucune slide n'est un paragraphe.** Si ça ne se dit pas en 25 mots,
  coupez en deux.
- **La slide récap est celle qu'on capture et qu'on envoie.** Les partages sont
  le signal le plus fort que vous puissiez obtenir. Rendez-la autonome et
  lisible sans contexte.
- **Le nom du compte sur chaque slide**, en petit, dans un coin du bas. Les
  captures d'écran voyagent sans vous.
- **Du texte alternatif au moins sur la couverture.** Il est lu par les lecteurs
  d'écran et par Instagram.
- **Le message sanitaire sur chaque slide où la bière apparaît**, à l'écart des
  120 pixels extérieurs pour qu'il survive au recadrage.

## Construire les fichiers

Instagram veut du 1080x1350 (4:5), en JPEG ou PNG, jusqu'à 20 éléments.
Construisez en HTML et imprimez chaque slide :

```bash
# une <section> par slide, 1080x1350, page-break-after: always
# puis Chrome headless --print-to-pdf, ou tout outil HTML vers image déjà utilisé
```

Écrivez le HTML avec `width:1080px; height:1350px`, une seule couleur d'accent,
et un corps de texte jamais inférieur à 32px, parce que tout cela se lit sur un
téléphone au tiers de sa taille réelle. Si le projet a un skill de marque ou un
design system, utilisez-le et n'inventez pas de palette.

## Sortie

D'abord le texte slide par slide, en liste numérotée que l'utilisateur peut lire
en dix secondes et modifier avant que quoi que ce soit ne soit généré. Puis la
**légende**, qui pour un carrousel est le Travail B de `/ig-caption` : la
légende travaille ici, parce que la couverture a déjà utilisé ses six mots.

Passez les deux dans `/ig-human`. Ne construisez les fichiers qu'après
validation du texte par l'utilisateur.

Exemple fictif :

```
CARROUSEL  ·  8 slides

1  COUVERTURE  4 HOUBLONS, 1 SEULE IPA
               Ce qu'on met dans la cuve, dans l'ordre.
2  ENJEU       Le même houblon donne deux bières selon le moment où on l'ajoute.
3              À L'ÉBULLITION
               L'amertume. 60 minutes, pas une de moins.
...
7  RÉCAP       Les quatre ajouts, dans l'ordre.
8  APPEL       Commentez HOUBLON et je vous envoie la fiche de brassage.

Mention sur les slides 1, 3 à 8 : « L'abus d'alcool est dangereux pour la santé. »
Légende : Travail B, accroche en ligne 1, un seul appel, 3 hashtags.
loi Évin :  message sanitaire présent (slides + légende) · 0 élément À FAIRE VALIDER
```

Rien n'est mis en ligne. L'utilisateur publie le carrousel.
