# FleetMaster — Système de Gestion de Flotte Automobile

> Projet réalisé dans le cadre du module **Développement Python et Frameworks** à l'EMSI.

FleetMaster est une application web ERP centralisée dédiée à la gestion intelligente d'un parc automobile d'entreprise. Elle offre un suivi complet du cycle de vie des véhicules, une gestion des accès par rôles, et un système d'alertes automatisées pour la maintenance préventive.

## Fonctionnalités

* **Authentification & Rôles** : Accès sécurisé avec deux profils distincts (Administrateur / Technicien) via `django.contrib.auth`.
* **Référentiel du parc** : Enregistrement complet des véhicules avec leurs caractéristiques techniques (modèle, marque, carburant, kilométrage, état).
* **Tableau de bord interactif** : Recherche multicritères en temps réel (immatriculation, marque, année, état) et barres de progression kilométrique visuelles.
* **Alertes de Maintenance Automatisées** : Déclenchement dynamique d'un badge "Révision" lorsque le kilométrage dépasse 250 000 km ou que l'âge du véhicule atteint 5 ans.
* **CRUD complet** : Ajout, modification, suppression et consultation des véhicules réservés à l'administrateur.
* **Mise à jour kilométrique rapide** : Interface épurée pour les techniciens de terrain.

## Technologies

* **Backend** : Python 3, Django 4.2
* **Frontend** : Twig, HTML5, Bootstrap 5, Bootstrap Icons
* **Base de données** : MySQL, Doctrine ORM, phpMyAdmin
* **Architecture** : MVT (Modèle-Vue-Template)
* **Modélisation** : UML (StarUML)

## Auteur

Projet réalisé par Hiba Karam — Élève Ingénieure @ EMSI
