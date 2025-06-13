import streamlit as st
from modules.discovery import discover_companies
from modules.enrichment import enrich_data
from modules.export import export_to_excel
import pandas as pd

st.set_page_config(page_title="M&A Mapper AI", layout="wide")

st.title("M&A Mapper AI – Company Discovery Tool")

openai_key = st.text_input("🔐 OpenAI API Key", type="password")
prompt = st.text_area("Prompt AI (es. 'CRM per associazioni sportive in Europa')", height=100)
country_filter = st.text_input("Filtro paese (opzionale)")
sector_filter = st.text_input("Filtro settore (opzionale)")

if st.button("Trova aziende"):
    if not openai_key:
        st.warning("Inserisci la tua API key OpenAI.")
    else:
        with st.spinner("Analisi in corso..."):
            companies = discover_companies(prompt, country_filter, sector_filter, openai_key)
            st.write("📦 Aziende trovate:", companies)

            if not companies:
                st.warning("⚠️ Nessuna azienda trovata. Controlla la tua API key o il prompt.")
            else:
                enriched_df = enrich_data(companies)
                st.success("Analisi completata.")
                st.dataframe(enriched_df)
                export_to_excel(enriched_df)
