from duckduckgo_search import ddg

def search_web(query: str, max_results: int = 20):
    results = ddg(query, max_results=max_results)
    return [
        {"title": r.get("title", ""),
         "href": r.get("href", ""),
         "body": r.get("body", "")}
        for r in results or []
    ]
