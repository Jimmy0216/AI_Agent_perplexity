# AI_Agent_perplexity/api/perplexity_client.py
import httpx

class PerplexityClient:
    def __init__(self):
        self.api_url = "https://api.purplexity.com/search"
        self.api_key = "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"  # 퍼플렉시티 API 키

    async def fetch_results(self, query: str):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        params = {"query": query}

        async with httpx.AsyncClient() as client:
            response = await client.get(self.api_url, headers=headers, params=params)

        response.raise_for_status()  # 오류 발생 시 예외 발생
        return response.json()