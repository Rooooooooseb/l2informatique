import pandas as pd
import joblib # Pourrait servir à sauvegarder le modèle plus tard

# 1. Charger les dernières données de l'IA
df = pd.read_csv("dataset_final_ia.csv", index_col=0, parse_dates=True)
dernier_jour = df.iloc[-1]

# 2. Logique de décision de l'agent (Simulation de l'IA) [Source 12, 50]
prix_actuel = dernier_jour['Close']
prediction = dernier_jour['Predict_Close_Demain']
sentiment = dernier_jour['Sentiment_News']

variation_predite = ((prediction - prix_actuel) / prix_actuel) * 100

print("--- AGENT IA : ANALYSE BOURSIÈRE ---")
print(f"Action : TotalEnergies")
print(f"Prix actuel : {prix_actuel:.2f} €")
print(f"Prédiction pour demain : {prediction:.2f} € ({variation_predite:+.2f}%)")

# 3. Génération de la réponse en langage naturel [Source 49, 52]
print("\n--- RÉPONSE DE L'AGENT ---")
if variation_predite > 0.5 and sentiment > 0:
    print(f"✅ RECOMMANDATION : ACHETER.")
    print(f"L'IA détecte une hausse probable couplée à un sentiment média positif ({sentiment:.2f}).")
elif variation_predite < -0.5:
    print(f"⚠️ RECOMMANDATION : ÉVITER / VENDRE.")
    print("Les indicateurs techniques prévoient une baisse du cours.")
else:
    print(f"👀 RECOMMANDATION : SURVEILLER.")
    print("Le marché semble stable, pas de mouvement majeur détecté.")