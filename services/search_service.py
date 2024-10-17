# AI_Agent_perplexity/services/search_service.py
from api.perplexity_client import PerplexityClient

class SearchService:
    def __init__(self, perplexity_client: PerplexityClient):
        self.perplexity_client = perplexity_client

    async def search(self, query: str):
        results = await self.perplexity_client.fetch_results(query)
        return results