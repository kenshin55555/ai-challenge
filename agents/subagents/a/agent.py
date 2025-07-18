from google.adk import Agent
from config.settings import MODEL_GEMINI
from google.adk.tools import google_search
from .a_prompt import A_PROMPT

def create_stock_agent():
    stock_agent = Agent(
        model=MODEL_GEMINI,
        name='stock_agent',
        instruction=A_PROMPT,
        tools=[google_search],
    )
    return stock_agent