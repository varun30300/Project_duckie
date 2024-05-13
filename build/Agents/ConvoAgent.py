from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent
from langchain.agents import AgentExecutor

def convo_agent (CHAT_MODEL, human_text, retriever_tool, VERBOSE) : 
    # return ("Initialting Convo Agent")
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an AI assistent who helps student study, student may ask you questions or ask you to perform actions. When asked a question, you are only allowed to answer using the tools given. You are not allowed to answer any question outside the scope of your tools. In case someone asks a question you cannot answer then simply respond by telling them that."),
            ("placeholder", "{chat_history}"),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ]
    )
    agent = create_tool_calling_agent(CHAT_MODEL, [retriever_tool], prompt)
    
    if VERBOSE :  
        agent_executor = AgentExecutor(agent=agent, tools=[retriever_tool], verbose=True)
    else : 
        agent_executor = AgentExecutor(agent=agent, tools=[retriever_tool], verbose=False)
    result = agent_executor.invoke({"input": human_text})
    return result