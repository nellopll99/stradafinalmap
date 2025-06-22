import streamlit as st
from modules.expand import expand_prompt
from modules.search import search_web
from modules.embedding import rank_by_similarity
from modules.export import export_results

st.set_page_config(page_title="AI MAPPER - Server Ready", layout="wide")
st.title("🤖 AI MAPPER - Versione Server")

openai_key = st.text_input("🔐 OpenAI API Key", type="password")
prompt = st.text_area("Cosa stai cercando? (es. CRM per club sportivi)", height=100)
max_results = st.slider("Quanti risultati web vuoi analizzare?", 5, 50, 15)

if st.button("🔍 Cerca aziende con AI"):
    if not openai_key or not prompt:
        st.error("❌ Inserisci API Key e un prompt.")
    else:
        with st.spinner("🚀 Espansione del prompt..."):
            expanded_prompt = expand_prompt(prompt, openai_key)
            st.info(f"🔁 Prompt espanso: {expanded_prompt}")

        with st.spinner("🔍 Ricerca con DuckDuckGo..."):
            results = search_web(expanded_prompt, max_results=max_results)

        with st.spinner("🧠 Ranking AI in corso..."):
            ranked = rank_by_similarity(prompt, results, openai_key)

        if ranked:
            st.success(f"✅ Trovati {len(ranked)} risultati rilevanti")
            st.dataframe(ranked)
            export_results(ranked)
        else:
            st.warning("⚠️ Nessun risultato rilevante trovato. Prova con un prompt diverso.")
