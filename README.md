Terminal Expert CAC40
I. Description du projet
Ce projet est un terminal boursier interactif destiné à l’analyse des actions du CAC 40. Il combine plusieurs approches pour offrir une vision complète du marché :

Visualisation des prix : Affichage historique avec chandeliers japonais (Candlesticks).

Indicateurs financiers : Calcul automatique des rendements et de la volatilité.

Analyse de sentiment : Évaluation à partir des titres financiers récents via NLTK – VADER.

Machine Learning : Modèle de prédiction à court terme (Random Forest Regressor) pour estimer le prix de clôture à J+1.

Intelligence Artificielle : Génération d’une analyse textuelle synthétique via Mistral AI pour contextualiser les résultats.

      Note : L’objectif est de fournir une aide à la lecture des marchés sans prétendre remplacer une analyse humaine ou donner des conseils financiers.

II. Fonctionnalités principales
      1. Sélection d'actif : Menu déroulant permettant de choisir une action parmi les entreprises majeures du CAC 40.       2. Graphique interactif : Visualisation en chandeliers avec sélecteur de période (1 mois, 6 mois, 1 an).       3. Indicateurs clés :          • Cours actuel (ex: 206,50 € pour Airbus).          • Volatilité sur 7 jours (ex: 1,12%).          • Score de sentiment médiatique.          • Tendance prédite (Haussière / Baissière).       4. Actualités : Marquee affichant les dernières news financières traduites en français.       5. Note de synthèse : Analyse textuelle dynamique générée par Mistral AI.

III. Technologies utilisées
Langage : Python 3.10+

Interface : Dash & Dash Bootstrap Components

Graphiques : Plotly Graph Objects

Données : yfinance & Finnhub API

Intelligence Artificielle : Mistral AI

Analyse NLP : NLTK – VADER

Machine Learning : Scikit-learn (Random Forest)

IV. Installation
1. Cloner le dépôt
Bash

git clone <URL_DU_DEPOT>
cd <NOM_DU_DEPOT>
2. Créer un environnement virtuel
Bash

# Linux / Mac
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
3. Installer les dépendances
Bash

pip install -r requirements.txt
Le fichier requirements.txt contient : dash, dash-bootstrap-components, yfinance, finnhub-python, mistralai, nltk, scikit-learn, plotly.

4. Télécharger les ressources NLTK
Python

import nltk
nltk.download('vader_lexicon')
5. Configurer les clés API
Ajoutez vos clés dans config.py ou directement dans app_final.py :

Python

FINNHUB_KEY = "<votre_cle_finnhub>"
MISTRAL_KEY = "<votre_cle_mistral>"
V. Lancement de l’application
Bash

python app_final.py
L’application s’exécute localement sur : http://127.0.0.1:8050/

VI. Structure du projet
Le projet est organisé de manière modulaire (18 éléments constitutifs) :

/terminal-expert
│
├─ app_final.py        # Script principal contenant l’application Dash
├─ requirements.txt    # Liste des dépendances Python
├─ README.md           # Documentation du projet
├─ config.py           # Configuration des clés d'accès API
├─ /assets             # Styles CSS et ressources graphiques
└─ /data               # Données historiques au format CSV
VII. Limites
Les prédictions du modèle sont à court terme (J+1) et purement indicatives.

Les scores de sentiment dépendent de la qualité et du volume des articles fournis par l'API.

Les performances peuvent varier selon le temps de réponse des API externes (Mistral, Finnhub).

Identification
Auteurs :

Samuel Nancy - 44009631

Bakekolo Rose - 44000281

Formation : Licence Économie et Gestion Parcours CMI (TD7) Janvier 2026
