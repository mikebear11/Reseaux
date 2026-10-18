---
name: ig-plan
description: >-
  Construire la semaine sur Instagram : quoi publier, sous quel format, quand,
  et avec qui interagir. À utiliser quand l'utilisateur dit « planifie ma
  semaine », « qu'est-ce que je publie ? », « calendrier éditorial », « je n'ai
  rien à publier », ou veut un planning de publication et une liste
  d'engagement.
---

# ig-plan

La salle de contrôle. Tout le reste du pack exécute ; ce skill décide de ce qui
est exécuté. Lancez-le une fois par semaine, toujours le même jour.

## Langue et ton

- Rédigez en français, plan compris (jours, formats, angles).
- Respectez le tutoiement ou le vouvoiement indiqué dans
  `~/.claude/instagram/voice.md`. S'il n'y est pas, demandez une fois ; sans
  réponse, vouvoyez.
- Typographie française : « guillemets », espace avant ; : ! ? acceptée, heures
  au format 19h30. Pas de tiret cadratin.
- Citez les formules d'accroche par leur numéro et leur nom français
  (`name_fr` dans `ig-reel/hooks.json`), par exemple « #3 Personne ne vous
  dit ».

## Loi Évin

**Règle absolue de la brasserie.** Dès qu'un contenu parle d'alcool, ou que
sa photo ou sa vidéo s'y rapporte (bière, verre, bouteille, canette, fût,
tireuse, cuve, comptoir, dégustation, brassage…), il porte la phrase
**« L'abus d'alcool est dangereux pour la santé. »** Sans exception, même quand
le texte ne nomme aucune bière. Dans le doute, mettez-la. Elle s'ajoute en fin
de texte, ne compte pas comme appel à l'action, et `/ig-human` ne la retire
jamais. Si `voice.md` donne une formule plus longue (par exemple « …, à
consommer avec modération »), utilisez celle-là.

Lisez `../ig-caption/loi-evin.md` avant de planifier pour une brasserie.

- Chaque créneau qui parle d'alcool ou dont l'image s'y rapporte prévoit le message sanitaire
  « L'abus d'alcool est dangereux pour la santé » (légende et visuel).
- Choisissez d'abord des angles que L3323-4 autorise : brassage, ingrédients,
  origine, degré, arômes, médailles, où acheter, comment servir. Ce sont aussi
  les angles les plus concrets.
- Tout angle qui en sort (fête, trinquer, humour, réussite sociale) est marqué
  « À FAIRE VALIDER (Loi Évin) » dans le plan, sur la ligne du créneau.
- Pas de mineur à l'image, pas de parrainage, pas de compte manifestement
  destiné à la jeunesse dans la liste d'engagement. Toute collaboration
  d'influenceur payée est marquée à faire valider.
- Le plan ne dit jamais qu'une semaine « respecte la Loi Évin ».

## Entrée

Si `~/.claude/instagram/voice.md`, `swipe.md` et `log.md` existent, lisez-les.
Le fichier d'inspiration (swipe file) est la preuve propre à l'utilisateur, issue
de `/ig-viral`, des formules qui marchent dans son domaine en ce moment, et il
prime sur tout ce qui est écrit ici. Le journal empêche le plan de répéter un
thème des deux dernières semaines.

S'ils n'existent pas, demandez quatre choses et notez-les :

1. Ce que vend l'utilisateur, et à qui.
2. Les trois ou quatre thèmes pour lesquels il veut être connu.
3. Ce qui s'est réellement passé cette semaine : un appel client, un chiffre,
   une erreur, quelque chose qu'il a construit, une dispute. C'est de là que
   viennent les posts.
4. Dix comptes auprès desquels il vaut la peine d'être visible.

## Quoi publier

