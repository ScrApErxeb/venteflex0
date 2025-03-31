# Projet VenteFlex

## Aperçu
VenteFlex est une application web basée sur Django, conçue pour fournir une plateforme flexible de gestion des ventes, des stocks, du personnel et de la comptabilité. Ce projet vise à simplifier les processus de gestion et à améliorer l'expérience utilisateur grâce à un backend robuste et une interface intuitive.

## Installation

Pour configurer le projet, suivez ces étapes :

1. **Cloner le dépôt :**
   ```
   git clone <repository-url>
   cd venteflex
   ```

2. **Créer un environnement virtuel :**
   ```
   python -m venv venv
   source venv/bin/activate  # Sur Windows utilisez `venv\Scripts\activate`
   ```

3. **Installer les dépendances :**
   ```
   pip install -r requirements.txt
   ```

4. **Appliquer les migrations :**
   ```
   python manage.py migrate
   ```

5. **Démarrer le serveur de développement :**
   ```
   python manage.py runserver
   ```

## Applications

Le projet est organisé en plusieurs applications pour une meilleure modularité :

- **personnel** : Gère les informations sur les employés, les rôles et les permissions.
- **vente** : Gère les processus de vente, les clients et les catalogues de produits.
- **compta** : Gère les finances, les factures et les rapports comptables.
- **stock** : Suit les niveaux de stock, les mouvements de stock et la gestion des entrepôts.

## Utilisation

Une fois le serveur démarré, vous pouvez accéder à l'application à l'adresse `http://127.0.0.1:8000/`. Vous pourrez créer, lire, mettre à jour et supprimer des enregistrements liés aux ventes, aux stocks, au personnel et à la comptabilité via les interfaces fournies.

## Contribution

Les contributions sont les bienvenues ! Veuillez forker le dépôt et soumettre une pull request pour toute amélioration ou correction de bug.

## Licence

Ce projet est sous licence MIT. Consultez le fichier LICENSE pour plus de détails.