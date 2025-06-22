import openai

def expand_prompt(prompt: str, api_key: str):
    openai.api_key = api_key
    messages = [
        {"role": "system", "content": "Sei un esperto di M&A e scouting tecnologico. Espandi un prompt per una ricerca web semantica su software di nicchia."},
        {"role": "user", "content": f"Espandi il prompt per cercare sul web: {prompt}"}
    ]
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"[ERROR] prompt expansion: {e}")
        return prompt
