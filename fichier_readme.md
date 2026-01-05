# Terminal Expert CAC40

## Description du projet

Ce projet est un terminal boursier interactif destiné à l’analyse d’actions du CAC 40. Il combine :

- Visualisation des prix historiques avec chandeliers japonais.
- Calcul d’indicateurs financiers simples (rendements, volatilité).
- Analyse de sentiment à partir des titres financiers récents.
- Modèle de prédiction à court terme (Random Forest Regressor) pour estimer le prix de clôture à J+1.
- Génération d’une analyse textuelle synthétique via l’IA (Mistral) pour contextualiser les résultats.

L’objectif est de fournir une **aide à la lecture des marchés**, sans prétendre remplacer une analyse humaine ou donner des conseils financiers.

---

## Fonctionnalités principales

1. Sélection d’un actif du CAC 40 via un menu déroulant.
2. Affichage d’un graphique interactif avec chandeliers japonais et sélecteur de période (1 mois, 6 mois, 1 an).
3. Affichage d’indicateurs clés :
   - Cours actuel
   - Volatilité sur 7 jours
   - Score de sentiment médiatique
   - Tendance prédite (haussière / baissière)
4. Marquee affichant les dernières actualités financières traduites en français.
5. Analyse textuelle synthétique des résultats, générée par Mistral.

---

## Technologies utilisées

- **Python 3.10+**
- [Dash](https://dash.plotly.com/) + [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/)
- [Plotly Graph Objects](https://plotly.com/python/graph-objects/)
- [yfinance](https://pypi.org/project/yfinance/)
- [Finnhub API](https://finnhub.io/)
- [Mistral AI](https://mistral.ai/)
- [NLTK – VADER](https://www.nltk.org/)
- [Scikit-learn](https://scikit-learn.org/stable/)

---

## Installation

1. Cloner le dépôt :

```bash
git clone <URL_DU_DEPOT>
cd <NOM_DU_DEPOT>
```

2. Créer un environnement virtuel :

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

3. Installer les dépendances :

```bash
pip install -r requirements.txt
```

> Le fichier `requirements.txt` doit contenir toutes les bibliothèques : `dash`, `dash-bootstrap-components`, `yfinance`, `finnhub-python`, `mistralai`, `nltk`, `scikit-learn`, `plotly`, etc.

4. Télécharger les données nécessaires pour NLTK (VADER) :

```python
import nltk
nltk.download('vader_lexicon')
```

5. Ajouter vos clés d’API dans le fichier `config.py` ou directement dans le code :

```python
FINNHUB_KEY = "<votre_cle_finnhub>"
MISTRAL_KEY = "<votre_cle_mistral>"
```

---

## Lancement de l’application

```bash
python app_final.py
```

- L’application s’exécute localement sur `http://127.0.0.1:8050/`
- L’interface permet de choisir un actif et de visualiser les indicateurs et l’analyse.

---

## Structure du projet

```
/terminal-expert
│
├─ app.py               # Script principal contenant l’application Dash
├─ requirements.txt     # Dépendances Python
├─ README.md
├─ config.py            # Fichier pour les clés d’API
├─ /assets              # Fichiers CSS ou images (optionnel)
└─ /data                # Données téléchargées ou fichiers CSV (optionnel)
```

---

## Limites

- Les prédictions du modèle sont à court terme (J+1) et indicatives. Elles ne doivent pas être interprétées comme des recommandations financières.
- Les scores de sentiment dépendent du volume et de la qualité des articles disponibles.
- Les performances de l’application peuvent être impactées par le temps de réponse des API externes.

---



[Samuel Nancy - 44009631]  
[Bakekolo Rose - 44000281]
Licence: [Licence Économie et Gestion Parcours CMI ( TD7)]  


