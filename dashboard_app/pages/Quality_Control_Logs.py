# File: pages/Quality_Control_Logs.py
import sys
import os

# Add the parent directory of the current script to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import streamlit as st
import pandas as pd
from utils.MagDBcontroller import connessione, selectSQL

# Authentication Check
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("Unauthorized access. Please log in first.")
    st.stop()

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

# Logout Button
if st.sidebar.button("Log Out"):
    st.session_state.clear()
    st.rerun()
    
try:
    logs = fetch_quality_logs()
    st.write("### Registri Controllo Qualità")
    st.dataframe(logs)
except Exception as e:
    st.error(f"Errore durante il caricamento dei registri: {e}")

