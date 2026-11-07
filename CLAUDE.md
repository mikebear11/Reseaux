# Reseaux : comptes de la Brasserie de Sulauze

Ce dépôt sert à gérer les réseaux sociaux de la Brasserie de Sulauze (Miramas,
13). Le compte principal est Instagram. Répondre en français.

## Compte géré

- Instagram : `@sulauze` (« Brasserie Sulauze | bière artisanale »), confirmé
  par la brasserie le 18/10/2026. Le lien `instagram.com/brasseriesulauze` du
  site sulauze.com n'est pas le bon compte (à corriger sur le site).
- Compte voisin, à ne pas confondre : `@sulauze.beergarden` (le beergarden).

## Règles qui priment sur tout

1. **Message sanitaire, toujours.** Tout contenu qui parle d'alcool, ou dont la
   photo ou la vidéo s'y rapporte, porte « L'abus d'alcool est dangereux pour
   la santé. » Détails : `.claude/skills/ig-caption/loi-evin.md`.
2. **Plus de bio.** La brasserie n'est plus en agriculture biologique
   (confirmé le 18/10/2026). Ne jamais écrire « bio », « biologique » ni
   afficher le logo AB, même si une ancienne source le dit. « Biodynamie » :
   pas d'usage tant que la brasserie ne l'a pas confirmé.
3. **Ne rien inventer.** Aucun chiffre, prix, médaille, date ou nom de bière
   qui ne vient pas de la brasserie ou d'une source citée. Sinon `{{à fournir}}`.
4. **Publication : jamais sans un « oui » explicite** sur le contenu exact
   (vidéo, légende, compte). Voir « Publication » ci-dessous.

## Fichiers de travail

Tout est dans `instagram/` à la racine du dépôt (les chemins `instagram/...`
des skills sont relatifs à cette racine) : `voice.md` (profil de ton),
`log.md` (historique des publications), `swipe.md`, `plan.md`. Les commiter
après chaque modification : une session cloud efface tout ce qui n'est pas
poussé.

## Publication

- Seul outil disponible ici : vidIQ (`vidiq_instagram_publish_reel`), qui passe
  par l'API officielle de Meta. Il ne publie que des **Reels** (vidéo de 3 s à
  15 min). Pas de photo, de carrousel ni de story : ceux-là, la brasserie les
  publie elle-même à partir du texte prêt à copier.
- Prérequis : un compte Instagram professionnel relié à vidIQ
  (app.vidiq.com), avec `publishingAvailable: true` dans
  `vidiq_instagram_connected_accounts`. Au 18/10/2026, aucun compte n'est relié.
- Avant chaque publication : montrer la vidéo, la légende finale (contrôlée par
  `caption.py`, message sanitaire compris) et le compte, puis attendre un
  « oui, publie ». Un accord ne vaut que pour ce Reel-là.
- Jamais d'automatisation par navigateur, de like, de follow, de commentaire
  ou de DM automatiques (conditions d'utilisation d'Instagram).
- Après publication : ajouter la ligne dans `instagram/log.md` et commiter.

## Façon de travailler (4 règles Karpathy)

Tirées de multica-ai/andrej-karpathy-skills (MIT), traduites et étendues au
contenu. Détails et exemples : skill `.claude/skills/karpathy-guidelines`.
Elles passent après les « Règles qui priment sur tout ». Pour une tâche triviale, juger au cas par cas.

1. **Réfléchir avant d'agir.** Dire ses hypothèses. S'il y a plusieurs
   lectures possibles de la demande, les présenter au lieu d'en choisir une en
   silence. Proposer plus simple quand ça existe. Si c'est flou : s'arrêter,
   nommer ce qui bloque, demander.
2. **Faire simple.** Rien au-delà de ce qui est demandé : pas de fonction,
   d'option ou de section « au cas où », pas d'abstraction pour un usage
   unique. Si 200 lignes peuvent en faire 50, réécrire.
3. **Changements chirurgicaux.** Ne toucher que ce qui est demandé. Ne pas
   « améliorer » le texte, le code ou la mise en forme d'à côté ; garder le
   style existant. Signaler ce qui semble mort ou faux sans le supprimer.
   Retirer seulement ce que ses propres changements ont rendu inutile.
   Test : chaque ligne modifiée se rattache à la demande.
4. **Viser un résultat vérifiable.** Transformer la demande en critère de
   réussite (ex. « corriger le bug » → un test qui le reproduit, puis qui
   passe ; « une légende » → `caption.py` ne signale plus rien). Pour une
   tâche en plusieurs étapes, donner un plan court : étape → vérification.
