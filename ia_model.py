import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

# 1. Charger le dataset final (Source 37, 39)
df = pd.read_csv("dataset_final_ia.csv", index_col=0, parse_dates=True)

# 2. Définition des variables d'entrée (Features) et de la cible (Target)
# On utilise les colonnes que tu as créées à l'étape précédente
features = ['Close', 'Variation', 'Volatilite', 'Sentiment_Tweets', 'Sentiment_News']
X = df[features]
y = df['Predict_Close_Demain']

# 3. Séparation : 80% pour l'entraînement, 20% pour le test final
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# 4. Création et entraînement du modèle Random Forest (Source 42)
print("Entraînement de l'agent IA en cours...")
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Évaluation du modèle (Source 54)
predictions = model.predict(X_test)
erreur = mean_absolute_error(y_test, predictions)

print(f"✅ Modèle IA entraîné avec succès !")
print(f"Erreur moyenne de prédiction : {erreur:.2f} euros")

# 6. Petit aperçu : Comparaison Réel vs Prédit
comparaison = pd.DataFrame({'Réel': y_test, 'Prédit': predictions}, index=y_test.index)
print("\nComparaison des derniers jours :")
print(comparaison.tail())