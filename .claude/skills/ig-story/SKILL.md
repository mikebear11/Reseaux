---
name: ig-story
description: >-
  Écrire les stories Instagram du jour : la séquence image par image, quel
  sticker mettre où, et celui qui fait passer les gens en DM (message privé).
  À utiliser quand l'utilisateur dit « stories », « qu'est-ce que je mets en
  story », « une séquence de stories », « une idée de sondage », « je n'ai rien
  à mettre en story », ou veut vendre quelque chose sans en faire un post.
---

# ig-story

Les stories ne sont pas un fil en plus petit. Le fil, c'est la façon dont des
inconnus vous trouvent. Les stories, c'est la façon dont ceux qui vous suivent
déjà décident si vous êtes quelqu'un à qui acheter, et c'est la seule surface
d'Instagram où un tap devient une conversation en un geste.

Personne en dehors de vos abonnés ne les voit, donc le travail est complètement
différent : de la profondeur, pas de la portée.

## Langue et ton

- Rédigez en français.
- Respectez le tutoiement ou le vouvoiement indiqué dans
  `~/.claude/instagram/voice.md`. S'il n'y est pas, demandez une fois ; sans
  réponse, vouvoyez. (Les stories parlent à une seule personne : « tu » ou
  « vous », mais toujours au singulier dans l'intention.)
- Typographie française : « guillemets », espace avant ; : ! ? acceptée. Pas de
  tiret cadratin.

## Loi Évin

**Règle absolue de la brasserie.** Dès qu'un contenu parle d'alcool, ou que
sa photo ou sa vidéo s'y rapporte (bière, verre, bouteille, canette, fût,
tireuse, cuve, comptoir, dégustation, brassage…), il porte la phrase
**« L'abus d'alcool est dangereux pour la santé. »** Sans exception, même quand
le texte ne nomme aucune bière. Dans le doute, mettez-la. Elle s'ajoute en fin
de texte, ne compte pas comme appel à l'action, et `/ig-human` ne la retire
jamais. Si `voice.md` donne une formule plus longue (par exemple « …, à
consommer avec modération »), utilisez celle-là.

Lisez `../ig-caption/loi-evin.md` avant toute séquence de brasserie.

- Toute story qui parle d'alcool ou dont l'image s'y rapporte porte le message sanitaire
  « L'abus d'alcool est dangereux pour la santé », dans la zone de texte sûre.
- Les sondages, quiz et curseurs n'incitent pas à boire (pas de « combien vous
  en buvez ce soir ? »). Faites voter sur ce que L3323-4 autorise : un houblon,
  un arôme, une couleur, un nom de bière, un point de vente.
- Montrez d'abord le brassage, les ingrédients, l'origine, les médailles, où
  acheter. Tout le reste (fête, trinquer, humour) est signalé « À FAIRE VALIDER
  (Loi Évin) » dans le récapitulatif.
- Pas de mineur à l'image avec le produit, pas de parrainage, et un « Ajoutez
  le vôtre » sur de l'alcool se fait valider : vous ne choisissez pas qui
  répond. Collaboration d'influenceur payée : à faire valider.
- Ne dites jamais qu'une séquence « respecte la Loi Évin ».

## La forme quotidienne

Trois à sept stories par jour. Au-delà d'environ sept, le taux de tap vers
l'avant grimpe et les dernières passent devant personne, et c'est exactement là
que les gens mettent leur demande.

```
1       L'OUVERTURE   quelque chose qui se passe aujourd'hui, avec un visage
                      ou une main dedans.
2-3     LE MILIEU     le vrai contenu : le procédé, le résultat, l'erreur.
4       LA DEMANDE    un sticker. Sondage, boîte à questions, quiz ou lien.
5       LA CLÔTURE    la réponse, le résultat, ou la mise en place de demain.
```

Mettez la demande en story 4, pas en story 7. On perd du monde à chaque tap, et
la demande doit être vue par ceux qui sont encore là.

## Les stickers, et à quoi chacun sert vraiment

