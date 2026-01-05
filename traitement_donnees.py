import pandas as pd
import numpy as np

# 1. Charger les données en sautant la ligne d'en-tête superflue si nécessaire
# On charge le fichier normalement
df = pd.read_csv("donnees_TotalEnergies.csv", index_col=0, parse_dates=True)

# Nettoyage : On s'assure que 'Close' est bien numérique et on supprime les erreurs
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

# 2. Calcul des variables techniques [Source 28]
# Calcul de la variation (pct_change) sans utiliser la méthode 'pad' obsolète
df['Variation'] = df['Close'].ffill().pct_change() * 100
# Volatilité sur 7 jours [Source 28]
df['Volatilite'] = df['Variation'].rolling(window=7).std()

# 3. Création des variables de Sentiment (Simulation NLP) [Source 10, 32, 35]
np.random.seed(42)
df['Sentiment_Tweets'] = np.random.uniform(-1, 1, size=len(df))
df['Sentiment_News'] = np.random.uniform(-0.5, 0.8, size=len(df))

# 4. Définition de la CIBLE (Predict Close+1) [Source 38]
df['Predict_Close_Demain'] = df['Close'].shift(-1)

# 5. Nettoyage final des valeurs vides
df.dropna(inplace=True)

# Affichage du résultat pour vérification [Source 37]
print("✅ Dataset corrigé et prêt !")
print(df[['Close', 'Variation', 'Sentiment_Tweets', 'Predict_Close_Demain']].head())

# Sauvegarde
df.to_csv("dataset_final_ia.csv")