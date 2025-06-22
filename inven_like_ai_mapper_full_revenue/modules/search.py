from duckduckgo_search import DDGS

def search_web(query, max_results=20):
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=max_results)
        cleaned = []
        for r in results:
            cleaned.append({
                "title": r.get("title", ""),
                "href": r.get("href", ""),
                "body": r.get("body", "")
            })
        return cleaned
