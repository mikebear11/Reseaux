---
name: ig-repurpose
description: >-
  Transformer un contenu long (vidéo YouTube, podcast, live, newsletter,
  article de blog ou appel client) en une semaine de Reels et de carrousels.
  À utiliser quand l'utilisateur dit « recycle ce contenu », « transforme ça
  en reels », « j'ai une vidéo / un podcast / une transcription », « découpe
  ça », « tire-moi des posts de cet article », ou colle quelque chose de long
  et veut le mettre sur Instagram.
---

# ig-repurpose

Un bon contenu long contient quatre à six posts. La plupart des gens en
tirent un et jettent le reste.

## Langue et ton

- Rédigez en français : extraits, plan de la semaine, brouillons. Si la source
  est dans une autre langue, traduisez les extraits et signalez-le.
- Respectez le tutoiement ou le vouvoiement indiqué dans `voice.md`. S'il n'y
  est pas, demandez une fois ; sans réponse, vouvoiement par défaut.
- Typographie française correcte : « guillemets », espace avant ; : ! ?
  acceptable. Pas de tiret cadratin.

## Loi Évin

Lisez d'abord `../ig-caption/loi-evin.md`. Pour une semaine tirée d'une source :

- Chaque post qui montre ou nomme une bière porte le message sanitaire
  « L'abus d'alcool est dangereux pour la santé » (sur le visuel et dans la
  légende).
- Privilégiez les extraits que L3323-4 autorise : degré, origine,
  ingrédients, brassage, arômes, médailles, où acheter.
- Un extrait qui sort de cette liste (une anecdote de fête, une dégustation
  entre amis, de l'humour sur la boisson) est signalé « À FAIRE VALIDER (Loi
  Évin) » dans le plan de la semaine. Pas de mineur à l'image, pas de
  parrainage, collaboration payée avec un créateur à faire valider.
- Une séquence tirée de la source n'est pas « conforme » parce qu'elle a déjà
  été diffusée ailleurs. Ne dites jamais qu'un post « respecte la Loi Évin ».

## Entrée

Une transcription, un article, une newsletter, un script, un compte rendu
d'appel, un live. Si l'utilisateur donne une URL et que cette session dispose
d'un outil de transcription, utilisez-le ; sinon demandez-lui de coller le
texte. Lisez tout avant d'extraire quoi que ce soit.

Si la source est une vidéo qui appartient à l'utilisateur, demandez aussi le
fichier. Un Reel construit sur ses propres images bat un Reel construit sur
ses propres mots relus.

## Extraire, pas résumer

Le résumé d'une vidéo n'est pas un Reel. Personne ne veut le résumé.
Parcourez la source et sortez ce qui tient debout tout seul :

| extrait | ce que c'est |
| --- | --- |
| **Affirmations** | chaque phrase qui lancerait un débat |
| **Chiffres** | chaque nombre, coût, durée, pourcentage |
| **Histoires** | chaque moment avec une personne, une scène et un coût |
| **Mécanismes** | chaque « en fait, ça marche comme ça… » |
| **Erreurs** | chaque aveu de quelque chose qui a mal tourné |
| **Phrases** | chaque phrase déjà citable telle quelle |

Listez ce que vous avez trouvé, avec les effectifs, avant d'écrire quoi que ce
soit. Si la source donne moins de quatre éléments, elle est maigre, et quatre
posts tirés d'elle seront maigres aussi. Dites-le.

## Puis choisir le format de chaque extrait

Tout n'est pas un Reel.

- **Affirmation, erreur, histoire** : un Reel. Il leur faut une voix et un
  visage.
- **Mécanisme, liste numérotée** : un carrousel. Il faut pouvoir les relire.
- **Une phrase citable** : une image de story, pas un post.

## Puis construire la semaine

Chaque extrait devient un post, et chaque post tient entièrement seul. La
personne n'a pas vu la source et ne la verra jamais. N'écrivez jamais « comme
je le disais dans ma dernière vidéo ». Le post est la chose.

Attribuez à chacun une formule d'accroche de `ig-reel/hooks.json` (citez-la
par son nom français, par exemple « #2 L'ordre négatif ») et variez-les. Cinq
posts tirés d'une même source avec la même forme d'accroche, ça se lit comme
une usine à contenu, parce que c'en est une.

Si la source est la vidéo de l'utilisateur, **utilisez les vraies images**. Le
passage où il a dit la chose, avec la vraie réaction dedans, bat un nouveau
tournage à chaque fois. Coupez sur la phrase, pas sur la respiration.

Ordonnez la semaine pour que l'affirmation la plus forte passe en premier,
que l'histoire tombe en milieu de semaine, et que le mécanisme passe en
dernier, quand ceux qui ont aimé les précédents l'attendent.

## Sortie (exemple fictif)

```
SOURCE : « Pourquoi on a arrêté de filtrer nos bières » (podcast de 42 min, 8 900 mots)

TROUVÉ  5 affirmations, 9 chiffres, 3 histoires, 4 mécanismes, 2 erreurs, 7 phrases citables

SEMAINE
MAR  REEL       #2  L'ordre négatif        Arrêtez de croire qu'une bière trouble est ratée
                                           prendre l'extrait à 14:20, il rit à la fin
MER  CARROUSEL  légende Travail B          Les 4 étapes de notre garde à froid
VEN  REEL       #21 Le début en pleine phrase  « …et le filtre nous coûtait 1 200 € par an »
DIM  REEL       #5  Le temps écrasé        Trois jours de garde gagnés, une étape supprimée

loi Évin :  message sanitaire prévu sur les 4 posts · 0 élément À FAIRE VALIDER

Dites « écris mardi » et je le rédige.
```

Puis rédigez à la demande, un à la fois, chacun via `/ig-reel` et
`/ig-human`. Ne déversez pas quatre scripts finis d'un coup. Ils sonneront
tous pareil et l'utilisateur n'en tournera aucun.

Rien n'est publié par ce skill : il prépare, l'utilisateur publie.
