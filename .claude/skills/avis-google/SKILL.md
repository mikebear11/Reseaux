---
name: avis-google
description: >-
  Répondre aux avis Google (et autres plateformes d'avis) de la brasserie, dans
  sa voix : merci précis sur les 5 étoiles, réponse calme et factuelle sur les
  1 étoile, traitement à part des avis faux, injustes ou qui parlent de santé.
  À utiliser quand l'utilisateur colle un avis ou une liste d'avis, dit
  « réponds à cet avis », « un client nous a mis une étoile », « qu'est-ce que
  je réponds sur Google », « vide mon arriéré d'avis », ou demande ce que
  disent les avis.
---

# avis-google

Adapté de `review-response-writer` (OneWave-AI/claude-skills, licence MIT,
voir `../LICENSE-onewave-claude-skills`), traduit et réécrit pour la Brasserie
de Sulauze.

La réponse à un avis négatif s'écrit pour tous ceux qui la liront ensuite, pas
pour l'auteur de l'avis. Entrée : le texte des avis (collé, exporté ou en
capture). Sortie : des réponses prêtes à copier, et la liste de ceux qui
demandent plus que des mots.

**Ce skill ne publie rien.** Il n'existe ici aucun outil pour répondre sur
Google : la brasserie copie elle-même la réponse dans sa fiche
d'établissement. Jamais d'automatisation par navigateur.

Lisez `regles-google.md` (dans ce dossier) et `../ig-caption/loi-evin.md`
avant la première réponse de la session.

## Langue et ton

- Rédigez en français, dans la voix décrite par `instagram/voice.md`
  (vouvoiement par défaut s'il n'est pas confirmé).
- Une réponse de propriétaire qui sonne comme le propriétaire vaut mieux
  qu'une réponse polie d'entreprise : gardez la personnalité, évitez les
  formules toutes faites. Passez chaque lot par `/ig-human`.
- Typographie française. Pas de tiret cadratin.

## Règles de la brasserie (priment sur tout)

1. **Message sanitaire.** Dès que la réponse parle de bière, de dégustation,
   de brassage ou de tout autre alcool, elle se termine par « L'abus d'alcool
   est dangereux pour la santé. » Dans le doute, mettez-la. Une réponse qui
   ne parle que d'accueil, de parking ou d'horaires peut s'en passer : dites
   dans le récapitulatif lesquelles n'en ont pas, et pourquoi.
2. **Ce qu'on peut dire de la bière** : ce que L3323-4 autorise (degré,
   origine, ingrédients, brassage, couleur, arômes, goût décrits
   objectivement, où l'acheter). Pas de fête, pas de « on trinque », pas
   d'humour sur l'alcool. Sinon : « À FAIRE VALIDER (Loi Évin) ».
3. **Pas de prix, de promo, de lien boutique ni d'invitation à acheter** dans
   une réponse (règle Google sur l'alcool, voir `regles-google.md` §3). Pas de
   geste commercial en public non plus : il apprend aux gens qu'un avis
   négatif rapporte une remise.
4. **Jamais « bio », « biologique » ni « biodynamie ».**
5. **Ne rien inventer.** Une réponse n'affirme une correction (« nous avons
   changé… ») que si la brasserie l'a dite. Sinon `{{à fournir}}`. Pareil pour
   un nom de bière, un horaire, un événement, le contact pour la suite.
6. **Pas de mineurs.** Un avis qui évoque un mineur servi ou présent avec de
   l'alcool passe en ESCALADE.

## Méthode

1. **La voix.** Lisez `instagram/voice.md` et, s'il y en a, quelques réponses
   déjà publiées par la brasserie (demandez-les une fois). Notez la chaleur,
   le registre, la signature (prénom ? « L'équipe de Sulauze » ?). La
   signature non confirmée reste `{{signature}}`.
2. **Trier chaque avis :**
   - `MERCI` (4-5 étoiles) : remercier précisément, en reprenant un détail de
     l'avis (jamais un merci générique), et inviter à revenir. Pas
     d'invitation à acheter.
   - `PLAINTE FONDÉE` : reconnaître le problème précis sans excuse ni
     justification, dire ce qui a été corrigé (si la brasserie l'a dit), et
     proposer de poursuivre hors ligne avec un vrai contact (`{{contact}}` tant
     qu'il n'est pas fourni). Ne jamais argumenter.
   - `INJUSTE / ERRONÉ` : rectifier un fait, brièvement et poliment
     (« D'après nos horaires, la boutique était fermée ce dimanche-là… »),
     uniquement avec des faits fournis par la brasserie.
   - `SUSPECT` (pas de trace du client, schéma de concurrent) : une réponse
     neutre et unique (« Nous ne retrouvons pas votre passage ; écrivez-nous à
     {{contact}} pour qu'on regarde ensemble »), aucune accusation publique, et
     les étapes de signalement de `regles-google.md` §4 avec la règle Google
     qui semble enfreinte. Rappelez que Google ne supprime pas un avis
     seulement parce qu'il déplaît.
   - `ESCALADE` : malaise, intoxication, blessure, allergie, corps étranger
     dans une bouteille, mineur, discrimination, menace juridique, employé
     nommé dans une accusation. Pas de réponse finale : signalez-le à la
     brasserie, proposez au plus une réponse d'attente sans reconnaissance de
     faute ni détail médical (« Nous prenons votre message très au sérieux et
     vous contactons directement »), et conseillez un avis juridique si c'est
     sérieux.
3. **Rédiger.** Moins de 100 mots pour un avis positif, moins de 150 pour un
   négatif. Variez la structure dans un lot : dix réponses sur le même modèle
   se lisent comme un robot.
4. **Contrôler** chaque réponse avant de la montrer : message sanitaire si
   alcool, aucun prix ni lien, rien d'inventé, pas de « bio », pas de nom
   d'employé dans un contexte d'accusation.
5. **Récapitulatif du lot.** Ordre conseillé : les négatifs les plus anciens
   sans réponse d'abord, puis les positifs récents. Notez les motifs qui se
   répètent : trois avis sur l'attente à la boutique, c'est un sujet
   d'organisation, pas de rédaction.

## Ce que le skill ne fait jamais

- Écrire un avis, pour la brasserie ou contre un concurrent (Code de la
  consommation, L121-4 28°).
- Conseiller de ne demander des avis qu'aux clients contents, d'offrir quoi
  que ce soit contre un avis, ou de demander aux clients de citer un mot ou
  une bière (règles Google, `regles-google.md` §1).
- Répondre avec sarcasme, ou sur le ton de l'auteur de l'avis.
- Dire qu'une réponse « respecte la Loi Évin » ou « respecte les règles de
  Google ». Il dit ce qu'il a vérifié et ce qui ne l'a pas été.

## Délai de réponse

Aucune source Google consultée ne fixe de délai ni ne dit que la vitesse de
réponse compte pour le classement. Proposez un rythme à la brasserie (par
exemple, un passage par semaine sur les nouveaux avis) comme une habitude, pas
comme une règle.

## Fichier de suivi

Les réponses validées par la brasserie peuvent être notées dans
`google/avis.md` à la racine du dépôt (date, note, extrait de l'avis, réponse,
statut : copiée ou non). Le créer à la première utilisation et le commiter
après chaque modification.

## Commandes rapides

- « Réponds à cet avis » : un avis, dans la voix de la brasserie
- « Vide mon arriéré » : un lot trié avec brouillons et récapitulatif
- « Gère ce 1 étoile » : réponse publique, message hors ligne, et évaluation
  du signalement si c'est justifié
- « Que disent nos avis ? » : les motifs récurrents, côté organisation
