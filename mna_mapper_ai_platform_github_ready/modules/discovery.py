import openai
import json
import streamlit as st

def get_best_model(api_key):
    openai.api_key = api_key
    try:
        models = openai.Model.list()
        model_ids = [m.id for m in models.data]
        if "gpt-4" in model_ids:
            return "gpt-4"
        elif "gpt-3.5-turbo" in model_ids:
            return "gpt-3.5-turbo"
        else:
            return "gpt-3.5-turbo"
    except Exception as e:
        st.error(f"Errore nel rilevamento modello: {e}")
        return "gpt-3.5-turbo"

def discover_companies(prompt, country, sector, api_key):
    model = get_best_model(api_key)
    openai.api_key = api_key

    base_prompt = (
        f"Riceverai un prompt in italiano o inglese. Identifica 15 aziende attive in {sector or 'qualsiasi settore'} "
        f"localizzate in {country or 'Europa'} rilevanti per: \"{prompt}\". "
        "Rispondi esclusivamente con un array JSON come questo esempio: "
        "[{\"name\": \"Azienda X\", \"url\": \"www.aziendax.com\"}, ...]. "
        "Non scrivere testo prima o dopo. Solo JSON puro."
    )

    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": base_prompt}],
            temperature=0.3
        )
        content = response['choices'][0]['message']['content']
        st.subheader("🧠 Risposta GPT grezza")
        st.code(content)

        if "[" in content:
            json_start = content.find("[")
            content = content[json_start:]
            companies = json.loads(content)
            return companies
        else:
            st.error("⚠️ Nessun JSON valido trovato nella risposta.")
            return []
    except Exception as e:
        st.error(f"❌ Errore durante la chiamata OpenAI: {e}")
        return []
