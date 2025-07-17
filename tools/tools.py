from typing import Dict, Any, Optional
from google.adk.tools.tool_context import ToolContext

def fetch_greeting(tool_context: ToolContext, name: Optional[str] = None, hobbies: Optional[str] = None, interests: Optional[str] = None) -> Dict[str, Any]:
    """
    Fetches a greeting message based on the user's name, hobbies, and interests.
    This tool also updates the ADK session state with any new user information provided.
    
    Args:
        tool_context: Provides access to the ADK session state and other tool-related functionalities.
        name (Optional[str]): The user's name to be stored or updated.
        hobbies (Optional[str]): The user's hobbies to be stored or updated.
        interests (Optional[str]): The user's interests to be stored or updated.
    Returns:
        Dict[str, Any]: A dictionary containing a status and the generated greeting message.
    """
    try:
        adk_session_state = tool_context.state # Access the current session state managed by ADK.
        
        # Update user information in the ADK session state if provided by the tool call.
        if name:
            adk_session_state['user_name'] = name
        if hobbies:
            adk_session_state['user_hobbies'] = hobbies
        if interests:
            adk_session_state['user_interests'] = interests
        # Retrieve user information (with default values if not set).
        user_name = adk_session_state.get('user_name', 'Friend')
        user_hobbies = adk_session_state.get('user_hobbies', '')
        user_interests = adk_session_state.get('user_interests', '')
        
        # Construct the personalized greeting message.
        greeting_parts = [f"Hello {user_name}!"]
        if user_hobbies:
            greeting_parts.append(f"I see you enjoy {user_hobbies}.")
        if user_interests:
            greeting_parts.append(f"Your interests in {user_interests} sound fascinating!")
        if not user_hobbies and not user_interests:
            greeting_parts.append("Nice to meet you!")
        greeting_parts.append("How can I help you today?")
        
        personalized_greeting = " ".join(greeting_parts)
        
        # Return the greeting message to the ADK agent.
        return {"status": "success", "greeting": personalized_greeting}
    except Exception as e:
        # Handle any errors during tool execution.
        return {"status": "error", "message": f"Sorry, I encountered an error: {str(e)}"}