| sticker | rôle | à utiliser quand |
| --- | --- | --- |
| **Sondage** | le tap le moins cher qui existe | vous voulez du volume de réponses, pas de l'information |
| **Boîte à questions** | récolter les mots exacts que les gens emploient | vous avez besoin d'idées de contenu ou d'objections, mot pour mot |
| **Quiz** | apprendre en laissant se tromper | il existe une idée reçue répandue dans le domaine |
| **Curseur** | prise de température | rien d'important. Amusant, peu de valeur |
| **Lien** | la seule surface cliquable avec la bio | il y a un vrai endroit où aller |
| **Compte à rebours** | une échéance à laquelle on peut s'abonner | un lancement, un live, une date de clôture |
| **Ajoutez le vôtre** | de la portée au-delà de vos abonnés, de temps en temps | la consigne est une question à laquelle n'importe qui du domaine peut répondre |

La boîte à questions est la plus sous-estimée de la liste. Chaque réponse est
une légende, une accroche de Reel ou une ouverture de DM écrite avec les mots du
public. Passez-les à `/ig-reel` comme formule #16 La question mot pour mot.

## Règles

- **Un visage ou une main dans la première story.** Du texte sur fond de
  couleur se fait passer d'un tap, et la première story décide si les suivantes
  seront regardées.
- **Une idée par story.** Lire un paragraphe en story, personne ne le fait.
- **Gardez le texte au centre.** Sur 1080x1920, rien au-dessus de y=250 ni
  en dessous de y=1600. La ligne du profil est en haut et la barre de réponse en
  bas. Le message sanitaire aussi reste dans cette zone.
- **Parlez à une seule personne.** « Tu » ou « vous », mais à quelqu'un, pas à
  une foule. Les stories sont ce qui ressemble le plus à un DM sans en être un.
- **Ne repartagez pas votre propre post en story sans commentaire.** C'est la
  story la plus ignorée de la plateforme. Si vous renvoyez vers un post, dites
  ce qui s'est passé dans les commentaires et pourquoi ça vaut le coup d'y
  retourner.
- **Vendez en stories, pas en posts.** Trois stories de contexte, une d'offre,
  une de preuve. Cette séquence vend plus qu'un post sur le même sujet et ne
  vous coûte aucune portée.

## L'entonnoir vers les DM, fait honnêtement

La séquence qui marche : une story qui nomme un problème, une boîte à questions
ou un sondage qui permet de dire « c'est moi », puis une réponse à chaque
personne qui a répondu. La conversation commence parce qu'ils ont parlé en
premier.

Les réponses automatiques en DM sur mot-clé sont une fonctionnalité réelle et
prise en charge pour les comptes professionnels, via les outils d'Instagram et
des partenaires agréés. Envoyer des DM en masse à des gens qui n'ont pas
interagi ne l'est pas, et c'est ce qui fait restreindre des comptes. La règle
est simple : **ils agissent d'abord, ensuite vous répondez.** Pour une
brasserie : pas de relance commerciale sur la bière à quelqu'un dont vous
ignorez l'âge.

## Sortie

Les stories dans l'ordre, chacune avec ce qui est à l'écran, ce qui est dit et
quel sticker, plus quoi faire des réponses. Exemple fictif :

```
STORIES  ·  mardi  ·  5 stories

1  [selfie, en marchant vers la cuve]   « Brassin de la blonde ce matin. On a changé un houblon. »
2  [vidéo, la main dans les cônes]       le houblon, en gros plan
3  [face caméra]                         « Plus d'agrumes, moins d'amertume. Ça s'entend au nez. »
4  [sondage]                             « Vous la préférez comment ? »  Plus fruitée / Plus amère
5  [texte sur photo de la bouteille]     « Répondez et je vous dis où la trouver samedi. »
                                         « L'abus d'alcool est dangereux pour la santé. »

Ensuite : chaque personne qui a voté reçoit une réponse. C'est tout l'entonnoir.
loi Évin :  message sanitaire présent (stories 2 à 5) · 0 élément À FAIRE VALIDER
```

Rien n'est publié. L'utilisateur publie ses stories.
