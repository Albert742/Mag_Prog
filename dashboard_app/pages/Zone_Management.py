# File: pages/Zone_Management.py
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


def fetch_zones():
    with connessione() as conn:
        query = "SELECT * FROM Zone"
        return pd.read_sql(query, conn)

st.title("Gestione Zone")
st.sidebar.success("Naviga in un'altra pagina usando il menu.")

# Logout Button
if st.sidebar.button("Log Out"):
    st.session_state.clear()
    st.rerun()
try:
    zones = fetch_zones()
    st.write("### Zone")
    st.dataframe(zones)
except Exception as e:
    st.error(f"Errore durante il caricamento delle zone: {e}")

