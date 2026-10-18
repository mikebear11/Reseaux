---
name: ig-caption
description: >-
  Écrire la légende Instagram : la ligne qui survit à la coupure « … plus », le
  corps, l'appel à l'action unique, les termes de recherche et jusqu'à 5
  hashtags, puis la vérifier avant publication. À utiliser quand l'utilisateur
  dit « écris la légende », « fais-moi une légende pour ce post », « qu'est-ce
  que je mets en description », « quels hashtags », a un Reel ou un carrousel
  prêt et a besoin du texte, ou pose une question sur les hashtags.
---

# ig-caption

Un outil vit dans ce dossier, et il se lance comme ceci :

```bash
python3 caption.py caption.txt
python3 caption.py caption.txt --keywords "bière artisanale,bière de saison"
python3 caption.py caption.txt --lang fr --evin on
```

Il affiche la légende comme le fil l'affiche : les 125 premiers caractères dans
un cadre, tout le reste derrière le tap. Lisez ce cadre avant de relire quoi que
ce soit d'autre de ce que vous avez écrit.

Options : `--lang auto|fr|en` (défaut `auto` : détecte la langue du texte, et
reconnaît les appels à l'action français) et `--evin auto|on|off` (contrôle
`ÉVIN`, voir plus bas).

## Langue et ton

- Rédigez en français.
- Respectez le tutoiement ou le vouvoiement indiqué dans
  `~/.claude/instagram/voice.md`. S'il n'y est pas, demandez une fois ; sans
  réponse, vouvoyez.
- Typographie française : « guillemets », apostrophe ’ ou ', espace avant ; : ! ?
  acceptée. Pas de tiret cadratin.

## Loi Évin

Lisez `../ig-caption/loi-evin.md` (le fichier `loi-evin.md` de ce dossier) avant
toute légende de brasserie.

- Toute légende qui montre ou nomme une bière porte le message sanitaire
  « L'abus d'alcool est dangereux pour la santé ». Mettez-le aussi sur le
  visuel quand le produit est montré.
- Appuyez la légende d'abord sur ce que L3323-4 autorise : degré, origine,
  ingrédients, brassage, arômes, couleur, médailles, où acheter.
- Tout le reste (fête, trinquer, humour, séduction, sport, réussite sociale)
  est signalé « À FAIRE VALIDER (Loi Évin) » dans le récapitulatif.
- Pas de mineurs, pas de parrainage. Une collaboration d'influenceur payée
  (en argent ou en produits) se fait valider avant.
- Ne dites jamais qu'une légende « respecte la Loi Évin ». Dites ce qui a été
  vérifié et ce qui ne l'a pas été.

## D'abord, décidez quel travail fait cette légende

C'est la décision qui ruine les légendes quand on la saute.

**Travail A : la vidéo les a déjà accrochés.** Un Reel porte sa propre accroche
dans les deux premières secondes, dite et en texte à l'écran. La légende n'est
pas une deuxième accroche, et faire concurrence à la vidéo, c'est perdre les
deux. Son travail : l'appel à l'action, le contexte qui lui donne du sens, et
les mots que les gens recherchent.

**Travail B : la légende est le contenu.** Une photo, une image seule, une
couverture de carrousel qui ouvre une boucle. Ici, la ligne 1 est l'accroche et
elle fonctionne exactement comme une accroche de Reel : concrète, courte, et
coupée sur un suspense plutôt qu'au milieu d'une proposition.

Demandez-vous lequel vous écrivez. Si l'utilisateur a un Reel avec une accroche
forte, écrivez A et dites pourquoi.

## La forme

```
Ligne 1     125 caractères visibles. Travail A : l'appel à l'action, simplement.
            Travail B : l'accroche.
            Jamais une salutation, jamais un hashtag, jamais un emoji en
            premier caractère.
Corps       paragraphes courts, une ligne vide entre chacun. Deux à six.
            C'est là que vivent les termes de recherche.
L'appel     un seul. Commenter un mot-clé, enregistrer, ou envoyer un DM. Un.
Message     « L'abus d'alcool est dangereux pour la santé », dès qu'une bière
sanitaire   est montrée ou nommée.
Hashtags    jusqu'à 5, sur leur propre ligne en bas, ou aucun.
```

La limite est de 2 200 caractères et presque rien n'en a besoin. Une légende qui
mérite le tap puis livre 600 caractères bat une légende qui en livre 1 800.

