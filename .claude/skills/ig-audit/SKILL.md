---
name: ig-audit
description: >-
  Faire le bilan de ce que l'utilisateur a déjà publié : quels Reels ont
  vraiment marché, pourquoi, et quoi arrêter de faire. À utiliser quand
  l'utilisateur colle ses statistiques Instagram ou ses anciens posts et
  demande « qu'est-ce qui marche », « pourquoi celui-ci a fait un flop »,
  « lis mes statistiques », « audite mon contenu », ou veut savoir quoi faire
  davantage.
---

# ig-audit

La seule source honnête de ce qui marche pour un compte, c'est ce compte.
Chaque règle de chaque guide Instagram, y compris celles de ce pack, est une
hypothèse de départ. Les 30 derniers posts de l'utilisateur sont la preuve.

## Langue et ton

- Rédigez en français : tableaux, constats, recommandations. Nombres au format
  français (« 4 100 », « 18,2x », « 62 % »).
- Respectez le tutoiement ou le vouvoiement indiqué dans `voice.md`. S'il n'y
  est pas, demandez une fois ; sans réponse, vouvoiement par défaut.
- Typographie française correcte : « guillemets », espace avant ; : ! ?
  acceptable. Pas de tiret cadratin.

## Entrée

Demandez ce que l'utilisateur a sous la main :

- Les statistiques par post : vues, portée, interactions, durée de
  visionnage, enregistrements, partages, nouveaux abonnés, et la part de
  portée hors abonnés. Des captures d'écran conviennent.
- Ou la courbe de rétention de ses meilleurs et de ses pires Reels récents.
  Cette seule capture vaut plus que tout le reste réuni.
- Ou simplement les posts et leurs nombres de vues, ce qui suffit pour un
  premier passage.

Lisez aussi `~/.claude/instagram/log.md` s'il existe, puisqu'il note la
formule d'accroche utilisée pour chaque post.

## Ce qu'il faut vraiment mesurer

Les vues brutes sont le chiffre le moins utile de la page, parce qu'elles
dépendent surtout du nombre de personnes qui suivent déjà le compte. Calculez
plutôt ceci et montrez le calcul :

| métrique | calcul | ce qu'elle dit |
| --- | --- | --- |
| **Multiple de surperformance** | vues / médiane des vues du compte | s'il s'agit d'un vrai succès ou d'une journée normale |
| **Portée hors abonnés** | % de la portée venant de non-abonnés | si le post a voyagé, ou pas du tout |
| **Rétention à 3 s** | spectateurs encore là à 3 s / spectateurs ayant commencé | si l'accroche a marché. C'est la note de l'accroche. |
| **Durée moyenne de visionnage** | directement dans les statistiques | si le milieu a marché |
| **Partages par portée** | partages / portée | le signal le plus fort qu'on puisse obtenir. Un partage, c'est quelqu'un qui engage son nom. |
| **Nouveaux abonnés par portée** | nouveaux abonnés / portée | si le profil a converti l'attention |

Classez par multiple de surperformance et par partages par portée, pas par
vues. Un Reel à 4 000 vues et 90 partages a battu celui à 60 000 vues et 11
partages.

## Puis trouver le schéma

Avec les cinq meilleurs et les cinq pires côte à côte, cherchez ce qui les
sépare, et acceptez de conclure quelque chose qui ne plaira pas à
l'utilisateur :

- **Rétention à 3 secondes.** Si le haut et le bas diffèrent là-dessus, c'est
  l'accroche et rien d'autre, et tout ce qui vient après est une diversion.
- **Formule d'accroche.** Quels identifiants de `ig-reel/hooks.json` sont dans
  le top 5 ? Citez-les par leur nom français (« #3 Personne ne vous dit »).
- **Format.** Reel, carrousel, image seule.
- **Durée.** Regroupez en moins de 15 s, 15 à 30 s, 30 à 60 s, plus de 60 s.
- **Thème.**
- **Si l'utilisateur a répondu aux commentaires dans la première heure.**
- **Jour et heure.** Vérifiez ça **en dernier**, et seulement si le reste ne
  montre rien. Ce n'est presque jamais la cause, et c'est là que les gens
  voudraient qu'elle soit.

Formulez le constat comme une affirmation avec la preuve jointe, et dites quel
degré de confiance il mérite. Avec 30 posts, on peut voir un schéma. Avec 6,
non, et le dire vaut mieux que d'en inventer un.

## La distinction qui fait gagner des mois

**Un Reel qui fait des vues et aucun nouvel abonné n'est pas un Reel raté,
c'est un problème de profil.** Un Reel qui ne fait pas de vues est un problème
d'accroche. Séparez les deux avant de recommander quoi que ce soit. Si la
portée hors abonnés est élevée et les nouveaux abonnés par portée faibles,
arrêtez de réécrire les accroches et passez à `/ig-profile`.

## Sortie (exemple fictif)

```
AUDIT  ·  31 posts  ·  du 12 juin au 5 sept.  ·  médiane des vues 4 100

TOP 5 PAR MULTIPLE DE SURPERFORMANCE
  18,2x  #3  Personne ne vous dit   74 600 vues  62 % hors abonnés  rétention à 3 s 71 %  128 partages
   6,4x  #1  L'aveu du coût         26 300 vues  48 % hors abonnés  rétention à 3 s 64 %   71 partages
  ...

LES 5 DERNIERS
   0,3x  #11 La liste avec un favori  1 200 vues   9 % hors abonnés  rétention à 3 s 31 %    2 partages
  ...

CE QUE DISENT LES DONNÉES
1. La rétention à 3 secondes explique tout. Le top 5 est à 66 % en moyenne,
   les 5 derniers à 33 %. Tout ce qui vous inquiète d'autre dépend des deux
   premières secondes.
2. Les posts où c'est vous qui aviez l'air bête (le brassin raté, la cuve qui
   déborde) : 8,1x en moyenne contre 0,9x pour tout le reste. n=5. Le signal
   le plus fort ici, et de loin.
3. Les listes « 5 accords mets et bières » font des vues et rien d'autre.
   Beaucoup de portée, pas de partages, pas de nouveaux abonnés. Trois de vos
   5 derniers.
4. Le jour de la semaine ne montre rien. Vos moyennes du mardi et du vendredi
   sont dans le bruit. Arrêtez de l'optimiser.

STOP : les listes.
PLUS DE : ceux où il y a un coût que vous avez payé et un chiffre derrière.
```

Puis transmettez les conclusions à `/ig-plan`, pour que la semaine suivante
soit construite sur les preuves de l'utilisateur plutôt que sur des valeurs
par défaut, et à `/ig-viral`, pour que le fichier d'inspiration (swipe file)
soit filtré sur les formules qui marchent pour ce compte précisément.

Ce skill ne publie rien : il lit les statistiques, l'utilisateur publie.
