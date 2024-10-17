# AI_Agent_perplexity/config/settings.py
import os

class Settings:
    API_KEY = os.getenv("PURPLEXITY_API_KEY", "YOUR_API_KEY")  # 환경 변수에서 API 키 가져오기