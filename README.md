# Project Duckie

## About
Project Duckie is a versatile tool designed for students to upload their study material and ask questions related to it. Additionally, it can create JSON files for generating flashcards (note: the UI for a functional flashcard system is not included).

## Features
- **AI Response Generation**: Tools for generating AI-based responses.
- **Human Text Classification**: Notebooks for classifying and analyzing human text.
- **Conversational Agent**: Implementations for creating conversation agents.
- **Document Loading**: Efficient methods for loading and processing documents.
- **Flashcards Agent**: A flashcard system for learning and testing knowledge (UI not included).

## File Structure
- `build/`: Directory containing build-related files.
- `duckie_knowledge/`: Resources related to the knowledge base of the project.
- `AIResponse.ipynb`: Notebook for AI response generation.
- `ClassifyHumanText.ipynb`: Notebook for classifying human text.
- `ConvoAgent.ipynb`: Notebook for the conversational agent.
- `DocumentLoader.ipynb`: Notebook for document loading.
- `FlashCardsAgent.ipynb`: Notebook for the flashcards agent.
- `Imports.ipynb`: Notebook managing import statements and dependencies.
- `Toolkit.ipynb`: Additional tools and utilities for the project.
- `duckie.ipynb`: Main project notebook.

### List of Unique Libraries

- **langchain_core**
  - `ChatPromptTemplate`

- **langchain**
  - `AgentExecutor`
  - `create_tool_calling_agent`

- **langchain_community**
  - `DirectoryLoader`
  - `vectorstores`
    - `FAISS`

- **langchain_text_splitters**
  - `RecursiveCharacterTextSplitter`

- **langchain_openai**
  - `OpenAIEmbeddings`
  - `ChatOpenAI`

- **langchain.tools**
  - `retriever`
    - `create_retriever_tool`

- **Agents**
  - `ConvoAgent`

- **Tools**
  - `KnowledgeInitializer`

- Other Dependencies
  - `AgentCaller`
  - `tkinter`
  - `ttk`
  - `os`


## Getting Started
1. Clone the repository:
   ```sh
   git clone https://github.com/varun30300/Project_duckie.git
   ```

2. Set OPENAI API:
   ```sh
   setx OPENAI_API_KEY "YOUR_API_KEY"
   ```

3. Navigate to the project build directory:
   ```sh
   cd Project_duckie/build
   ```

4. Run the program:
   ```python
   python main.py
   ```
