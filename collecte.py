import yfinance as yf
import pandas as pd

# On définit les 12 entreprises majeures du CAC40 pour le projet
entreprises = {
    "TotalEnergies": "TTE.PA",
    "Renault": "RNO.PA",
    "Airbus": "AIR.PA",
    "LVMH": "MC.PA",
    "L'Oreal": "OR.PA",
    "Hermes": "RMS.PA",
    "BNP_Paribas": "BNP.PA",
    "Sanofi": "SAN.PA",
    "AXA": "CS.PA",
    "Schneider_Electric": "SU.PA",
    "Air_Liquide": "AI.PA",
    "Safran": "SAF.PA"
}

print("🚀 Lancement de la collecte globale des données (12 entreprises)...")

for nom, ticker in entreprises.items():
    # Collecte de 10 ans de données pour garantir la précision du Random Forest
    data = yf.download(ticker, start="2015-01-01", end="2025-12-31")
    
    if not data.empty:
        # Sauvegarde en CSV pour l'historique local
        filename = f"donnees_{nom}.csv"
        data.to_csv(filename)
        print(f"✅ Fichier créé : {filename} ({len(data)} lignes)")
    else:
        print(f"❌ Erreur pour {nom} : Aucune donnée trouvée.")

print("\n✨ Collecte terminée ! Votre base de données est prête pour GitHub.")
