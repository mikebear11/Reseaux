---
name: ig-reel
description: >-
  Écrire un Reel Instagram à partir d'une idée brute : des accroches tirées de
  26 formules, le script parlé, le texte à l'écran et un minutage chronométré,
  dans la voix de l'utilisateur et notés avant le tournage. À utiliser dès que
  l'utilisateur veut un Reel, un script de vidéo courte, une accroche, une voix
  off, dit « fais-moi un reel sur… », « écris-moi un reel », « qu'est-ce que je
  dis dans cette vidéo », « trouve-moi une accroche », ou s'apprête à tourner
  sans avoir sa première phrase.
---

# ig-reel

Transforme une idée brute en un Reel que quelqu'un regarde jusqu'au bout.

Deux outils vivent dans ce dossier et ils fonctionnent vraiment. Utilisez-les.
Ne jugez pas l'accroche à l'œil et ne devinez pas la durée.

```bash
python3 hookscore.py hooks.txt              # classer vos accroches
python3 hookscore.py --hook "une seule ligne"   # noter une seule accroche
python3 beats.py script.txt --target 30     # minutage chronométré avant le tournage
```

Les deux scripts acceptent `--lang auto|fr|en` (par défaut `auto` : la langue
du texte est détectée). En français, ils utilisent des listes de mots
françaises (enjeux, ouvertures faibles, impératifs, nombres dits à l'oral, €).
Attention : les seuils (accroche de 5 à 12 mots, 3 s, 165 mots/min) viennent de
l'auteur d'origine et n'ont pas été recalibrés pour le français. Chronométrez-
vous en lisant un script à voix haute, puis passez votre vrai débit à
`beats.py` avec `--wpm`.

## Langue et ton

- Rédigez en français : accroches, script, texte à l'écran, récapitulatif.
- Respectez le tutoiement ou le vouvoiement indiqué dans `voice.md`. S'il n'y
  est pas, demandez une fois ; sans réponse, vouvoiement par défaut.
- Typographie française correcte : « guillemets », espace avant ; : ! ?
  acceptable, apostrophe ’ ou '. Pas de tiret cadratin.

## Loi Évin

Lisez d'abord `../ig-caption/loi-evin.md`. Pour un Reel :

- Tout Reel qui montre ou nomme une bière porte le message sanitaire
  « L'abus d'alcool est dangereux pour la santé » : sur une carte à l'écran ET
  dans la légende (`/ig-caption`).
- Construisez l'accroche et le script d'abord sur ce que L3323-4 autorise :
  degré, origine, ingrédients, brassage, arômes, couleur, médailles, où acheter.
- Tout le reste (ambiance de fête, gens qui trinquent, humour, séduction,
  sport, réussite sociale) est signalé « À FAIRE VALIDER (Loi Évin) » dans le
  récapitulatif.
- Aucun mineur à l'image avec le produit. Pas de parrainage. Une collaboration
  avec un créateur payé (en argent ou en produits) est à faire valider.
- Ne dites jamais qu'un Reel « respecte la Loi Évin ». Dites ce qui a été
  vérifié et ce qui ne l'a pas été.

## Avant d'écrire

1. Lisez `~/.claude/instagram/voice.md` s'il existe. C'est le profil de voix de
   l'utilisateur : comment il parle face caméra, ce qu'il ne dit jamais, à qui
   il s'adresse. S'il n'existe pas, demandez **trois de ses propres Reels**,
   transcrivez-les ou lisez-les, déduisez la voix et écrivez le fichier. Un
   script dans la mauvaise voix est inutilisable, parce qu'il faut le dire à
   voix haute.
2. Lisez `hooks.json` dans ce dossier. 26 formules, chacune avec un modèle, un
   exemple rempli, la version à l'écran, son usage et la façon dont on la gâche.
   Les champs `name_fr`, `template_fr`, `example_fr`, `on_screen_fr` et
   `match_fr` en donnent la version française (les exemples `_fr` sont
   fictifs). Quatre de ces formules y sont parce qu'elles revenaient sans cesse
   dans de vraies accroches, pas pour compléter une série.
3. Si l'idée est maigre, ne la gonflez pas. Posez une seule question groupée :
   que s'est-il passé, à qui, et qu'est-ce que ça a coûté ou rapporté. Un Reel
   a besoin d'une chose précise et vraie. Obtenez-la avant d'écrire.
4. Si `~/.claude/instagram/swipe.md` existe, lisez-le. `/ig-viral` écrit ce
   fichier, et c'est la preuve propre à l'utilisateur des formules qui marchent
   dans sa niche en ce moment. Il l'emporte sur les valeurs par défaut de ce
   fichier.

## La structure

Un Reel se joue dans les deux premières secondes et se garde dans les cinq
suivantes.

```
0:00 - 0:02   ACCROCHE    l'affirmation. Phrase parlée et phrase à l'écran,
                          écrites séparément. Du mouvement dès la première
                          image, pas un visage figé.
0:02 - 0:07   L'ENJEU     pourquoi ça compte pour la personne qui regarde.
                          Une phrase.
0:07 - ...    LE CORPS    une idée par temps, et le plan change à chaque temps.
3 DERNIÈRES s LA CHUTE    livrer ce que l'accroche promettait, puis la demande
                          unique.
DERNIÈRE      LA BOUCLE   reprendre un mot de l'accroche pour que le
PHRASE                    revisionnage s'enchaîne proprement.
```

Durée : de 15 à 45 secondes, c'est la plage utile. Les Reels vont jusqu'à
3 minutes et presque personne ne devrait s'en servir. Sous 7 secondes, les
comptages de boucles gonflent, et rien d'autre.

## La boucle de travail

**1. Choisissez trois accroches, pas une.** Passez l'idée dans `hooks.json`,
choisissez trois formules qui lui vont vraiment, et écrivez pour chacune la
phrase parlée et la phrase à l'écran. Trois formules différentes, pas trois
réécritures de la même.

**2. Notez-les.** Mettez les trois phrases parlées dans un fichier, une par
ligne, et lancez `hookscore.py`. Montrez le classement à l'utilisateur. Si la
meilleure est sous 50, vous n'avez pas encore l'accroche, et aucune retouche ne
réglera ça.

**3. Écrivez le script** sur l'accroche gagnante. Une langue parlée simple, la
façon dont l'utilisateur parle vraiment. Les tournures orales qu'il utilise
(« y a », « on a »). Des phrases courtes. Aucune phrase qu'il devrait répéter
avant de la dire.

**4. Chronométrez.** Lancez `beats.py script.txt --target {durée}` (avec
`--wpm` si l'utilisateur connaît son débit). Corrigez chaque alerte : une
accroche au-delà de 3 secondes, un temps de plus de 4 secondes, une suite de
temps sans rien de concret, pas de boucle. Relancez jusqu'à ce que ce soit
propre.

**5. Humanisez.** Passez le script dans `/ig-human` avant de le montrer. Une
phrase qui sonne écrit se remarque dès qu'on la dit à voix haute.

**6. Affichez le bloc.** Le script dans un bloc de code, le texte à l'écran
dans une liste séparée avec les minutages, puis :

```
REEL PRÊT
accroche :   #1 L'aveu du coût, note 78 STRONG
durée :      27,9 s sur 9 temps à 165 mots/min (non calibré pour le français)
à l'écran :  6 cartes, dont le message sanitaire
humaniseur : 3 artefacts retirés, score humain 80 PASS
loi Évin :   message sanitaire présent · 1 élément À FAIRE VALIDER (plan de dégustation au comptoir)
légende :    lancez /ig-caption ensuite

Répondez « oui » pour l'enregistrer dans le journal, ou dites-moi ce qu'il faut changer.
```

**7. Ne publiez jamais.** Ce skill produit un script. L'utilisateur le tourne
et le publie. Sur « oui », ajoutez à `~/.claude/instagram/log.md` la date, la
formule d'accroche utilisée et la première phrase, pour que `/ig-audit` ait un
historique plus tard.

## Le texte à l'écran est un script à part

Écrivez-le séparément, à chaque fois. Il est lu avant d'être entendu.

- **Six mots maximum par carte.** Il est lu à bout de bras par quelqu'un qui
  n'écoute pas encore.
- **La carte d'accroche est là dès la première image**, pas après un temps de
  silence.
- **Restez dans la zone de sécurité.** Sur une image de 1080x1920, rien
  au-dessus de y=230 ni en dessous de y=1440, et laissez libres les 230 pixels
  de droite. L'interface recouvre tout ce qui sort de ce cadre : la légende, la
  colonne d'actions, la bande audio.
- **Ne mettez jamais l'accroche là où se trouve la légende.** C'est le bas de
  l'image, et il est recouvert.
- **Incrustez les sous-titres pour le corps.** La plupart des gens regardent
  d'abord sans le son.
- **Le message sanitaire** est une carte lisible, dans la zone de sécurité,
  dès que la bière est montrée ou nommée.

## Les règles qui font la différence

- **Une idée par Reel.** Si le script en contient deux, vous avez deux Reels.
  Dites-le.
- **Des chiffres plutôt que des adjectifs.** « 1 200 € » bat « beaucoup ».
  « 14 jours de garde » bat « longtemps ». Si l'utilisateur n'a pas donné de
  chiffre, demandez-en un plutôt que d'écrire autour du trou.
- **Coupez l'intro.** Pas de bonjour, pas de « dans cette vidéo », pas de nom,
  pas de jingle de logo. La vidéo commence à la phrase que vous auriez
  normalement atteinte à la sixième seconde.
- **Changez de plan à chaque temps.** Un plan fixe de 8 secondes, c'est là que
  les gens partent, et `beats.py` le signalera.
- **Une seule demande à la fin.** Commenter un mot-clé, enregistrer, ou
  s'abonner. Une.
- **N'inventez jamais.** Aucune métrique, aucun client, aucun chiffre
  d'affaires, aucune médaille ni aucun résultat inventé au nom de
  l'utilisateur, même comme bouche-trou. Si un chiffre est nécessaire et
  inconnu, laissez `{{votre chiffre}}` dans le script et signalez-le.
- **N'écrivez pas un script autour d'un son tendance que l'utilisateur ne peut
  pas utiliser.** Si l'idée a besoin de sa propre voix, dites-le.

## Exemple (fictif)

```
/ig-reel avant, notre houblon frais mettait six semaines à arriver en cuve, maintenant 48 heures
```

```
ACCROCHES  (notées par hookscore.py)
  78  STRONG  #1  L'aveu du coût   « On a jeté 400 litres avant de comprendre ça. »
                                   à l'écran : 400 L JETÉS
  49  WEAK    #5  Le temps écrasé  « Six semaines entre la récolte et la cuve. Quarante-huit heures maintenant. »
                                   à l'écran : 6 SEMAINES → 48 H
  37  WEAK    #9  À voler          « Volez notre calendrier de récolte. »
                                   à l'écran : À VOLER

On tourne la #1 : un chiffre, un coût, et c'est le vôtre. La #5 a les chiffres
mais rien en jeu (STAKES 20) : ajoutez ce que les six semaines coûtaient avant
de la retenter. Les deux parlent du brassage et de l'origine du houblon, ce que
L3323-4 autorise. Ajoutez la carte « L'abus d'alcool est dangereux pour la
santé » dès que la bouteille apparaît.
```
