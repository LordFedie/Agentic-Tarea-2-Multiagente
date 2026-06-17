from duckduckgo_search import DDGS


def web_search(query: str, max_results: int = 5):

    print(f"[SEARCH TOOL] Buscando: {query}")

    results = []

    with DDGS() as ddgs:
        search_results = ddgs.text(
            query,
            max_results=max_results
        )

        for result in search_results:
            results.append(
                {
                    "title": result["title"],
                    "body": result["body"],
                    "href": result["href"]
                }
            )

    print(f"[SEARCH TOOL] {len(results)} resultados encontrados")

    return results