Quatre à cinq posts par semaine, dont au moins trois Reels. Les Reels sont le
seul format d'Instagram qui atteint de façon fiable des gens qui ne suivent pas
le compte. Les carrousels vont en profondeur avec ceux qui suivent déjà. Les
stories sont quotidiennes et se planifient à part.

Mélangez sur la semaine, jamais deux posts du même type à la suite :

| type | part | rôle |
| --- | --- | --- |
| **Preuve** | 1 par semaine | quelque chose qui s'est passé, avec un chiffre. Reel. |
| **Apprendre** | 1 à 2 par semaine | une chose que le spectateur peut faire aujourd'hui. Reel ou carrousel. |
| **Opinion** | 1 par semaine | une position qui pourrait vous faire perdre des abonnés. Reel. |
| **Récit** | 1 toutes les deux semaines | une scène qui a un coût. Reel. |
| **Offre** | 1 toutes les deux semaines | ce que vous vendez, dit simplement, sans excuse. Carrousel ou stories. |

Pour chaque créneau, donnez : le thème, l'angle précis tiré de ce qui s'est
réellement passé cette semaine, le format, et le numéro de formule d'accroche
de `ig-reel/hooks.json`. Pas un sujet, un angle. « La bière » n'est pas un plan.
« Le brassin qu'on a jeté parce que la fermentation est partie à 26 °C » est un
Reel.

## Quand publier

Publiez quand le public de l'utilisateur est réveillé et pas au travail. Pour
la plupart des publics grand public, c'est en début de soirée, heure locale ;
pour un public professionnel, tôt le matin.

Mais dites-le clairement : **l'heure compte bien moins que les deux premières
secondes.** Instagram continuera de montrer un Reel pendant des jours s'il
performe, et enterrera un Reel bien programmé qui ne performe pas. Si
l'utilisateur optimise ses heures de publication avant que ses accroches
fonctionnent, il polit la mauvaise chose, et vous devez le lui dire.

Calez les heures sur le fuseau du public, pas sur celui de l'utilisateur, s'ils
diffèrent.

## La tournée d'engagement, qui n'est pas optionnelle

20 minutes par jour, avant de publier, pas après. Construisez une liste de 10 :

- **5 portée** : des comptes dont l'audience intéresse l'utilisateur, où un bon
  commentaire se voit. Commentez tôt, avant que le fil ait 200 réponses.
- **3 pairs** : même taille, même domaine. C'est le groupe qui rend la pareille.
- **2 acheteurs** : des gens qui pourraient réellement acheter (pour une
  brasserie : cavistes, bars, restaurateurs, épiceries fines). Commentez
  pendant des semaines avant tout DM, et ne vendez jamais dans un commentaire.

Passez la liste à `/ig-comment`.

## Sortie

Exemple fictif :

```
SEMAINE DU 15 SEPTEMBRE

LUN  engagement seul  (20 min, liste ci-dessous)
MAR  19h30  REEL       PREUVE     #5  Le temps écrasé          - 6 semaines de garde en 30 secondes
MER  stories seules + engagement
JEU  19h00  CARROUSEL  APPRENDRE  légende Travail B            - les 4 ajouts de houblon, slide par slide
VEN  19h30  REEL       OPINION    #2  L'ordre négatif          - arrêtez de servir une IPA glacée
SAM  -
DIM  18h00  REEL       RÉCIT      #21 Le début en pleine phrase - le brassin jeté à 26 °C

STORIES  tous les jours, 3 à 5 stories, boîte à questions le jeudi.

ENGAGEMENT  (5 portée / 3 pairs / 2 acheteurs)
  ...

loi Évin :  message sanitaire prévu sur les 4 posts · 1 élément À FAIRE VALIDER (VEN : ton d'opinion)

Dites « écris mardi » et je le rédige.
```

Écrivez le plan dans `~/.claude/instagram/plan.md` pour que les autres skills
puissent le lire. Rien n'est programmé ni publié nulle part. C'est un plan, et
c'est l'utilisateur qui le met en œuvre.
