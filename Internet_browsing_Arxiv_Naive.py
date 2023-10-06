from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools, initialize_agent, AgentType
import os


#pip install arxiv
os.environ['OPENAI_API_KEY'] = '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'

llm = ChatOpenAI(temperature=0.3)
tools = load_tools(
    ["arxiv"]
)

agent_chain = initialize_agent(
    tools,
    llm,
    max_iterations=5,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True, ### IMPORTANT
)

agent_chain.run(
    "what is RLHF?",
)