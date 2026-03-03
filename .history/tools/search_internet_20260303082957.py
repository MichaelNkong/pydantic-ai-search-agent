from ddgs import DDGS
from pydantic_ai import Tool
from tools.schema import SearchInput



#@Tool
def search_internet(input:SearchInput)-> list:
    """
    Search the internet for current information.
    Returns a list of dicts with keys: title, href, body
    """
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(input.query, max_results=input.max_results):
            # ddgs.text() returns dicts in modern versions, but wrap to be safe
            if isinstance(r, dict):
                results.append({
                    "title": r.get("title", "No title"),
                    "href": r.get("href"),
                    "body": r.get("body")
                })
            else:
                # fallback for string-only results
                results.append({
                    "title": r,
                    "href": None,
                    "body": None
                })
    return results
if __name__ == "__main__":
    input_data = SearchInput(query="latest AI news")
    result = search_internet(input_data)
    print(result)