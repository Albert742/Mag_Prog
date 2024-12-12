import streamlit as st

# Authentication Check
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("Unauthorized access. Please log in first.")
    st.stop()


# Logout Button
if st.sidebar.button("Log Out"):
    st.session_state.clear()
    st.rerun()
    
# Funzione per la pagina di ingresso della dashboard
def warehouse_dashboard_home():
    st.image("logo.jpg", use_container_width=True)
    st.write("# Benvenuto nella Dashboard di Gestione Magazzino di Food&Pharma 📦")
    st.sidebar.success("Naviga attraverso il menu per accedere alle diverse funzionalità ")
    st.sidebar.write(f"Logged in as: {st.session_state.get('username', 'Unknown')}")


    st.markdown(
        """
        ### Panoramica
        Questa dashboard è stata progettata per gestire le operazioni del magazzino in modo efficiente, comprese:

        - **Gestione Inventari**: Tenere traccia delle quantità di stock, delle posizioni dei prodotti e delle date di scadenza.
        - **Elaborazione Ordini**: Creare, aggiornare e monitorare gli ordini per operazioni fluide.
        - **Gestione Zone e Scaffalature**: Sovrintendere e gestire le zone di stoccaggio e le loro configurazioni.
        - **Controllo Qualità**: Monitorare le attività di controllo qualità per mantenere gli standard.

        ### Funzionalità Principali
        - **Dati in Tempo Reale**: Rimani aggiornato con informazioni in tempo reale sul tuo magazzino.
        - **Interfaccia Utente Amichevole**: Semplifica le operazioni del magazzino complesse con un layout intuitivo.
        - **Analisi e Reporting**: Genera informazioni dai dati delle operazioni del magazzino per prendere decisioni informate.

        ### Guida all'Avvio
        Utilizza il menu a sinistra per navigare tra le diverse pagine, comprese:

        - **Panoramica Inventari**: Visualizza i livelli di stock correnti e i rapporti dettagliati sull'inventario.
        - **Gestione Ordini**: Gestisci gli ordini in arrivo e in partenza in modo efficiente.
        - **Gestione Zone**: Organizza e ottimizza le zone di stoccaggio e le scaffalature.
        - **Log di Controllo Qualità**: Verifica i log di controllo qualità per assicurarti che siano rispettati gli standard.

        Per ulteriore supporto o per segnalare problemi, si prega di contattare il nostro team di supporto.

        """
    )

    st.info(
        "Consiglio: Segna questo pagina come preferita per accedere rapidamente al tuo cruscotto di magazzino.",
        icon="🔖",
    )


if __name__ == "__main__":
    warehouse_dashboard_home()
