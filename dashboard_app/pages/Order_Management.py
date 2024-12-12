# File: pages/Order_Management.py
import sys
import os

# Add the parent directory of the current script to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


import streamlit as st
import pandas as pd
from utils.MagDBcontroller import connessione, selectSQL, add_record

# Authentication Check
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("Unauthorized access. Please log in first.")
    st.stop()


def fetch_orders():
    with connessione() as conn:
        query = "SELECT * FROM Ordini"
        return pd.read_sql(query, conn)

st.title("Gestione Ordini")
st.sidebar.success("Naviga in un altra pagina del menu.")

# Logout Button
if st.sidebar.button("Log Out"):
    st.session_state.clear()
    st.rerun()

st.write("### Ordini Esistenti")
try:
    orders = fetch_orders()
    st.dataframe(orders)
except Exception as e:
    st.error(f"Errore durante il caricamento degli ordini: {e}")

st.write("### Crea un Nuovo Ordine")
order_type = st.selectbox("Tipo di Ordine", ["Entrata", "Uscita"])
stato = st.selectbox("Stato dell Ordine", ["In elaborazione", "Spedito", "Concluso"])
if st.button("Crea Ordine"):
    try:
        with connessione() as conn:
            add_record(conn, "Ordini", ["Tipo", "Stato"], [order_type, stato])
            st.success("Ordine creato con successo!")
    except Exception as e:
        st.error(f"Impossibile creare l ordine: {e}")

