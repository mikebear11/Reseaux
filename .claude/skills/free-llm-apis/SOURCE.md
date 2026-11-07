# Origine de ce skill

- Source : https://github.com/mnfst/awesome-free-llm-apis (dossier `free-llm-apis/`)
- Commit copié : `095e35e10f33d7ba32ebb86e1dd0ff604dea9c1a` (04/11/2026), copie du 07/11/2026
- Licence : CC0 1.0 (domaine public), texte dans `LICENSE`
- Fichiers copiés sans modification : `SKILL.md`, `references/`

## Mise à jour

Les offres gratuites changent souvent (modèles retirés, limites revues). Avant de
s'appuyer sur une limite, vérifier la doc du fournisseur. Pour rafraîchir la copie :
recloner le dépôt source et remplacer `SKILL.md` et `references/`.

## Points d'attention pour la Brasserie de Sulauze (d'après la source elle-même)

1. **Usage commercial** : l'offre gratuite de Cohere est « Non-commercial use only ».
   À exclure pour la brasserie.
2. **Données** : en offre gratuite, Mistral (sauf refus explicite), OpenRouter et Kilo
   peuvent utiliser les textes envoyés pour entraîner leurs modèles. Ne pas y envoyer
   de données clients ou confidentielles.
3. **Gemini en Europe** : les conditions de Google imposent les services payants si
   on met un outil à disposition d'utilisateurs dans l'EEE, en Suisse ou au Royaume-Uni.
4. **Règles du dépôt** : un texte produit par ces modèles reste soumis aux règles de
   `CLAUDE.md` (message sanitaire Loi Évin, jamais « bio », rien d'inventé) et doit
   passer par `caption.py` avant toute publication.
5. **Clés d'API** : jamais dans le dépôt. Variables d'environnement ou secrets
   de l'environnement cloud uniquement.
