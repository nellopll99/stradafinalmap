import requests

def search_web(query: str, max_results: int = 20, rapidapi_key: str = ""):
    url = "https://bing-web-search1.p.rapidapi.com/search"
    headers = {
        "X-RapidAPI-Key": rapidapi_key,
        "X-RapidAPI-Host": "bing-web-search1.p.rapidapi.com"
    }
    params = {
        "q": query,
        "count": max_results,
        "safeSearch": "Off",
        "textFormat": "Raw"
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    results = data.get("webPages", {}).get("value", [])

    return [
        {
            "title": r.get("name", ""),
            "href": r.get("url", ""),
            "body": r.get("snippet", "")
        }
        for r in results
    ]
