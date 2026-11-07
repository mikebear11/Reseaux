---
name: seo-local
description: >-
  Auditer la présence locale de la brasserie sur Google : fiche
  d'établissement, avis, cohérence du nom, de l'adresse et du téléphone sur les
  annuaires et réseaux, et couche locale du site sulauze.com. Produit une liste
  de corrections sourcées. À utiliser quand l'utilisateur dit « audite notre
  fiche Google », « pourquoi on n'apparaît pas sur Maps », « brasserie près de
  Miramas », « vérifie nos annuaires », « comment avoir plus d'avis », ou
  colle le contenu de sa fiche d'établissement.
---

# seo-local

Adapté de `local-seo-optimizer` (OneWave-AI/claude-skills, licence MIT, voir
`../LICENSE-onewave-claude-skills`), traduit et réécrit pour la Brasserie de
Sulauze. Les affirmations chiffrées de l'original qui n'avaient pas de source
(nombre de photos, poids de la catégorie principale) ont été retirées.

Pour une brasserie qui vend aussi sur place (boutique, click & collect,
visites), la fiche Google est souvent ce que voit un client avant le site.
Ce skill dresse l'état des lieux et la liste des corrections. **Il ne modifie
rien** : la brasserie fait les changements dans sa fiche
(business.google.com), sur son site et ses annuaires.

Lisez `../avis-google/regles-google.md` et `../ig-caption/loi-evin.md` avant de
commencer.

## Ce que Google dit, et seulement ça

Selon Google, les résultats locaux reposent « principalement » sur la
pertinence, la distance et la popularité, et des informations « complètes et
exactes » augmentent les chances d'apparaître (`regles-google.md` §5, source
[G3]). Le poids exact de chaque élément n'est pas public. Le skill ne promet
donc aucun gain de classement et ne présente pas de « facteur le plus
important ».

## Règles de la brasserie (priment sur tout)

- **Jamais « bio », « biologique » ni « biodynamie »** dans la description de
  la fiche, les produits, les posts ou le site. Si une ancienne mention bio
  traîne quelque part (fiche, annuaire, site), c'est une correction
  prioritaire de l'audit.
- **Message sanitaire** sur tout texte proposé qui parle de bière (post Google,
  description produit, page du site) : « L'abus d'alcool est dangereux pour la
  santé. »
- **Pas de prix, de promotion datée ni d'appel direct à acheter dans la
  fiche** (règle Google, `regles-google.md` §3). Les actualités et offres sont
  admises dans les posts selon Google, mais l'alcool reste un contenu
  « soumis à des restrictions » : tout post qui mentionne un prix ou une
  remise sur de la bière est signalé « À FAIRE VALIDER (règles Google / Loi
  Évin) ».
- **Ne rien inventer** : catégories, horaires, adresse, téléphone, services
  viennent de la brasserie ou d'une source citée. Sinon `{{à fournir}}`.

## Méthode

1. **Point de départ.** Demandez (ou relevez sur des pages publiques) :
   catégorie actuelle de la fiche, adresse exacte, zone de chalandise,
   horaires de la boutique et des visites, téléphone, lien du site. Demandez
   à la brasserie 5 à 10 recherches qu'un client ferait vraiment (par exemple
   « brasserie artisanale Miramas », « bière locale Istres », « visite
   brasserie Bouches-du-Rhône ») : ce sont des hypothèses à confirmer, pas des
   volumes de recherche mesurés. Le skill n'a pas d'outil de mesure de
   positions : si l'utilisateur fait les recherches, il colle les résultats ;
   sinon, dites « Je ne sais pas » sur la position actuelle.
2. **Audit de la fiche**, champ par champ, à partir de ce que la brasserie
   colle ou montre (Google Maps se lit mal automatiquement) : fiche validée,
   catégorie principale et secondaires (exactes, sans mot-clé ajouté au nom),
   adresse, horaires y compris exceptionnels, attributs (parking, accès…),
   description, produits, photos (intérieur, extérieur, brassage, boutique),
   date du dernier post, questions-réponses. Pour chaque écart : ce qui est
   vu, la correction, la source de la règle.
3. **Avis.** Nombre, note moyenne, part d'avis ayant une réponse, motifs qui
   reviennent. Pour la suite : une façon de demander des avis **conforme aux
   règles Google** (`regles-google.md` §1) : demander à tous les clients, pas
   seulement aux contents ; aucun avantage en échange ; ne pas leur demander
   de citer un mot, une bière ou un employé ; pas de pression sur place. Un
   lien direct vers le formulaire d'avis est fourni par la brasserie depuis sa
   fiche (`{{lien avis}}`). Pour répondre aux avis : `/avis-google`.
4. **Cohérence nom / adresse / téléphone.** Comparez la fiche Google avec le
   site sulauze.com, Instagram `@sulauze`, Facebook, et les annuaires où la
   brasserie apparaît (à vérifier un par un : Apple Plans, Bing Places,
   PagesJaunes, TripAdvisor, Untappd…). Listez chaque écart avec la
   correction. Écarts déjà connus au 18/10/2026 (voir `instagram/voice.md`) :
   le site renvoie vers `instagram.com/brasseriesulauze` au lieu de `@sulauze`,
   le lien de la bio Instagram s'écrit « wwww.sulauze.com », et la bio cite
   « Miramas / Istres » : l'adresse de référence est à confirmer.
5. **Couche locale du site.** Vérifiez : adresse, horaires et téléphone
   identiques à la fiche ; carte intégrée ; balisage schema.org du type
   `Brewery` (type qui existe, sous-type de `FoodEstablishment` et
   `LocalBusiness` : https://schema.org/Brewery) avec les mêmes informations ;
   titres de pages qui disent où est la brasserie. Pas de pages « ville »
   copiées-collées (Miramas, Istres, Salon…) sans contenu propre : signalez
   celles qui existent, n'en fabriquez pas.

## Livrable

Un rapport en français, dans cet ordre :
1. Ce qui est faux ou incohérent (adresse, horaires, liens, mention bio) :
   à corriger d'abord.
2. Ce qui manque dans la fiche.
3. Les avis : état et méthode de demande conforme.
4. Le site.
Chaque ligne dit : constat, correction, source (page Google, Légifrance, ou
« donné par la brasserie le … »). Ce qui n'a pas pu être vérifié est écrit
« Je ne sais pas » ou `{{à fournir}}`.

Proposez de refaire le point dans 4 à 6 semaines : c'est un rythme de suivi,
pas une durée garantie par Google.

Le rapport peut être enregistré dans `google/audit-AAAA-MM-JJ.md` à la racine
du dépôt et commité.

## Ce que le skill ne fait jamais

- Conseiller des faux avis, des avis de salariés ou de proches, des avis
  achetés ou filtrés (règles Google ; Code de la consommation L121-4 28°).
- Ajouter des mots-clés, une ville ou un slogan au nom de l'établissement
  sur la fiche (consignes Google, `regles-google.md` §6).
- Promettre une position ou un délai de résultat.
