from google.adk.agents import Agent
from tools.tools import fetch_greeting
from google.adk.tools import google_search
from config.settings import MODEL_GEMINI

def create_greeting_agent():
    """
    Creates and configures the Google ADK greeting agent.
    This agent is designed to provide personalized greetings and engage in general conversation.
    """
    root_agent = Agent(
        name="greeting_agent", # A unique name for this specific agent.
        model=MODEL_GEMINI,    # Specifies the Gemini model to power this agent's language understanding and generation.
        description="An agent that greets the user based on their name, hobbies, and interests.", # A brief, human-readable description of the agent's role.
        instruction=""" # The core instructions that dictate the agent's behavior and how it should use its tools.
        You are a helpful assistant that will answer the user's questions using google search.
        
        In case that the question involves weather, you will provide:
        - Celsius degrees as the main value, farenheit degress as secondary
        - Weather for the next 3 hours with Celsius degrees as the main value, farenheit degress as secondary 
        - A random fact about the location provided                 
        """,
        tools=[google_search], # Registers the 'fetch_greeting' function as a callable tool for this agent.
    )
    return root_agent