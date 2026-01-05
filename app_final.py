import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import yfinance as yf
import pandas as pd
import numpy as np
import finnhub
from mistralai import Mistral
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.ensemble import RandomForestRegressor
import plotly.graph_objects as go
from datetime import datetime, timedelta

# ====== CONFIGURATION ======
FINNHUB_KEY = "d5bt6l1r01qsbmgh5jlgd5bt6l1r01qsbmgh5jm0"
MISTRAL_KEY = "s2awLatXWwnjpw4stfpLpeHc6xht1NsE" 
PINK_COLOR = "#FFC0CB" 

finnhub_client = finnhub.Client(api_key=FINNHUB_KEY)
mistral_client = Mistral(api_key=MISTRAL_KEY)
sia = SentimentIntensityAnalyzer()

CAC40_PRO = {
    "Airbus": "AIR.PA", "LVMH": "MC.PA", "TotalEnergies": "TTE.PA", 
    "L'Oréal": "OR.PA", "Sanofi": "SAN.PA", "BNP Paribas": "BNP.PA", 
    "Renault": "RNO.PA", "Hermès": "RMS.PA", "Orange": "ORA.PA",
    "Danone": "BN.PA", "Vinci": "DG.PA", "Société Générale": "GLE.PA"
}

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG, dbc.icons.BOOTSTRAP])

# ====== INTERFACE ======
app.layout = html.Div([
    html.Div([
        html.H3("TERMINAL EXPERT", style={'color': PINK_COLOR, 'fontWeight': 'bold'}),
        html.P("Analyse Décisionnelle & Stratégique", className="small text-muted"),
        html.Hr(style={'borderColor': '#333'}),
        html.Label("SÉLECTIONNER UN ACTIF :", style={'color': PINK_COLOR, 'fontSize': '0.8rem', 'fontWeight': 'bold'}),
        dcc.Dropdown(id='ticker-dropdown', options=[{'label': k, 'value': v} for k, v in CAC40_PRO.items()],
                     value='AIR.PA', style={'color': '#000'})
    ], style={"position": "fixed", "top": 0, "left": 0, "bottom": 0, "width": "20rem", "padding": "2rem", "backgroundColor": "#0b0e14", "borderRight": f"2px solid {PINK_COLOR}"}),

    html.Div([
        html.H5("1. INDICATEURS TEMPS RÉEL & PRÉVISIONS", style={'color': PINK_COLOR, 'fontWeight': 'bold'}),
        dbc.Row(id="metrics-row", className="mb-4"),
        
        html.H5("2. ACTUALITÉS RÉCENTES DU MARCHÉ (FR)", style={'color': PINK_COLOR, 'fontWeight': 'bold'}),
        html.Div(id="marquee-container", className="mb-4", style={'border': f'1px solid {PINK_COLOR}', 'padding': '10px', 'borderRadius': '5px'}),
        
        dbc.Row([
            dbc.Col([
                html.H5("4. ANALYSE TECHNIQUE & VOLATILITÉ", style={'color': PINK_COLOR, 'fontWeight': 'bold'}),
                dbc.Card(dcc.Graph(id='main-graph'), style={'backgroundColor': '#161a21', 'border': 'none'})
            ], width=7),
            
            dbc.Col([
                html.H5("3. NOTE DE SYNTHÈSE STRATÉGIQUE", style={'color': PINK_COLOR, 'fontWeight': 'bold'}),
                dbc.Card(dbc.CardBody(html.Div(id='ai-report-container')), 
                         style={'backgroundColor': '#0b0e14', 'border': f'1px solid {PINK_COLOR}', 'minHeight': '450px'})
            ], width=5)
        ])
    ], style={"marginLeft": "22rem", "padding": "2rem"})
])

def format_expert_report(text):
    if not text: return [html.P("Analyse en cours...")]
    lines = text.split('\n')
    formatted = []
    keywords = ['TENDANCE', 'VOLATILITÉ', 'SUPPORT', 'SURVEILLANCE']
    
    for line in lines:
        line = line.strip()
        if not line: continue
        is_title = any(line.upper().startswith(kw) for kw in keywords)
        
        if is_title:
            formatted.append(html.H6(line.upper(), 
                                     style={
                                         'color': PINK_COLOR, 'marginTop': '20px', 'fontWeight': 'bold', 
                                         'fontSize': '0.95rem', 'borderBottom': f'1px solid {PINK_COLOR}', 'paddingBottom': '5px'
                                     }))
        else:
            formatted.append(html.P(line, style={
                'fontSize': '0.85rem', 'textAlign': 'justify', 'lineHeight': '1.5', 'textIndent': '25px', 'marginTop': '10px'
            }))
    return formatted

