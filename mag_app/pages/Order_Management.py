# File: pages/Order_Management.py
import streamlit as st
import pandas as pd
from MagDBcontroller import connessione, selectSQL, add_record

def fetch_orders():
    with connessione() as conn:
        query = "SELECT * FROM Ordini"
        return pd.read_sql(query, conn)

st.title("Gestione Ordini")
st.sidebar.success("Naviga in un altra pagina del menu.")

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

