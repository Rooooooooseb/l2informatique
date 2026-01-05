Terminal Expert CAC40
Description du projet
Ce projet est un terminal boursier interactif destiné à l’analyse d’actions du CAC 40. Il combine :

Visualisation des prix historiques avec chandeliers japonais.
Calcul d’indicateurs financiers simples (rendements, volatilité).
Analyse de sentiment à partir des titres financiers récents.
Modèle de prédiction à court terme (Random Forest Regressor) pour estimer le prix de clôture à J+1.
Génération d’une analyse textuelle synthétique via l’IA (Mistral) pour contextualiser les résultats.
L’objectif est de fournir une aide à la lecture des marchés, sans prétendre remplacer une analyse humaine ou donner des conseils financiers.

Fonctionnalités principales
Sélection d’un actif du CAC 40 via un menu déroulant.
Affichage d’un graphique interactif avec chandeliers japonais et sélecteur de période (1 mois, 6 mois, 1 an).
Affichage d’indicateurs clés :
Cours actuel
Volatilité sur 7 jours
Score de sentiment médiatique
Tendance prédite (haussière / baissière)
Marquee affichant les dernières actualités financières traduites en français.
Analyse textuelle synthétique des résultats, générée par Mistral.
Technologies utilisées
Python 3.10+
Dash + Dash Bootstrap Components
Plotly Graph Objects
yfinance
Finnhub API
Mistral AI
NLTK – VADER
Scikit-learn
Installation
Cloner le dépôt :
git clone <URL_DU_DEPOT>
cd <NOM_DU_DEPOT>
Créer un environnement virtuel :
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
Installer les dépendances :
pip install -r requirements.txt
Le fichier requirements.txt doit contenir toutes les bibliothèques : dash, dash-bootstrap-components, yfinance, finnhub-python, mistralai, nltk, scikit-learn, plotly, etc.

Télécharger les données nécessaires pour NLTK (VADER) :
import nltk
nltk.download('vader_lexicon')
Ajouter vos clés d’API dans le fichier config.py ou directement dans le code :
FINNHUB_KEY = "<votre_cle_finnhub>"
MISTRAL_KEY = "<votre_cle_mistral>"
Lancement de l’application
python app_final.py
L’application s’exécute localement sur http://127.0.0.1:8050/
L’interface permet de choisir un actif et de visualiser les indicateurs et l’analyse.
Structure du projet
/terminal-expert
│
├─ app.py               # Script principal contenant l’application Dash
├─ requirements.txt     # Dépendances Python
├─ README.md
├─ config.py            # Fichier pour les clés d’API
├─ /assets              # Fichiers CSS ou images (optionnel)
└─ /data                # Données téléchargées ou fichiers CSV (optionnel)
Limites
Les prédictions du modèle sont à court terme (J+1) et indicatives. Elles ne doivent pas être interprétées comme des recommandations financières.
Les scores de sentiment dépendent du volume et de la qualité des articles disponibles.
Les performances de l’application peuvent être impactées par le temps de réponse des API externes.
[Samuel Nancy - 44009631]
[Bakekolo Rose - 44000281] Licence: [Licence Économie et Gestion Parcours CMI ( TD7)]
