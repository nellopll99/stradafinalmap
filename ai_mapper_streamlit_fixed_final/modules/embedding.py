import openai
from sklearn.metrics.pairwise import cosine_similarity
import random

def get_embedding(text, api_key, model="text-embedding-ada-002"):
    openai.api_key = api_key
    try:
        result = openai.Embedding.create(input=[text], model=model)
        return result["data"][0]["embedding"]
    except Exception as e:
        print(f"Errore embedding: {e}")
        return None

def estimate_revenue(text):
    text = text.lower()
    keywords = {
        "enterprise": (50, 500),
        "b2b": (10, 200),
        "crm": (5, 100),
        "saas": (2, 100),
        "startup": (0.1, 5),
        "club": (0.1, 10),
        "membership": (0.5, 20),
        "association": (0.5, 20),
        "non profit": (0.1, 5),
        "open source": (0.1, 2)
    }

    estimated = (1, 10)
    for k, rng in keywords.items():
        if k in text:
            estimated = rng
            break
    return round(random.uniform(*estimated), 2)

def rank_by_similarity(prompt, docs, api_key):
    prompt_emb = get_embedding(prompt, api_key)
    if not prompt_emb:
        return []

    enriched = []
    for d in docs:
        full_text = f"{d['title']} {d['body']}"
        doc_emb = get_embedding(full_text, api_key)
        if doc_emb:
            score = cosine_similarity([prompt_emb], [doc_emb])[0][0]
            revenue = estimate_revenue(full_text)
            enriched.append({**d, "score": score, "estimated_revenue_musd": revenue})
    ranked = sorted(enriched, key=lambda x: x["score"], reverse=True)
    return ranked
