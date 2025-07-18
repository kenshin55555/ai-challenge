# Repository made to host code for an AI challenge I'm working on

Code will not be updated once the challenge has been completed

I'm making use of Streamlit logic published by Ketan Raj in this [article](https://medium.com/@ketanraaz/build-your-agent-a-deep-dive-into-google-adk-and-streamlit-integration-cee9d79164e4)

## Steps to run
1. Install requirements from requirements file `pip install -r requirements.txt`
2. Create ".env" file and include the following variables:
    1. GOOGLE_API_KEY: (to be able to use any Gemini model), note: to generate the API, you need an exisiting Google Project, key can then be generated [here](https://aistudio.google.com/apikey)
    2. MODEL: To initialize the model to use across the code base
3. Run the following command: `streamlit run main.py`

## Considerations
- WIP: So far there's only the root agent and a subagent
- Bugs: When the agent is trying to return the response to the question, it won't return a field and so far waiting a little while before sending a simple additional input (like just one lletter) is needed in order for the response to be shown
