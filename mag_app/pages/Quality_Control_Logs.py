# File: pages/Quality_Control_Logs.py
import streamlit as st
import pandas as pd
from MagDBcontroller import connessione, selectSQL

def fetch_quality_logs():
    with connessione() as conn:
        query = """
        SELECT ControlloQualitaMovimenti.ID_Controllo, RichiesteMovimento.ID_Richiesta, 
               ControlloQualitaMovimenti.Esito, ControlloQualitaMovimenti.Note
        FROM ControlloQualitaMovimenti
        JOIN RichiesteMovimento ON ControlloQualitaMovimenti.ID_Richiesta = RichiesteMovimento.ID_Richiesta
        """
        return pd.read_sql(query, conn)

st.title("Registri Controllo Qualità")
st.sidebar.success("Naviga ad altra pagina utilizzando il menu.")

try:
    logs = fetch_quality_logs()
    st.write("### Registri Controllo Qualità")
    st.dataframe(logs)
except Exception as e:
    st.error(f"Errore durante il caricamento dei registri: {e}")

