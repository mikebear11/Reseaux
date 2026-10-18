---
name: ig-human
description: >-
  Retire l'empreinte machine de n'importe quel brouillon (tirets cadratins,
  formules toutes faites d'IA, caractères invisibles de filigrane) et le note
  sur un panel de cinq contrôles de détection avant qu'il sorte. À utiliser dès
  qu'un texte doit sonner humain, quand l'utilisateur dit « humanise ce
  texte », « est-ce que ça fait IA ? », « enlève les tirets cadratins »,
  « nettoie les formules toutes faites », « on dirait ChatGPT », ou avant de
  montrer à l'utilisateur toute légende, script, commentaire, réponse ou DM.
---

# ig-human

Deux outils vivent dans ce dossier et ils tournent vraiment. Servez-vous-en. Ne
faites pas ça à l'œil.

```bash
python3 humanize.py draft.txt --report        # nettoie, montre ce qui a changé
python3 detect.py draft.txt                    # note le texte, cinq contrôles
python3 detect.py before.txt after.txt         # prouve l'écart avant / après
```

Les deux scripts acceptent `--lang auto|fr|en` (défaut `auto` : la langue du
texte est détectée).

## Langue et ton

- Rédigez et réécrivez en français.
- Respectez le tutoiement ou le vouvoiement indiqué dans
  `~/.claude/instagram/voice.md`. S'il n'est pas indiqué, demandez une fois ;
  sans réponse, vouvoiement par défaut.
- Typographie française correcte : « guillemets », apostrophe, espace avant
  ; : ! ? acceptable. Pas de tiret cadratin.

## Les lexiques

En anglais, les scripts lisent `slop.json` : 154 mots et expressions toutes
faites avec leur remplacement en langage simple, 18 classes de caractères
invisibles, 11 substitutions typographiques et 16 tics structurels. Le dernier
bloc de chaque liste est propre à Instagram : le vocabulaire qu'on ne trouve
que dans les légendes et les voix off.

En français, ils lisent `slop.fr.json`, choisi automatiquement quand le texte
est en français. On y trouve le même genre de choses : les formules de
remplissage (« dans un monde en constante évolution »), les intensifs vides
(« véritable »), les tournures commerciales (« n'hésitez pas à », qui est
**signalée, pas supprimée**, parce que la phrase autour doit être réécrite à la
main), et le bloc Instagram (« arrête de scroller », « abonne-toi pour plus »).
Ce lexique français est une liste éditoriale, pas une mesure : il dit ce qui
sonne fabriqué à son auteur, il n'a été calibré sur aucun corpus.

Les deux fichiers sont faits pour être modifiés. Si l'utilisateur emploie
toujours un mot que le lexique supprime, retirez-le du fichier.

## Le message sanitaire n'est jamais touché

« L'abus d'alcool est dangereux pour la santé » (et la formule de `voice.md`
si elle est plus longue) reste mot pour mot dans tout texte nettoyé. Si un
texte parle d'alcool ou accompagne une image qui s'y rapporte et que la phrase
manque, ajoutez-la en fin de texte avant de le montrer. C'est la règle de la
brasserie, voir `../ig-caption/loi-evin.md`.

## Pourquoi c'est plus important sur Instagram qu'il n'y paraît

Les légendes sont courtes et les scripts sont dits à voix haute. Une phrase qui
sent l'écrit dans une légende de 600 caractères pèse plus lourd que la même
phrase dans un long texte, et une voix off que personne ne pourrait dire
naturellement s'entend dès la première prise. Le vrai signal ici n'est pas un
détecteur qui repère le post. C'est quelqu'un qui scrolle devant un texte qui
sonne comme une marque, ou un créateur qui bute sur son propre script.

## Ce qui est corrigé automatiquement

**1. Les caractères invisibles.** Espaces et liants de largeur nulle,
word joiners, traits d'union conditionnels, marques d'ordre d'octets,
caractères d'étiquette Unicode, séparateurs invisibles, espaces insécables et
fines. Un clavier ne les produit pas. Ils survivent au copier-coller, ils sont
invisibles dans tous les éditeurs, et ce sont les traces les plus mécaniques
d'un texte généré. `humanize.py` les supprime tous, y compris tout caractère de
format Unicode restant qu'il ne sait pas nommer.

Exception en français : les espaces insécables et fines (devant ; : ! ? et à
l'intérieur des « ») font partie de la typographie normale. En mode français,
`detect.py` ne les compte pas comme empreinte machine ; `humanize.py` les
remplace quand même par une espace normale, ce qui ne change rien à l'œil.

**2. La typographie.** Tiret cadratin vers virgule, tiret demi-cadratin vers
trait d'union, points de suspension vers trois points, puce vers trait
d'union, guillemets courbes “ ” et apostrophe ’ vers droits. Les guillemets
« » ne sont pas touchés. Le passage sur le tiret
cadratin est celui qui compte : il remplace le tiret par une virgule, puis
nettoie la double ponctuation et les points orphelins que ça laisse.

En français, `detect.py` ne compte ni l'apostrophe ’ ni les guillemets « »
comme empreinte machine. Seuls “ ” et ‘ comptent.

**3. Le lexique.** En anglais : delve, leverage, robust, seamless, crucial,
testament to, « in today's fast-paced world », plus le bloc Instagram :
« stop scrolling », « in today's video », « follow for more », « tag someone
who needs this », « the algorithm loves », « run don't walk ». En français, les
entrées de `slop.fr.json` décrites plus haut. Chaque entrée est remplacée par
un mot simple ou supprimée, la casse est conservée et les URL ne sont pas
touchées. Les entrées marquées comme signalées (« n'hésitez pas à ») ne sont
pas réécrites : elles apparaissent dans le rapport.

## Ce qui n'est PAS corrigé automatiquement

Les tics structurels sont **signalés, pas réécrits**, parce que changer la
forme d'une phrase demande du jugement :

- « Ce n'est pas juste X, c'est Y » et « non seulement X, mais aussi Y »
- Les triades systématiques (trois adjectifs, trois exemples)
- Les questions rhétoriques d'un mot sur leur propre ligne : « Le résultat ? »
- Le préambule vidéo : « dans cette vidéo, je vais vous montrer »
- Les listes à puces en émojis
- Trois mots ou plus en majuscules d'affilée
- Les murs de hashtags
- Les appâts réflexes : « abonne-toi pour plus », « identifie quelqu'un qui »,
  « double tape si »

Cette liste, c'est votre travail. Réécrivez chaque ligne signalée à la main en
gardant le sens, puis relancez `detect.py`. C'est ce qui fait passer la note de
REVIEW à PASS, et c'est la partie qu'un script ne peut pas faire.

## Les cinq contrôles

`detect.py` note cinq signaux de 0 à 100, plus c'est haut, plus c'est humain :

| contrôle | ce qu'il mesure | à quoi ressemble la machine |
| --- | --- | --- |
| BURSTINESS | variation de longueur des phrases | toutes les phrases de la même longueur |
| SPECIFICITY | chiffres, noms, marqueurs concrets pour 100 mots | noms abstraits, aucun chiffre |
| SLOP DENSITY | occurrences du lexique pour 100 mots | vocabulaire tout fait |
| FINGERPRINT | caractères invisibles, tirets cadratins, guillemets courbes pour 1 000 caractères | typographie trop parfaite |
| VOICE | en anglais : contractions ; en français : marques de l'oral (« c'est pas » sans « ne », « t'as », « y'a », « du coup »). Plus la personne (je, on, vous…) et les tics structurels | aucune marque d'oral, révélations mises en scène |

Le verdict pondère la moyenne à 60 % et le **contrôle le plus faible** à 40 %,
parce qu'un seul signal suffit. PASS demande une note globale de 70 ou plus,
sans aucun contrôle sous 55. Ces seuils sont ceux de l'auteur, mesurés en
anglais ; ils n'ont pas été recalibrés pour le français. Les élisions écrites
(« j'ai », « c'est ») ne comptent pas : en français elles sont obligatoires et
ne disent rien de la voix.

## Dites-le honnêtement

Ce sont cinq heuristiques locales, modelées sur les signaux qu'utilisent les
détecteurs publics. Elles tournent entièrement sur la machine de l'utilisateur
et rien n'est envoyé. Ce **ne sont pas** GPTZero, Originality, Copyleaks,
Winston ou Turnitin, elles n'appellent pas leurs API et ne peuvent pas promettre
leurs verdicts. Corriger ce qu'elles mesurent fait en général bouger ces
chiffres-là, parce qu'elles mesurent les mêmes choses de fond. C'est ça, la
promesse. N'en faites pas une plus grosse au nom de l'utilisateur, et ne lui
dites jamais que son texte est indétectable. En français, rappelez en plus que
le lexique est une liste éditoriale, pas une mesure.

## Ordre des opérations

1. `humanize.py draft.txt -o clean.txt --report`
2. Lisez les tics signalés. Réécrivez ces lignes vous-même.
3. `detect.py draft.txt clean.txt` pour montrer l'avant et l'après.
4. Si le verdict n'est pas PASS, corrigez le contrôle le plus faible indiqué
   dans la sortie et recommencez. Deux tours, c'est normal. Cinq, c'est que le
   brouillon a été écrit à la formule, et la solution est un autre brouillon,
   pas plus de passages.
5. Montrez à l'utilisateur le texte nettoyé et la note. Jamais la note seule.
