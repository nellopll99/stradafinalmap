from duckduckgo_search import DDGS, DuckDuckGoSearchException
import time
from duckduckgo_search import ddg

def search_web(query: str, max_results: int = 20):
    tries = 0
    while tries < 3:
        try:
            with DDGS() as ddgs:
                return [
                    {"title": r.get("title", ""),
                     "href": r.get("href", ""),
                     "body": r.get("body", "")}
                    for r in ddgs.text(query, max_results=max_results)
                ]
        except DuckDuckGoSearchException:
            tries += 1
            time.sleep(1.5)
    legacy = ddg(query, max_results=max_results)
    return [{"title": r["title"], "href": r["href"], "body": r["body"]} for r in legacy or []]
