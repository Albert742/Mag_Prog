# File: pages/Inventory_Overview.py
import streamlit as st
import pandas as pd
from MagDBcontroller import connessione, selectSQL

def fetch_inventory_data():
    with connessione() as conn:
        query = """
        SELECT Prodotti.Nome AS Prodotto, Zone.Nome AS Zona, Scaffalature.Nome AS Scaffalatura, 
               Lotti.Quantita, Lotti.Scadenza, Lotti.Stato
        FROM Lotti
        JOIN Prodotti ON Lotti.ID_Prodotto = Prodotti.ID_Prodotto
        JOIN Zone ON Lotti.ID_Zona = Zone.ID_Zona
        JOIN Scaffalature ON Lotti.ID_Scaffalatura = Scaffalature.ID_Scaffalatura
        """
        return pd.read_sql(query, conn)

st.title("Panoramica Inventario")
st.sidebar.success("Naviga in un altra pagina utilizzando il menu.")

try:
    inventory_data = fetch_inventory_data()
    st.write("### Stato attuale dell inventario")
    st.dataframe(inventory_data)
except Exception as e:
    st.error(f"Errore durante il caricamento dei dati: {e}")

