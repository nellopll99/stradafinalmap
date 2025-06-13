import openai
import json

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
        print("Errore nel rilevamento modello:", e)
        return "gpt-3.5-turbo"

def discover_companies(prompt, country, sector, api_key):
    model = get_best_model(api_key)
    openai.api_key = api_key

    base_prompt = f"Dammi un elenco di 15 aziende attive in {sector or 'qualsiasi settore'} in {country or 'Europa'} che siano rilevanti per: \"{prompt}\". Per ciascuna, indicami: - Nome azienda - Dominio web ufficiale. Rispondi solo con un JSON valido."

    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": base_prompt}],
            temperature=0.3
        )
        content = response['choices'][0]['message']['content']
        print("🧠 Risposta GPT:
", content)

        if "[" in content:
            json_start = content.find("[")
            content = content[json_start:]
            companies = json.loads(content)
            return companies
        else:
            print("⚠️ Nessun JSON trovato nella risposta.")
            return []
    except Exception as e:
        print("❌ Errore chiamata OpenAI:", str(e))
        return []
