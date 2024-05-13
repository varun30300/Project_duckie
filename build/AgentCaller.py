from langchain_core.prompts import ChatPromptTemplate
from Agents import ConvoAgent

def duckie_response(CHAT_MODEL,human_text, retriever_tool, VERBOSE):

    chat_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", '''You are a helpful AI bot. You read the human text and classify the type of the text.
                            Types of human text can be - CreateConvo, CreateFlashCards. 
                            Definition of each type is, 
                            CreateConvo : If the human text is asking a question and the only acceptable output is an answer to that question 
                                       or if the human is asking for an explanation or for an elaloration of a specific or a broad topic
                                       then the human is supposed to be classified as CreateConvo. 
                            CreateFlashCards : If the human text is asking for an action and the action asked is to create flash cards 
                                       for revision or exam preperation, then the human text is supposed to be classified as CreateFlashCards.
                            
                        '''
            ),
            ("human", "What is magnitism ?"),
            ("ai", "CreateConvo"),
            ("human", "Can you explain me photosynthesis."),
            ("ai", "CreateConvo"),
            ("human", "Can you create flash card for my revision."),
            ("ai", "CreateFlashCards"),
            ("human", "Explain Apple. "),
            ("ai", "CreateConvo"),
            ("human", "Can you elaborate on how does magnets work"),
            ("ai", "CreateConvo"),
            ("human", "Can you summarize the topic 'Functions' please."),
            ("ai", "CreateConvo"),
            ("human", "{text}"),
        ]
    )

    request = chat_prompt.format_prompt(text=human_text).to_messages()
    result = CHAT_MODEL.invoke(request)
    human_text_classification = result.content

    if human_text_classification == "CreateConvo" : 
        # return convoAgent(human_text, verbose)
        return ConvoAgent.convo_agent(CHAT_MODEL, human_text, retriever_tool, VERBOSE)

    # elif human_text_classification.content == "CreateFlashCards" : 
    #     return flashCardsAgent(human_text, verbose)
    else :
        return "Unknown human text type" 