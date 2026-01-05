import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# 1. Charger les données
df = pd.read_csv("dataset_final_ia.csv", index_col=0, parse_dates=True)
features = ['Close', 'Variation', 'Volatilite', 'Sentiment_Tweets', 'Sentiment_News']
X = df[features]
y = df['Predict_Close_Demain']

# 2. Ré-entraîner rapidement pour l'analyse
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
preds = model.predict(X_test)

# --- GRAPHIQUE 1 : Courbe Réelle vs Prédite ---
plt.figure(figsize=(12, 6))
plt.plot(y_test.index[-50:], y_test.values[-50:], label="Prix Réel", color='blue', linewidth=2)
plt.plot(y_test.index[-50:], preds[-50:], label="Prédiction IA", color='orange', linestyle='--')
plt.title("TotalEnergies : Prix Réel vs Prédiction de l'Agent IA (50 derniers jours)")
plt.legend()
plt.savefig("courbe_prediction.png") # Sauvegarde pour ton rapport
plt.show()

# --- GRAPHIQUE 2 : Importance des variables ---
importances = pd.Series(model.feature_importances_, index=features).sort_values(ascending=False)
plt.figure(figsize=(10, 5))
sns.barplot(x=importances.values, y=importances.index, palette="viridis")
plt.title("Quelles variables influencent le plus l'IA ?")
plt.xlabel("Score d'importance")
plt.savefig("importance_variables.png")
plt.show()