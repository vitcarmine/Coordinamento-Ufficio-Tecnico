from datetime import date, timedelta
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Agenda Ufficio Tecnico",
    page_icon="📋",
    layout="wide",
)

st.title("📋 Coordinamento Ufficio Tecnico — Cronoprogramma & SAL")

# Se il repo è pubblico puoi usare il raw URL, oppure leggere il file locale in Streamlit Cloud
DATA_URL = st.sidebar.text_input(
    "Percorso o URL RAW del CSV",
    value="dati_lavori.csv",
)

@st.cache_data(ttl=120)
def carica_dati(path_or_url: str) -> pd.DataFrame:
    df = pd.read_csv(path_or_url)
    df["inizio"] = pd.to_datetime(df["inizio"])
    df["scadenza"] = pd.to_datetime(df["scadenza"])
    df["avanzamento"] = pd.to_numeric(df["avanzamento"], errors="coerce").fillna(0)
    return df

try:
    df = carica_dati(DATA_URL)
except Exception as e:
    st.error(f"Impossibile caricare il CSV: {e}")
    st.stop()

# Filtri laterali
st.sidebar.header("Filtri")
stati = st.sidebar.multiselect("Stato", sorted(df["stato"].unique()), default=sorted(df["stato"].unique()))
priorita = st.sidebar.multiselect("Priorità", sorted(df["priorita"].unique()), default=sorted(df["priorita"].unique()))
referenti = st.sidebar.multiselect("Referente", sorted(df["referente"].unique()), default=sorted(df["referente"].unique()))

filtro = df[
    df["stato"].isin(stati)
    & df["priorita"].isin(priorita)
    & df["referente"].isin(referenti)
].copy()

oggi = pd.Timestamp(date.today())
in_7_giorni = oggi + timedelta(days=7)

scadenze_imminenti = filtro[
    (filtro["stato"] != "Completato")
    & (filtro["scadenza"] >= oggi)
    & (filtro["scadenza"] <= in_7_giorni)
]
scadute = filtro[(filtro["stato"] != "Completato") & (filtro["scadenza"] < oggi)]
bloccate = filtro[filtro["stato"] == "Bloccato"]

# KPI
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Attività", len(filtro))
c2.metric("Avanzamento medio", f"{filtro['avanzamento'].mean():.0f}%" if len(filtro) else "0%")
c3.metric("In scadenza (7 gg)", len(scadenze_imminenti))
c4.metric("Scadute", len(scadute))
c5.metric("Bloccate", len(bloccate))

# Gantt / Cronoprogramma
st.subheader("🗓️ Cronoprogramma (Gantt)")
if not filtro.empty:
    fig = px.timeline(
        filtro.sort_values("inizio"),
        x_start="inizio",
        x_end="scadenza",
        y="attivita",
        color="stato",
        hover_data=["id", "wbs", "referente", "avanzamento", "priorita", "note"],
    )
    fig.update_yaxes(autorange="reversed")
    fig.update_layout(height=380, margin=dict(l=10, r=10, t=30, b=10))
    st.plotly_chart(fig, use_container_width=True)

# Tabella dettagliata
st.subheader("📊 Avanzamento Lavori e Scadenze")
tab_view = filtro.copy()
tab_view["inizio"] = tab_view["inizio"].dt.strftime("%Y-%m-%d")
tab_view["scadenza"] = tab_view["scadenza"].dt.strftime("%Y-%m-%d")
st.dataframe(
    tab_view[["id", "wbs", "attivita", "referente", "inizio", "scadenza", "avanzamento", "stato", "priorita", "note"]],
    use_container_width=True,
    hide_index=True,
)
