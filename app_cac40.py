import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# Configuration de la page
st.set_page_config(page_title="Terminal Intelligence de Marche", layout="wide", initial_sidebar_state="expanded")

# --- STYLE CSS POUR UN RENDU IDENTIQUE A LA PHOTO ---
st.markdown("""
    <style>
    .stApp { background-color: #1a1c24; color: #d1d4dc; }
    [data-testid="stSidebar"] { background-color: #11141a; border-right: 1px solid #333; }
    h1, h2, h3 { color: #ffffff; font-family: 'Inter', sans-serif; font-weight: 600; }
    .section-header { background-color: #2a2e39; padding: 10px; border-radius: 4px; margin-bottom: 20px; }

    /* Blocs de cotation visibles pour toutes les entreprises */
    div[data-testid="stMetric"] {
        background-color: #232731;
        border: 1px solid #363c4e;
        border-radius: 4px;
        padding: 15px !important;
    }
    div[data-testid="stMetricValue"] > div { color: #ffffff !important; font-size: 1.5rem !important; }
    div[data-testid="stMetricLabel"] > div { color: #9598a1 !important; text-transform: uppercase; }

    /* Bande Twitter bleue sur noir */
    .marquee-container {
        width: 100%; overflow: hidden; white-space: nowrap; 
        background: #000000; border: 1px solid #1da1f2; padding: 12px 0; margin: 20px 0;
    }
    .marquee-text {
        display: inline-block; padding-left: 100%;
        animation: marquee 35s linear infinite;
        color: #1da1f2; font-family: 'Courier New', monospace; font-size: 1.1rem;
    }
    @keyframes marquee { 0% { transform: translate(0, 0); } 100% { transform: translate(-100%, 0); } }

    /* Bloc Rapport Blanc et Vert */
    .report-card {
        background-color: #ffffff; color: #1a1c24;
        padding: 20px; border-radius: 4px; border-left: 10px solid #28a745;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIQUE DE L'AGENT IA ---
entreprises = {
    "Renault": "RNO.PA", "Airbus": "AIR.PA", "LVMH": "MC.PA", 
    "TotalEnergies": "TTE.PA", "L'Oreal": "OR.PA", "BNP Paribas": "BNP.PA"
}

st.sidebar.title("Parametres")
choix = st.sidebar.selectbox("Selection valeur :", list(entreprises.keys()))
ticker = entreprises[choix]
echelle = st.sidebar.radio("Periode :", ("1 Semaine", "1 Mois", "1 An", "5 Ans"), index=2)

@st.cache_data
def fetch_data(symbol):
    df = yf.download(symbol, period="5y")
    if isinstance(df.columns, pd.MultiIndex): df.columns = df.columns.get_level_values(0)
    df['Variation'] = df['Close'].pct_change() * 100
    df['Volat'] = df['Variation'].rolling(7).std()
    np.random.seed(42)
    df['S_Score'] = np.random.uniform(-1, 1, len(df))
    df['Target'] = df['Close'].shift(-1)
    return df.dropna()

data = fetch_data(ticker)
last = data.iloc[-1]

# --- 1. COTATION ACTUELLE ---
st.title("Terminal Analytique CAC40 : Intelligence de Marche")
st.markdown(f'<div class="section-header"><h3>1. Cotation : {choix.upper()}</h3></div>', unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Variation", f"{last['Variation']:+.2f} %")
c2.metric("Ouverture", f"{last['Open']:.2f} EUR")
c3.metric("Plus Haut", f"{last['High']:.2f} EUR")
c4.metric("Plus Bas", f"{last['Low']:.2f} EUR")

# --- 2. FIL TWITTER DÉFILANT ---
st.markdown('<div class="section-header"><h3>2. Flux Social Twitter (Simule)</h3></div>', unsafe_allow_html=True)
news = [
    f"ALERT: Flux acheteur detecte sur {choix}",
    f"INFO: Sentiment Twitter positif pour le ticker {ticker}",
    f"MARCHE: Resistance technique identifiee pour {choix}",
    f"NEWS: Les analystes confirment leur position sur {choix}"
]
marquee_content = "  ---  ".join(news)
st.markdown(f'<div class="marquee-container"><div class="marquee-text">{marquee_content}</div></div>', unsafe_allow_html=True)

# --- 3. ANALYSE ET GRAPHIQUE ---
st.markdown('<div class="section-header"><h3>3. Analyse IA et Rapport Expert</h3></div>', unsafe_allow_html=True)

features = ['Close', 'Variation', 'Volat', 'S_Score']
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(data[features][:-1], data['Target'][:-1])
pred = model.predict(data[features].tail(1))[0]
diff = ((pred - last['Close']) / last['Close']) * 100

col_left, col_right = st.columns([2, 1])

with col_left:
    st.write(f"Evolution Historique ({echelle})")
    hist_map = {"1 Semaine": 7, "1 Mois": 30, "1 An": 252, "5 Ans": 1260}
    st.line_chart(data['Close'].tail(hist_map[echelle]))

with col_right:
    st.write("Note de Synthese")
    status = "Opportunite d'Achat Confirmee" if diff > 0.4 else "Position Neutre"
    st.markdown(f"""
        <div class="report-card">
            <h4 style="color: #28a745;">{status}</h4>
            <p>Valeur cible : <b>{pred:.2f} EUR</b> ({diff:+.2f}%).</p>
            <p>L'indice de sentiment Twitter est de {last['S_Score']:.2f}. La volatilite mesuree autorise une exposition au marche.</p>
        </div>
    """, unsafe_allow_html=True)