Terminal Expert CAC40
I. Description du projet

Ce projet est un terminal boursier interactif destiné à l’analyse des actions du CAC 40.
Il combine plusieurs approches complémentaires afin d’offrir une vision globale et structurée des marchés financiers :

Visualisation des prix :
Affichage de l’historique des cours sous forme de chandeliers japonais (Candlesticks).

Indicateurs financiers :
Calcul automatique des rendements et de la volatilité à partir des données de marché.

Analyse de sentiment :
Évaluation du sentiment médiatique à partir des titres financiers récents grâce à NLTK – VADER.

Machine Learning :
Modèle de prédiction à court terme basé sur un Random Forest Regressor, utilisé pour estimer le prix de clôture à J+1.

Intelligence Artificielle :
Génération d’une analyse textuelle synthétique via Mistral AI, permettant de contextualiser les résultats quantitatifs.

Note :
L’objectif du projet est de fournir une aide à la lecture des marchés financiers.
Il ne prétend ni remplacer une analyse humaine, ni fournir des conseils en investissement.

II. Fonctionnalités principales
Sélection d’actif

Menu déroulant permettant de choisir une action parmi les entreprises majeures du CAC 40.

Graphique interactif

Visualisation en chandeliers japonais avec sélecteur de période :

1 mois

6 mois

1 an

Indicateurs clés

Cours actuel (exemple : 206,50 € pour Airbus)

Volatilité sur 7 jours (exemple : 1,12 %)

Score de sentiment médiatique

Tendance prédite (Haussière / Baissière)

Actualités

Bandeau défilant affichant les dernières actualités financières

Traduction automatique en français

Note de synthèse

Analyse textuelle dynamique générée par Mistral AI

Mise en perspective des indicateurs financiers et du sentiment médiatique

III. Technologies utilisées

Langage : Python 3.10+

Interface : Dash, Dash Bootstrap Components

Graphiques : Plotly Graph Objects

Données financières : yfinance, Finnhub API

Intelligence Artificielle : Mistral AI

Analyse NLP : NLTK – VADER

Machine Learning : Scikit-learn (Random Forest)

IV. Installation
1. Cloner le dépôt
git clone <URL_DU_DEPOT>
cd <NOM_DU_DEPOT>

2. Créer un environnement virtuel
# Linux / Mac
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate

3. Installer les dépendances
pip install -r requirements.txt


Le fichier requirements.txt contient notamment :

dash

dash-bootstrap-components

yfinance

finnhub-python

mistralai

nltk

scikit-learn

plotly

4. Télécharger les ressources NLTK
import nltk
nltk.download('vader_lexicon')

5. Configurer les clés API

Les clés API sont directement renseignées dans le fichier app_final.py (lignes 17–18) :

FINNHUB_KEY = "<votre_cle_finnhub>"
MISTRAL_KEY = "<votre_cle_mistral>"

V. Lancement de l’application
python app_final.py


L’application s’exécute localement à l’adresse suivante :
👉 http://127.0.0.1:8050/

VI. Structure du projet

Le projet est organisé de manière modulaire :

/l2informatique
│
├─ app_final.py        # Application Dash (Interface et Prédictions)
├─ ia_model.py         # Script d'entraînement du modèle Random Forest
├─ collecte.py         # Script de récupération des données via API
├─ requirements.txt    # Liste des dépendances Python
├─ README.md           # Documentation officielle
├─ /assets             # Images du rapport et ressources graphiques
└─ /data               # Répertoire des fichiers CSV (Données historiques et dataset final)


⚠️ Le programme recherche les fichiers de données exclusivement dans le dossier /data.

Identification

Auteurs :

Samuel Nancy – 44009631

Bakekolo Rose – 44000281

Formation :
Licence Économie et Gestion – Parcours CMI (TD11)


