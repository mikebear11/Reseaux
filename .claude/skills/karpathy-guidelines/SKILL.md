---
name: karpathy-guidelines
description: Quatre règles de travail pour éviter les erreurs typiques d'un assistant IA (hypothèses cachées, travail trop compliqué, modifications hors sujet, objectif flou), appliquées aux contenus Instagram comme aux scripts du dépôt. À utiliser avant toute tâche qui n'est pas triviale - écrire ou corriger une légende, un Reel, un carrousel, un plan, modifier un script (`caption.py`, `hookscore.py`…) ou un fichier de travail -, quand une demande est floue, ou quand l'utilisateur dit « réfléchis avant », « fais simple », « ne touche qu'à ça », « comment on vérifie ? ».
license: MIT
---

# Règles Karpathy

Traduit et adapté de [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)
(commit `2c60614`, licence MIT, auteur forrestchang). Le dépôt d'origine s'appuie
sur un [post d'Andrej Karpathy sur X](https://x.com/karpathy/status/2015883857489522876)
à propos des erreurs des modèles de langage quand ils codent. L'original ne parle
que de code ; cette version l'étend aux contenus de la brasserie.

**Ordre de priorité :** les « Règles qui priment sur tout » de `CLAUDE.md`
(message sanitaire, pas de « bio », ne rien inventer, pas de publication sans
« oui ») passent avant ces quatre règles.

**Compromis :** ces règles privilégient la prudence sur la vitesse. Pour une
tâche triviale (une faute de frappe, un mot à changer), juger au cas par cas.

## Le constat de départ

Le dépôt d'origine cite trois reproches de Karpathy aux modèles :

> « The models make wrong assumptions on your behalf and just run along with them
> without checking. They don't manage their confusion, don't seek clarifications,
> don't surface inconsistencies, don't present tradeoffs, don't push back when they
> should. »

En clair : ils supposent à ta place sans vérifier, ne disent pas quand ils sont
perdus, ne posent pas de question, ne signalent pas les incohérences, ne
présentent pas les choix possibles et ne contredisent pas quand il faudrait.

> « They really like to overcomplicate code and APIs, bloat abstractions, don't
> clean up dead code... »

Ils compliquent, gonflent, et ne nettoient pas derrière eux.

> « They still sometimes change/remove comments and code they don't sufficiently
> understand as side effects, even if orthogonal to the task. »

Ils modifient ou suppriment au passage des choses qu'ils ne comprennent pas et
qui n'ont rien à voir avec la demande.

## 1. Réfléchir avant d'agir

**Ne pas supposer. Ne pas cacher qu'on est perdu. Montrer les choix.**

Avant de produire :
- Dire ses hypothèses à voix haute. En cas de doute, demander.
- Si la demande a plusieurs lectures, les présenter au lieu d'en choisir une en silence.
- S'il existe plus simple, le dire. Contredire quand c'est justifié.
- Si quelque chose est flou : s'arrêter, nommer ce qui bloque, demander.

Exemple. Demande : « Fais-moi une légende pour la nouvelle bière. »

À ne pas faire : inventer un nom, un style, un degré et une date de sortie, puis
écrire la légende.

À faire :
```
Avant d'écrire, il me manque :
1. Le nom de la bière et son style : {{à fournir}}
2. Le support : Reel, carrousel ou photo ?
3. Le but : annoncer la sortie, faire venir à la brasserie, vendre en ligne ?
4. Une info à mettre en avant (date, lieu, accord mets) : {{à fournir}}

Le plus simple : une légende courte d'annonce, avec le message sanitaire.
Je pars là-dessus si tu me donnes le nom et le style.
```

## 2. Faire simple

**Le minimum qui répond à la demande. Rien de spéculatif.**

- Rien au-delà de ce qui est demandé.
- Pas d'abstraction, de modèle ou de structure pour un usage unique.
- Pas d'option, de variante ou de « souplesse » que personne n'a demandée.
- Pas de gestion de cas impossibles.
- Si 200 lignes peuvent en faire 50, réécrire.

Question à se poser : « Un professionnel expérimenté trouverait-il ça trop
compliqué ? » Si oui, simplifier.

Pour le contenu : une légende demandée, c'est une légende, pas trois versions,
un plan de diffusion et une série de stories en prime. Proposer la suite en une
ligne, ne pas la produire d'office.

## 3. Changements chirurgicaux

**Ne toucher que ce qu'il faut. Ne nettoyer que ses propres dégâts.**

En modifiant un texte, un fichier ou un script existant :
- Ne pas « améliorer » le texte, le code, les commentaires ou la mise en forme d'à côté.
- Ne pas réécrire ce qui marche.
- Garder le style existant, même si on ferait autrement.
- Si on voit quelque chose de mort ou de faux sans rapport, le signaler, ne pas le supprimer.

Quand ses propres changements laissent des restes :
- Retirer ce que SES changements ont rendu inutile.
- Ne pas supprimer ce qui était déjà mort avant, sauf demande.

Test : chaque ligne modifiée se rattache directement à la demande.

Exemple : on demande de corriger une ligne de `instagram/voice.md`.
On change cette ligne, et rien d'autre. Si une autre ligne du fichier semble fausse,
on le dit dans la réponse.

## 4. Viser un résultat vérifiable

**Fixer un critère de réussite. Recommencer jusqu'à ce qu'il soit atteint.**

Transformer la tâche en objectif vérifiable :

| Au lieu de… | Viser… |
|---|---|
| « Ajoute une vérification » | Écrire des tests pour les entrées invalides, puis les faire passer |
| « Corrige le bug » | Écrire un test qui reproduit le bug, puis le faire passer |
| « Réorganise X » | Les tests passent avant et après |
| « Écris la légende » | `caption.py` ne signale plus rien, message sanitaire compris |
| « Une meilleure accroche » | Un score `hookscore.py` comparé avant et après |

Pour une tâche en plusieurs étapes, donner un plan court :
```
1. [Étape] → vérification : [contrôle]
2. [Étape] → vérification : [contrôle]
3. [Étape] → vérification : [contrôle]
```

Un critère solide permet d'avancer seul. Un critère faible (« que ça marche »)
oblige à redemander sans cesse.

Le dépôt d'origine cite aussi Karpathy sur ce point :

> « LLMs are exceptionally good at looping until they meet specific goals...
> Don't tell it what to do, give it success criteria and watch it go. »

Autrement dit : les modèles sont très bons pour recommencer jusqu'à atteindre un
objectif précis. Il vaut mieux leur donner un critère de réussite qu'une liste
d'instructions.

## Les erreurs à éviter, en résumé

| Règle | Erreur typique | Correction |
|---|---|---|
| Réfléchir avant d'agir | Supposer le support, la bière, le ton ou le but | Lister les hypothèses, demander |
| Faire simple | Livrer trois variantes et un plan quand on demande une légende | Livrer ce qui est demandé, proposer la suite en une ligne |
| Changements chirurgicaux | Reformuler tout le fichier en corrigeant une ligne | Ne changer que la ligne concernée |
| Viser un résultat vérifiable | « Je vais revoir et améliorer le texte » | « Corriger X → contrôler avec `caption.py` → montrer le résultat » |

L'idée de fond, selon le dépôt d'origine : la version compliquée n'est pas
forcément fausse, elle arrive trop tôt. Elle est plus dure à relire, cache plus
d'erreurs et prend plus de temps. **Un bon travail règle simplement le problème
d'aujourd'hui, pas celui de demain avant l'heure.**

## Comment savoir que ça marche

- Les modifications ne contiennent que ce qui a été demandé.
- Moins de réécritures parce que c'était trop compliqué.
- Les questions arrivent avant le travail, pas après les erreurs.
- Des commits et des PR courts, sans « améliorations » au passage.
