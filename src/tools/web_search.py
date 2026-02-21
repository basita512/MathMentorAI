"""Web search tool with citation tracking using Tavily API."""
from typing import List, Dict, Optional
from tavily import TavilyClient
from src.utils.config import config
from src.utils.logger import get_logger

logger = get_logger()

class WebSearchTool:
    """
    Web search tool for finding math-related information not in knowledge base.
    
    Uses Tavily API for high-quality search results with automatic citations.
    """
    
    def __init__(self):
        """Initialize Tavily client."""
        api_key = getattr(config, 'TAVILY_API_KEY', None)
        if not api_key:
            logger.warning("TAVILY_API_KEY not found in config. Web search will be disabled.")
            self.client = None
        else:
            self.client = TavilyClient(api_key=api_key)
            logger.info("Tavily web search initialized")
    
    def search(
        self, 
        query: str, 
        max_results: int = 3,
        search_depth: str = "basic"
    ) -> Dict:
        """
        Search the web for math-related information.
        
        Args:
            query: Search query (usually the math problem)
            max_results: Maximum number of results to return
            search_depth: "basic" or "advanced" (advanced costs more)
            
        Returns:
            dict with 'results' (list of sources) and 'answer' (direct answer if available)
        """
        if not self.client:
            logger.error("Tavily client not initialized. Cannot perform search.")
            return {'results': [], 'answer': None}
        
        try:
            logger.info(f"Searching web for: {query[:100]}...")
            
            # Perform search
            response = self.client.search(
                query=query,
                search_depth=search_depth,
                max_results=max_results,
                include_answer=True,
                include_raw_content=False,
                include_images=False
            )
            
            # Extract results
            results = []
            for item in response.get('results', []):
                results.append({
                    'title': item.get('title', 'Untitled'),
                    'url': item.get('url', ''),
                    'content': item.get('content', ''),
                    'score': item.get('score', 0.0)
                })
            
            # Get direct answer if available
            answer = response.get('answer', None)
            
            logger.info(f"Found {len(results)} web search results")
            
            return {
                'results': results,
                'answer': answer,
                'query': query
            }
            
        except Exception as e:
            logger.error(f"Web search failed: {e}")
            return {'results': [], 'answer': None}
    
    def format_for_context(self, search_result: Dict) -> str:
        """
        Format search results for inclusion in LLM context.
        
        Args:
            search_result: Result from search() method
            
        Returns:
            Formatted string with citations
        """
        if not search_result['results']:
            return ""
        
        formatted = "\n\n=== WEB SEARCH RESULTS ===\n"
        
        # Add direct answer if available
        if search_result.get('answer'):
            formatted += f"\nDirect Answer: {search_result['answer']}\n"
        
        # Add sources
        formatted += "\nSources:\n"
        for i, result in enumerate(search_result['results'], 1):
            formatted += f"\n{i}. {result['title']}\n"
            formatted += f"   URL: {result['url']}\n"
            formatted += f"   {result['content'][:300]}...\n"
        
        formatted += "\n=== END WEB SEARCH ===\n"
        
        return formatted
    
    def extract_citations(self, search_result: Dict) -> List[Dict]:
        """
        Extract citation information for UI display.
        
        Returns:
            List of citation dicts with title, url, source='web_search'
        """
        citations = []
        for result in search_result.get('results', []):
            citations.append({
                'title': result['title'],
                'url': result['url'],
                'source': 'web_search',
                'score': result.get('score', 0.0)
            })
        return citations
