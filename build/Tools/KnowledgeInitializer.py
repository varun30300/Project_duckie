from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
import os
from langchain.tools.retriever import create_retriever_tool

def knowledge_initializer ():

    # getting latest_file_last_update_time
    knowledge_files = [os.path.join("Knowledge", f) for f in os.listdir("Knowledge") if os.path.isfile(os.path.join("Knowledge", f))]
    print(knowledge_files)
    latest_file = max(knowledge_files, key=os.path.getctime)
    latest_file_last_update_time =  os.path.getmtime(latest_file)

    # Open the text file in read mode
    with open('meta.txt', 'r') as file:
        # Read the contents of the file
        saved_last_update_time = file.read()
    print(saved_last_update_time)

    if  float(latest_file_last_update_time) > float(saved_last_update_time) : 
        print("Embedding latest documents.")

        with open('meta.txt', 'w') as file:
            file.write(str(latest_file_last_update_time))

        loader = DirectoryLoader('./Knowledge', glob="*.txt" ,show_progress=True, use_multithreading=True) # only reads txt files 
        docs = loader.load()

        # Name of files in the knowledge
        for doc in range(len(docs)) : 
            print("File",doc+1,"-",docs[doc].metadata['source'].split("\\")[-1])

        # Number of files in the knowledge
        print("Number of file/s :",len(docs))

        # converting docs into chunks 
        documents = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200).split_documents(docs)

        # embedding documents 
        vector_db = FAISS.from_documents(documents, OpenAIEmbeddings())
    
        # storing the embeddings locally
        vector_db.save_local('./knowledge_embeddings')

    else : 
        print("Loading stored embeddings")
        vector_db=FAISS.load_local('./knowledge_embeddings', OpenAIEmbeddings(), allow_dangerous_deserialization=True)

    retriever = vector_db.as_retriever()

    retriever_tool = create_retriever_tool(
    retriever,
    "full_directory",
    "Search for information about only using this tool.",
)

    return retriever_tool
    