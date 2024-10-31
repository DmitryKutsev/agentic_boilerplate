from tavily import TavilyClient
import os

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

tavily_client = TavilyClient(api_key=TAVILY_API_KEY)