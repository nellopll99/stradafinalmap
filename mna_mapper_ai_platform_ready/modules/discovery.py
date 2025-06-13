import openai
import json

def discover_companies(prompt, country, sector, api_key):
    openai.api_key = api_key

    base_prompt = f"Dammi un elenco di 15 aziende attive in {sector or 'qualsiasi settore'} in {country or 'Europa'} che siano rilevanti per: \"{prompt}\". Per ciascuna, indicami: - Nome azienda - Dominio web ufficiale. Rispondi solo con un JSON array della forma: [{{'name': ..., 'url': ...}}, ...]"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": base_prompt}],
            temperature=0.3
        )
        content = response['choices'][0]['message']['content']
        companies = json.loads(content)
        return companies
    except Exception as e:
        print("Errore GPT:", e)
        return []
