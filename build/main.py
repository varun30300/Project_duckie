from Tools import KnowledgeInitializer
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import AgentCaller

CHAT_MODEL = ChatOpenAI(model = "gpt-4-turbo")
VERBOSE = True

# check if the database is changed, if yes, get new embedded knowledge retrieved tool 
retriever_tool = KnowledgeInitializer.knowledge_initializer()

human_text = "What is the meaning of life"

reponse = AgentCaller.duckie_response(CHAT_MODEL, human_text, retriever_tool, VERBOSE)

print(reponse)