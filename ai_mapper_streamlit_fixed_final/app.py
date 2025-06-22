import streamlit as st
from modules.search import search_web
from modules.embedding import rank_by_similarity
from modules.export import export_results

st.set_page_config(page_title="AI MAPPER", layout="wide")

st.title("🤖 AI MAPPER")

openai_key = st.text_input("🔐 OpenAI API Key", type="password")
prompt = st.text_area("Descrivi cosa cerchi (es. CRM per club sportivi)", height=100)
max_results = st.slider("Quanti risultati web vuoi analizzare?", 5, 50, 15)

if st.button("Cerca aziende"):
    if not openai_key or not prompt:
        st.error("❌ Inserisci chiave OpenAI e descrizione.")
    else:
        with st.spinner("🔍 Ricerca in corso..."):
            results = search_web(prompt, max_results=max_results)
            ranked = rank_by_similarity(prompt, results, openai_key)

        if ranked:
            st.success(f"✅ Trovati {len(ranked)} risultati rilevanti")
            st.dataframe(ranked)
            export_results(ranked)
        else:
            st.warning("⚠️ Nessun risultato rilevante trovato. Prova un prompt diverso.")
