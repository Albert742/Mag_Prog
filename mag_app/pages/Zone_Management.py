# File: pages/Zone_Management.py
import streamlit as st
import pandas as pd
from MagDBcontroller import connessione, selectSQL

def fetch_zones():
    with connessione() as conn:
        query = "SELECT * FROM Zone"
        return pd.read_sql(query, conn)

st.title("Gestione Zone")
st.sidebar.success("Naviga in un'altra pagina usando il menu.")

try:
    zones = fetch_zones()
    st.write("### Zone")
    st.dataframe(zones)
except Exception as e:
    st.error(f"Errore durante il caricamento delle zone: {e}")