## Les hashtags, honnêtement

Les hashtags ne sont plus un levier de portée, et la plateforme l'a maintenant
dit par un changement de produit. **Instagram a plafonné les hashtags à cinq par
post le 18 décembre 2025**, contre trente auparavant, en expliquant aux
créateurs qu'utiliser « moins de hashtags (jusqu'à 5), plus ciblés, plutôt que
beaucoup de hashtags génériques » fonctionne mieux. Adam Mosseri avait déjà dit
en février 2025 que les hashtags n'augmentent pas la portée : ce sont des
étiquettes, pas un levier de diffusion.

Donc : jusqu'à 5, précis, comme étiquettes de sujet. Si l'utilisateur garde un
bloc de vingt hashtags dans ses notes, ce bloc est désormais un poids mort et le
linter le fera échouer.

`#viral`, `#fyp`, `#explorepage`, `#foryou`, `#pourtoi` ne décrivent rien.
Coupez-les.

## Les termes de recherche comptent plus que les hashtags

La recherche Instagram lit le texte de la légende. Donc l'expression pour
laquelle l'utilisateur veut être trouvé va dans la légende, telle qu'un humain
la taperait, dans une phrase qui se lit normalement. « Bière artisanale » en
toutes lettres en ligne 3, pas « #bièreartisanale » dans un bloc en bas.

Demandez deux ou trois de ces termes, puis passez-les au linter :

```bash
python3 caption.py brouillon.txt --keywords "bière artisanale,bière de saison"
```

## Règles

- **Pas de lien dans la légende.** Les légendes ne sont pas cliquables. Une URL
  dans le corps est du texte mort qui dit « je n'utilise pas cette
  plateforme ». Bio ou DM.
- **Un seul appel à l'action.** Deux appels, c'est comme aucun. `caption.py`
  les compte, y compris en français.
- **L'appel à commenter un mot-clé exige un mot-clé que les gens peuvent
  taper.** Un mot, sans espace, sans emoji, et dites-le aussi à voix haute dans
  la vidéo. `Commentez HOUBLON` fonctionne. `Commentez « le guide des
  houblons »` ne fonctionne pas.
- **Écrivez le premier commentaire à part** s'il y a un lien. Dites-le dans le
  récapitulatif.
- **L'emoji comme ponctuation, pas comme décoration.** Le linter signale tout
  ce qui dépasse 4 emoji pour 100 caractères.
- **Le texte alternatif vaut 20 secondes.** Pour les carrousels et les photos,
  écrivez-le. Il est lu par les lecteurs d'écran et par Instagram.
- **Le message sanitaire n'est pas négociable** dès qu'une bière est montrée ou
  nommée. Il ne compte pas dans « un seul appel à l'action ».

## La boucle

1. Décidez Travail A ou Travail B, et dites lequel.
2. Rédigez.
3. Passez-la dans `/ig-human`. Les légendes sont courtes, donc les formules
   toutes faites (« slop ») s'y entendent plus que partout ailleurs dans le
   pack.
4. Lancez `caption.py` avec les termes de recherche de l'utilisateur
   (`--lang fr` si la détection hésite). Corrigez chaque FAIL. Tranchez chaque
   WARN à voix haute plutôt qu'en silence.
5. Contrôle `ÉVIN` : si `caption.py` renvoie FAIL parce que la légende parle
   d'alcool sans message sanitaire, ajoutez-le et relancez. `--evin on` force le contrôle
   (par exemple quand la bière n'est montrée que sur l'image) ; n'utilisez
   `--evin off` que pour un post sans aucun lien avec l'alcool. Relisez ensuite
   le contenu contre `loi-evin.md` : le script vérifie la présence du message,
   pas le reste. Chaque élément hors L3323-4 devient « À FAIRE VALIDER (Loi
   Évin) ».
6. Affichez le bloc prêt à copier, puis le récapitulatif :

```
LÉGENDE PRÊTE
travail:    A - le reel porte l'accroche
visible:    118 caractères sur 125 utilisés avant la coupure
appel:      un seul, commentez HOUBLON
hashtags:   3 (5 maximum)
recherche:  « bière artisanale » en ligne 3, « bière de saison » en ligne 5
loi Évin:   message sanitaire présent · 1 élément À FAIRE VALIDER (photo de
            terrasse entre amis)
linter:     READY
```

Rien n'est publié. L'utilisateur colle la légende et publie.
