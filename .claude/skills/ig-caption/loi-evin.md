# Loi Évin : ce que ça change pour un post Instagram de brasserie

Ce fichier n'est pas un avis juridique. Il reprend le texte des articles en
vigueur et dit clairement où s'arrête ce qu'on sait. En cas de doute sur un
post précis, faites-le valider (avocat, ARPP, syndicat professionnel).

Sources, consultées le 18/10/2026 :
- Code de la santé publique, art. L3323-2, version en vigueur depuis le
  02/03/2017 : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000034110404
- Code de la santé publique, art. L3323-4 :
  https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000049070860
- Code de la santé publique, art. L3323-3-1 (loi n° 2016-41 du 26 janvier 2016) :
  https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031917671
- Ministère de la Santé, « Alcool : cadre légal », mis à jour le 09/08/2024 :
  https://sante.gouv.fr/prevention-en-sante/addictions/article/alcool-cadre-legal

## 1. Instagram est un support autorisé, sous conditions

L3323-2, 9° : la publicité pour l'alcool est autorisée « sur les services de
communications en ligne à l'exclusion de ceux qui, par leur caractère, leur
présentation ou leur objet, apparaissent comme principalement destinés à la
jeunesse, ainsi que ceux édités par des associations, sociétés et fédérations
sportives ou des ligues professionnelles au sens du code du sport, sous réserve
que la propagande ou la publicité ne soit ni intrusive ni interstitielle. »

Même article : « Toute opération de parrainage est interdite lorsqu'elle a pour
objet ou pour effet la propagande ou la publicité, directe ou indirecte, en
faveur des boissons alcooliques. »

## 2. Ce qu'une publicité pour de l'alcool a le droit de dire

L3323-4, texte exact :

> La publicité autorisée pour les boissons alcooliques est limitée à
> l'indication du degré volumique d'alcool, de l'origine, de la dénomination,
> de la composition du produit, du nom et de l'adresse du fabricant, des agents
> et des dépositaires ainsi que du mode d'élaboration, des modalités de vente et
> du mode de consommation du produit.
>
> Cette publicité peut comporter des références relatives aux terroirs de
> production, aux distinctions obtenues, aux appellations d'origine [...] ou aux
> indications géographiques [...]. Elle peut également comporter des références
> objectives relatives à la couleur et aux caractéristiques olfactives et
> gustatives du produit.

Donc, permis sans discussion : degré, origine, nom de la bière, ingrédients,
brasserie et adresse, comment elle est brassée, où et comment l'acheter, comment
la servir, médailles, couleur, arômes, goût décrits objectivement.

Tout le reste (ambiance de fête, des gens qui trinquent, humour, réussite
sociale, séduction, sport) sort de la liste telle qu'elle est écrite. Je ne sais
pas où la jurisprudence place la limite exacte pour chaque type de post : c'est
précisément le cas où il faut faire valider avant de publier.

## 3. Le message sanitaire est obligatoire

L3323-4 : toute publicité « doit être assortie d'un message de caractère
sanitaire précisant que l'abus d'alcool est dangereux pour la santé ».

La formule courante est « L'abus d'alcool est dangereux pour la santé, à
consommer avec modération. » Seule la première moitié découle directement du
texte ; « à consommer avec modération » est un usage, pas une obligation écrite
dans l'article.

Le texte ne dit pas où le message doit apparaître dans un post Instagram
(légende ou visuel). Je ne connais pas de position officielle là-dessus. En
pratique : mettez-le dans la légende ET sur le visuel quand le produit est
montré, c'est l'option la plus prudente. `caption.py` vérifie sa présence dans
la légende.

## 4. L'exception « terroir » ne couvre probablement pas une bière artisanale

L3323-3-1 : ne sont pas considérés comme de la publicité les contenus relatifs à
une région, un terroir, un savoir-faire, l'histoire ou le patrimoine « liés à
une boisson alcoolique disposant d'une identification de la qualité ou de
l'origine, ou protégée au titre de l'article L. 665-6 du code rural et de la
pêche maritime ».

Cette exception vise les boissons sous signe officiel (AOP, IGP, etc.). Une
bière artisanale sans un tel signe n'en bénéficie probablement pas. Je ne sais
pas si les vôtres en ont un : si c'est le cas, dites-le dans `voice.md`.

## 5. Mineurs

La vente d'alcool et l'offre gratuite d'alcool à tous les mineurs sont
interdites (loi n° 2009-879 du 21 juillet 2009, art. 93, selon le ministère de
la Santé). Pas de mineur à l'image avec le produit, pas de contenu qui vise les
moins de 18 ans.

## 6. Influenceurs

Si vous faites appel à des créateurs rémunérés ou payés en produits, la loi
n° 2023-451 du 9 juin 2023 encadre l'influence commerciale. Je ne l'ai pas
vérifiée en détail ici : faites valider avant toute collaboration payée.

## Ce que les skills font de tout ça

- Chaque légende, Reel, carrousel ou story qui montre ou nomme une bière porte
  le message sanitaire.
- Les accroches et scripts s'appuient d'abord sur ce que L3323-4 autorise : le
  brassage, les ingrédients, l'origine, les arômes, les médailles, où acheter.
  C'est aussi ce qui donne les meilleures accroches (des chiffres, des noms,
  du concret).
- Tout contenu qui sort de cette liste est signalé « À FAIRE VALIDER (Loi
  Évin) » dans le récapitulatif, jamais présenté comme conforme.
- Les skills ne disent jamais qu'un post « respecte la Loi Évin ». Ils disent
  ce qu'ils ont vérifié et ce qui ne l'a pas été.
