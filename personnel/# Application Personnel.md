# Application Personnel

## Description
L'application **personnel** gère les informations relatives aux employés et aux postes dans l'organisation. Elle permet de suivre les employés, leurs rôles et leurs informations professionnelles.

## Modèles

### 1. Poste
Représente un poste ou un rôle dans l'organisation.

- **Champs :**
  - `nom` : Nom du poste (unique).
  - `description` : Description du poste (facultatif).

- **Méthodes :**
  - `__str__` : Retourne le nom du poste.

### 2. Employe
Représente un employé de l'organisation.

- **Champs :**
  - `nom` : Nom de l'employé.
  - `prenom` : Prénom de l'employé.
  - `poste` : Référence au modèle `Poste` (relation `ForeignKey`).
  - `date_embauche` : Date d'embauche de l'employé.
  - `salaire` : Salaire de l'employé.

- **Méthodes :**
  - `__str__` : Retourne le prénom et le nom de l'employé.

## Administration
Les modèles **Poste** et **Employe** sont enregistrés dans l'interface d'administration Django, permettant une gestion facile des données.

## Fonctionnalités
- Ajouter, modifier et supprimer des employés.
- Ajouter, modifier et supprimer des postes.
- Associer chaque employé à un poste spécifique.

## Relations
- Un **Poste** peut être associé à plusieurs **Employes**.
- Chaque **Employe** est lié à un seul **Poste**.

## Exemple d'utilisation
- Créer des postes comme "Développeur", "Manager", "Comptable".
- Ajouter des employés et les associer à leurs postes respectifs.