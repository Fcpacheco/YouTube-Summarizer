import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

from langchain_community.document_loaders import WikipediaLoader
from langchain_community.tools.tavily_search import TavilySearchResults
import arxiv

def search_web(query: str, max_results: int = 3) -> list:
    """
    Searches the web using TavilySearch and returns a list of search results.
    """
    tavily_search = TavilySearchResults(max_results=max_results)
    search_results = tavily_search.invoke(query)
    # Optionally, format results as needed.
    formatted_results = [
        {
            "url": result.get("url"),
            "content": result.get("content")
        }
        for result in search_results
    ]
    return formatted_results

def search_wikipedia(query: str, load_max_docs: int = 2) -> str:
    """
    Searches Wikipedia for the query and returns a formatted string with document contents.
    """
    loader = WikipediaLoader(query=query, load_max_docs=load_max_docs)
    search_docs = loader.load()
    formatted_results = "\n\n---\n\n".join([
        f"Source: {doc.metadata.get('source', 'unknown')}\nContent: {doc.page_content}"
        for doc in search_docs
    ])
    return formatted_results

def search_arxiv(query: str, max_results: int = 5) -> list:
    """
    Searches arXiv for the query and returns a list of papers with relevant details.
    The standard arXiv API does not require an API key.
    """
    # Although we retrieve the ARXIV_API_KEY from the environment,
    # it is not used since the public arXiv API does not require an API key.
    arxiv_api_key = os.getenv('ARXIV_API_KEY', None)
    
    # Use the arxiv library to perform the search.
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )
    
    results = []
    for result in search.results():
        results.append({
            "title": result.title,
            "summary": result.summary,
            "url": result.entry_id,
            "authors": [author.name for author in result.authors],
            "published": result.published.strftime("%Y-%m-%d") if result.published else "N/A"
        })
    return results