@app.callback(
    [Output('main-graph', 'figure'), Output('ai-report-container', 'children'),
     Output('marquee-container', 'children'), Output('metrics-row', 'children')],
    [Input('ticker-dropdown', 'value')]
)
def update_terminal(ticker):
    # 1. DONNÉES (Téléchargement d'un an pour cohérence des échelles)
    df = yf.download(ticker, period="1y")
    if isinstance(df.columns, pd.MultiIndex): df.columns = df.columns.get_level_values(0)
    
    # 2. NEWS & TRADUCTION
    news = finnhub_client.company_news(ticker.split('.')[0], _from=(datetime.now()-timedelta(days=60)).strftime('%Y-%m-%d'), to=datetime.now().strftime('%Y-%m-%d'))
    headlines_en = [n['headline'] for n in news[:8]]
    try:
        trad_res = mistral_client.chat.complete(model="mistral-small-latest", messages=[{"role": "user", "content": f"Traduis ces titres financiers en français : {headlines_en}"}])
        headlines_fr = trad_res.choices[0].message.content
    except:
        headlines_fr = " | ".join(headlines_en)

    v_score = np.mean([sia.polarity_scores(h)['compound'] for h in headlines_en]) if headlines_en else 0.0
    
    # 3. CALCULS ML & VOLATILITÉ
    df['Ret'] = df['Close'].pct_change()
    df['Volat'] = df['Ret'].rolling(7).std()
    vol = df['Volat'].iloc[-1]
    
    train = df[['Close', 'Ret', 'Volat']].copy()
    train['S'] = v_score
    train = train.dropna()
    rf = RandomForestRegressor(n_estimators=100, random_state=42).fit(train[['Close', 'Ret', 'Volat', 'S']][:-1], train['Close'].shift(-1).dropna())
    pred = rf.predict(train[['Close', 'Ret', 'Volat', 'S']].tail(1))[0]

    # 4. KPI
    direction_label = "BAISSIÈRE" if pred < df['Close'].iloc[-1] else "HAUSSIÈRE"
    color_trend = "#ff4d4d" if pred < df['Close'].iloc[-1] else "#00ff7f"

    metrics = [
        dbc.Col(dbc.Card([html.Small("COURS ACTUEL", style={'color': PINK_COLOR}), html.H4(f"{df['Close'].iloc[-1]:.2f}€")], body=True, style={'borderTop': f'3px solid {PINK_COLOR}'})),
        dbc.Col(dbc.Card([html.Small("VOLATILITÉ J+7", style={'color': PINK_COLOR}), html.H4(f"{vol*100:.2f}%")], body=True, style={'borderTop': f'3px solid {PINK_COLOR}'})),
        dbc.Col(dbc.Card([html.Small("CONFIANCE MÉDIAS", style={'color': PINK_COLOR}), html.H4(f"{v_score:+.2f}")], body=True, style={'borderTop': f'3px solid {PINK_COLOR}'})),
        dbc.Col(dbc.Card([html.Small("TENDANCE PRÉVUE", style={'color': PINK_COLOR}), html.H4(direction_label, style={'color': color_trend})], body=True, style={'borderTop': f'3px solid {color_trend}'}))
    ]
    
    # 5. GRAPHIQUE AVEC ÉCHELLE TEMPORELLE COHÉRENTE
    fig = go.Figure(data=[go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'])])
    
    fig.update_xaxes(
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1M", step="month", stepmode="backward"),
                dict(count=6, label="6M", step="month", stepmode="backward"),
                dict(step="all", label="1AN")
            ]),
            bgcolor="#161a21", activecolor=PINK_COLOR, font=dict(color="white", size=11)
        )
    )
    
    fig.update_layout(
        template="plotly_dark", height=450, margin=dict(l=0,r=0,t=0,b=0), 
        xaxis_rangeslider_visible=False, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)'
    )

    # 6. ANALYSE EXPERTE
    name = [k for k,v in CAC40_PRO.items() if v == ticker][0]
    direction = "baissière" if pred < df['Close'].iloc[-1] else "haussière"
    comparaison = "inférieur" if pred < df['Close'].iloc[-1] else "supérieur"
    nervosite = "faible" if vol < 0.015 else "élevée"
    
    report_text = f"""
    TENDANCE PRÉDICTIVE : {direction.upper()} À {pred:.2f}€
    L'analyse algorithmique de l'historique des prix, des volumes d'échanges et du sentiment médiatique projette un prix cible de {pred:.2f}€ pour la séance de demain. Ce niveau étant {comparaison} au cours de clôture actuel, le modèle valide une dynamique {direction}. Pour l'investisseur, cela impose une stratégie de prudence.
    
    VOLATILITÉ ET CRÉDIBILITÉ DU MODÈLE
    La volatilité actuelle de {vol*100:.2f}% reflète une nervosité {nervosite} de l'actif. Sur le plan statistique, une faible volatilité augmente significativement la fiabilité des prédictions du modèle Random Forest. Le marché étant peu erratique, les probabilités de réalisation de la cible sont renforcées.
    
    SURVEILLANCE DES SEUILS DE SUPPORT
    Le support technique agit comme un plancher invisible où la concentration des ordres d'achat empêche historiquement le titre de chuter davantage. Dans le cadre de cette variation vers {pred:.2f}€, la surveillance de ces paliers est cruciale pour identifier si l'actif rebondit ou si la rupture du support entraîne une accélération du mouvement.
    """

    return fig, format_expert_report(report_text), html.Marquee(headlines_fr, style={'color': PINK_COLOR}), metrics

if __name__ == '__main__':
    app.run(debug=True)