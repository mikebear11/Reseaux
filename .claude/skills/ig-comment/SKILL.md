---
name: ig-comment
description: >-
  Écrire des commentaires sous les posts et Reels des autres qui se lisent
  comme ceux d'une personne qui a un avis, pas d'un robot. À utiliser quand
  l'utilisateur colle un post ou un Reel et veut un commentaire, dit
  « commente ça », « réagis à ce post », « qu'est-ce que je mets là ? », ou
  veut une série pour sa tournée d'engagement quotidienne.
---

# ig-comment

Commenter, ce sont les vingt minutes les plus rentables sur Instagram, et les
plus faciles à mal faire. Un commentaire en haut d'un Reel à 40 000 vues est vu
par plus de monde que la plupart des posts des comptes eux-mêmes, et c'est le
seul endroit où un inconnu peut taper directement jusqu'à un profil.

Un commentaire générique est pire que rien. Il coûte un tap qui ne mène nulle
part et il range le compte parmi les comptes de « pods » d'engagement aux yeux
de la seule personne dont l'avis comptait : le créateur.

## Langue et ton

- Rédigez en français.
- Respectez le tutoiement ou le vouvoiement indiqué dans
  `~/.claude/instagram/voice.md`. S'il n'est pas indiqué, demandez une fois ;
  sans réponse, vouvoiement par défaut. Sous le post d'un autre, alignez-vous
  aussi sur le registre du créateur et de ses commentaires.
- Typographie française correcte : « guillemets », espace avant ; : ! ?
  acceptable. Pas de tiret cadratin.

## Loi Évin

Lisez d'abord `../ig-caption/loi-evin.md`. Pour un commentaire :

- Pas de pitch (voir les règles), donc en principe pas de bière de la brasserie
  nommée. Si un commentaire montre ou nomme une bière, il porte le message
  sanitaire « L'abus d'alcool est dangereux pour la santé ».
- Quand on parle de bière, rester sur ce que L3323-4 autorise : degré, origine,
  ingrédients, brassage, arômes, médailles, où acheter. Tout le reste (fête,
  trinquer, incitation à boire, humour sur l'alcool) est signalé « À FAIRE
  VALIDER (Loi Évin) ».
- Ne jamais commenter avec du contenu alcool sous un compte qui vise les moins
  de 18 ans. Pas de parrainage. Une collaboration d'influenceur payée se fait
  valider avant.
- Ne jamais écrire qu'un commentaire « respecte la Loi Évin » : dire ce qui a
  été vérifié.

## Entrée

L'utilisateur colle le texte du post ou du Reel, ou une capture d'écran, avec
le nom du compte. S'il donne une URL que vous ne pouvez pas ouvrir, demandez-lui
de coller le contenu. N'utilisez pas d'outil de navigation pour aspirer le fil
et ne publiez rien.

## Les neuf types de commentaires

Choisissez selon ce qu'est vraiment le post. Ne prenez jamais le type 1 par
défaut.

| # | type | quand | forme |
| --- | --- | --- | --- |
| 1 | **Ajouter une donnée** | le post affirme quelque chose qu'un chiffre peut appuyer | « Pareil chez nous : 40 % de... » |
| 2 | **Ajouter le cas manquant** | le post a raison mais il est incomplet | « C'est vrai jusqu'à ce que {condition}. » |
| 3 | **Désaccord respectueux** | vous pensez sincèrement que c'est faux | nommez d'abord le point d'accord, puis la bifurcation |
| 4 | **Prolonger une phrase** | une phrase du post est la bonne | citez-la, construisez dessus |
| 5 | **Poser la vraie question** | le post a sauté la partie difficile | une question, précise |
| 6 | **Le vécu** | vous avez fait ce qu'ils décrivent | ce qui s'est passé, en deux phrases |
| 7 | **La correction** | il y a une erreur factuelle | ayez raison, soyez bref, gentil et sûr de vous |
| 8 | **Le recadrage** | bons faits, mauvais cadre | « Une autre façon de le lire : » |
| 9 | **La phrase courte** | le post n'a besoin de rien, vous voulez être présent | moins de 10 mots, drôle ou vrai |

## Règles

- **Une à trois phrases.** Les commentaires Instagram se lisent dans une
  colonne étroite sous une vidéo. Un paragraphe se replie derrière « plus » et
  personne ne tape dessus.
- **N'ouvrez jamais par** « Super post », « J'adore », « Tellement vrai »,
  « Ça 👏 », « J'avais besoin de lire ça aujourd'hui », ou le prénom du créateur
  suivi d'un point d'exclamation. Tout ça est invisible.
- **Pas de commentaire fait uniquement d'émojis**, et pas d'émoji en premier
  caractère.
- **Ne résumez jamais le Reel.** Tous ceux qui le regardent viennent de le voir.
- **Une seule idée.** Un commentaire avec deux points se lit comme une prise
  d'otage.
- **Dites la chose précise.** Si le commentaire pouvait aller sous n'importe
  quel post sur le sujet, ce n'est pas un commentaire, c'est du bruit.
- **Jamais de pitch.** Ni l'offre, ni le lien, ni « passe voir ma page ». C'est
  le moyen le plus rapide de se faire bloquer par exactement la personne qu'on
  voulait atteindre.
- **La rapidité compte plus ici que n'importe où.** Un commentaire posté dans
  la première heure sous un Reel qui décolle ensuite voyage avec lui.

## Sortie

Donnez **deux options de types différents**, étiquetées, plus une ligne sur
celle que vous posteriez et pourquoi. Passez les deux dans `/ig-human` d'abord :
les commentaires sont courts, donc un tiret cadratin ou une formule toute faite
s'entend proportionnellement plus fort que dans une légende.

Exemple fictif :

```
OPTIONS DE COMMENTAIRE  (sous le Reel de @compte sur les prix de vente)

[6 · Vécu]
On a augmenté nos tarifs pro de 15 % en mars et on a perdu un seul
revendeur, celui qui nous prenait la moitié des appels. Il nous a fallu
huit mois pour ne plus en avoir peur.

[3 · Désaccord respectueux]
D'accord sur l'ancrage. Là où je ne te suis pas, c'est le faire en pleine
saison. On a essayé et ça nous a coûté une cave qui était partie pour
renouveler.

Poste le premier. Il concède quelque chose et il contient un chiffre.

loi Évin:  aucune bière nommée · 0 élément À FAIRE VALIDER
```

## Mode série

Pour une tournée d'engagement, demandez les 5 à 10 posts en texte collé dans un
seul message, rendez un commentaire par post dans un seul bloc, et tenez à jour
dans `~/.claude/instagram/log.md` la liste des comptes commentés cette semaine.
Commenter les trois mêmes comptes tous les jours, ça se voit, et ça ressemble
exactement à ce que c'est.

## Jamais

Ne postez rien automatiquement, n'automatisez pas les commentaires et
n'utilisez pas d'outil de navigation pour publier à la place de l'utilisateur.
L'engagement automatisé enfreint les conditions d'utilisation d'Instagram et
fait bloquer les actions du compte. Ce skill écrit le commentaire.
L'utilisateur le poste.
