# l2informatique

Terminal Expert CAC40 - Analyse IA et Stratégique

I. Présentation du projet
Ce projet consiste en un terminal boursier interactif dédié à l'analyse des 12 principales capitalisations du CAC 40. Il s'appuie sur un système hybride combinant la science des données classique et l'intelligence artificielle générative.

      L'objectif principal est de corréler des données quantitatives (prix et volumes) avec des analyses qualitatives issues du traitement du langage naturel (NLP) afin d'offrir une aide à la décision structurée.
      
      

II. Architecture Technique
Le projet est segmenté en plusieurs modules technologiques complémentaires :

Collecte et Gestion des Données
Utilisation de la bibliothèque yfinance pour l'extraction de 10 ans d'historique boursier.
Génération de fichiers CSV locaux pour assurer l'intégrité et la rapidité d'accès aux jeux de données.
Mise à jour dynamique des cours en temps réel pour l'affichage des indicateurs actuels.
Modélisation et Intelligence Artificielle
Machine Learning : Implémentation d'un algorithme Random Forest Regressor pour l'estimation du prix à J+1.
NLP (VADER) : Calcul automatique d'un score de polarité (-1 à +1) basé sur les actualités financières récentes.
IA Générative (Mistral) : Analyse textuelle avancée pour transformer les flux de NewsAPI en synthèses stratégiques exploitables.
Interface Utilisateur (Dash)
Développement d'un tableau de bord professionnel avec graphiques en chandeliers japonais.
Intégration d'indicateurs de volatilité et de jauges de confiance médiatique.



III. Fonctionnalités principales
      1. Sélecteur d'actifs : Menu déroulant couvrant les entreprises majeures telles qu'Airbus, LVMH ou TotalEnergies.
      2. Indicateurs décisionnels : Affichage du cours actuel (ex: 206,50 € pour Airbus), du score de confiance et de la volatilité hebdomadaire.
      3. Tendance prédictive : Qualification visuelle de la tendance attendue (HAUSSIÈRE / BAISSIÈRE) générée par le modèle prédictif.
      4. Synthèse stratégique : Rédaction automatisée portant sur les seuils de support technique et la fiabilité des projections.
      
      
      

IV. Structure du répertoire
Le dépôt GitHub est organisé de manière modulaire (18 éléments constitutifs) :

      • app_final.py : Script central de l'application Dash et gestion des callbacks.

      • collecte.py : Automatisation de la récupération des données historiques.

      • ia_model.py : Définition et entraînement du modèle Random Forest.

      • traitement_donnees.py : Nettoyage et ingénierie des variables (features).

      • /data : Dossier contenant les bases de données historiques au format CSV.

      

V. Identification
Auteurs :

Samuel Nancy - 44009631
Bakekolo Rose - 44000281
Formation : Licence Économie et Gestion Parcours CMI (TD11)
Date : Janvier 2026



