from ddgs import DDGS
from pydantic_ai import Tool
from tools.schema import SearchInput, SearchOutput, SearchResult
import logging


logger = logging.getLogger(__name__)


@Tool
def search_internet(input:SearchInput) -> dict:
    """
    Search the internet for current information.
    Returns a list of dicts with keys: title, href, body
    """
    results: list[SearchResult] = []
    try:
        with DDGS() as ddgs:
            for r in ddgs.text(input.query, max_results=input.max_results):
                # ddgs.text() returns dicts in modern versions, but wrap to be safe
                if isinstance(r, dict):
                    sr = SearchResult(
                        title=r.get("title", "No title"),
                        href=r.get("href"),
                        body=r.get("body"),
                    )
                else:
                    # fallback for string-only results
                    sr = SearchResult(title=str(r), href=None, body=None)

                results.append(sr)
    except Exception:
        logger.exception("search_internet: DDGS search failed")
        return SearchOutput(results=[]).dict()

    return SearchOutput(results=results).dict()
if __name__ == "__main__":
    input_data = SearchInput(query="latest AI news")
    result = search_internet(input_data)
    print(result)