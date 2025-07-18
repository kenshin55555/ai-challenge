from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from config.settings import MODEL_GEMINI
from .prompts.root_prompt import ROOT_PROMPT
from .subagents.a.agent import create_stock_agent

stock_agent = create_stock_agent()

def create_greeting_agent():
    """
    Creates and configures the Google ADK greeting agent.
    This agent is designed to provide personalized greetings and engage in general conversation.
    """
    root_agent = Agent(
        name="greeting_agent", # A unique name for this specific agent.
        model=MODEL_GEMINI,    # Specifies the Gemini model to power this agent's language understanding and generation.
        description="An agent that orchestrates access to stock information", # A brief, human-readable description of the agent's role.
        instruction=ROOT_PROMPT,
        tools=[AgentTool(agent=stock_agent)], 
    )
    return root_agent