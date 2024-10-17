# AI_Agent_perplexity/models/travel_query.py
from pydantic import BaseModel

class TravelQuery(BaseModel):
    query: str