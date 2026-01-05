# l2informatique

## 📊 Terminal Expert CAC40 – Analyse IA & Stratégique

---

## I. Présentation du projet

Ce projet consiste en un **terminal boursier interactif** dédié à l’analyse des principales capitalisations du **CAC 40**.  
Il repose sur une **approche hybride** combinant :

- **Méthodes classiques de science des données**
- **Modèles de Machine Learning**
- **Analyse du langage naturel (NLP)**
- **IA générative utilisée uniquement comme outil d’interprétation**

🎯 **Objectif principal**  
Corréler des **données quantitatives de marché** (prix, rendements, volatilité) avec des **signaux informationnels issus de l’actualité financière**, afin de fournir une **aide à la décision structurée, explicable et non hallucinatoire**.

Le projet ne vise pas à produire des recommandations automatiques, mais à **éclairer la prise de décision** à partir de données objectives.

---

## II. Architecture technique

Le système est conçu de manière **modulaire**, chaque composant ayant un rôle bien défini.

### 1️⃣ Collecte et gestion des données

- **yfinance**
  - Extraction de l’historique boursier (jusqu’à 10 ans)
  - Données OHLC, volumes, rendements
- **Stockage local**
  - Génération de fichiers CSV
  - Garantit la reproductibilité et la rapidité d’accès
- **Mise à jour dynamique**
  - Actualisation des cours pour l’affichage temps réel des indicateurs

---

### 2️⃣ Modélisation & Intelligence Artificielle

#### 🔹 Machine Learning (cœur du système)
- Algorithme : **Random Forest**
- Objectif :
  - Estimation du prix à **J+1**
  - Qualification de la **tendance attendue**
- Utilisation de features quantitatives et informationnelles combinées

#### 🔹 NLP – Analyse de sentiment
- Méthode : **VADER**
- Application :
  - Analyse des titres d’actualités financières
  - Calcul d’un score de polarité normalisé (-1 à +1)
- Pondération temporelle pour privilégier les news récentes

#### 🔹 IA générative (Mistral)
⚠️ L’IA générative **n’est pas décisionnelle**.

- Rôle :
  - Interpréter les résultats du modèle ML
  - Générer une **synthèse stratégique lisible**
- Contraintes strictes :
  - Aucune connaissance externe
  - Analyse uniquement basée sur les données fournies

---

### 3️⃣ Interface utilisateur (Dash)

- Tableau de bord interactif développé avec **Dash**
- Visualisations :
  - Graphiques en chandeliers japonais
  - Indicateurs de volatilité
  - Scores de sentiment
- Interface pensée pour une lecture **claire et professionnelle**

---

## III. Fonctionnalités principales

1. **Sélecteur d’actifs**
   - Menu déroulant couvrant plusieurs entreprises majeures du CAC 40
   - Exemple : Airbus, LVMH, TotalEnergies

2. **Indicateurs décisionnels**
   - Cours actuel
   - Score de sentiment informationnel
   - Volatilité hebdomadaire

3. **Tendance prédictive**
   - Estimation issue du modèle de Machine Learning
   - Indication visuelle :  
     **HAUSSIÈRE / NEUTRE / BAISSIÈRE**

4. **Synthèse stratégique**
   - Analyse automatisée et contextualisée
   - Mise en perspective des signaux quantitatifs et informationnels
   - Évaluation de la fiabilité des projections

---

## IV. Structure du répertoire

Le dépôt GitHub est organisé de manière modulaire :





