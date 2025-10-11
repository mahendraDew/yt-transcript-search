from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.document_loaders import TextLoader

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain.tools import tool

from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import ChatPromptTemplate



from dotenv import load_dotenv
import os
load_dotenv()

GEMINI_API = os.getenv("GEMINI_API")


def main():
    print("hi there")

 
    #1. load the txt file
    file_path = "./example.txt"
    loader = TextLoader(file_path)
    docs = loader.load()
    print(len(docs))
    # print(docs)


    #2. text splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200, add_start_index=True
    )
    all_splits = text_splitter.split_documents(docs)
    # print(len(all_splits))
    print(f"Splited into {len(all_splits)} sub-documents.")


    embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001", google_api_key=GEMINI_API)
    vector_store = InMemoryVectorStore(embeddings)

    # vector_1 = embeddings.embed_query(all_splits[1].page_content)

    # print(f"Generated vectors of length {len(vector_1)}\n")


    document_ids = vector_store.add_documents(documents=all_splits)
    # print("some doc ids: ", document_ids[:3])


    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=GEMINI_API)
    @tool(response_format="content_and_artifact")
    def retrieve_context(query: str):
        """Retrieve information to help answer a query."""
        retrieved_docs = vector_store.similarity_search(query, k=2)
        serialized = "\n\n".join(
            (f"Source: {doc.metadata}\nContent: {doc.page_content}")
            for doc in retrieved_docs
        )
        return serialized, retrieved_docs

    from langchain_core.prompts import PromptTemplate

    tools = [retrieve_context]
    # If desired, specify custom instructions
    # prompt = ChatPromptTemplate.from_messages([
    #     (
    #         "system",
    #         "You have access to a tool that retrieves context from a blog post. "
    #         "Use it to help answer user queries as accurately as possible."
    #     ),
    #     ("human", "{input}")  # placeholder for the user's question
    # ])
    prompt = PromptTemplate.from_template("""
        You are a helpful AI assistant.
        Answer the following questions as best you can.
        You have access to the following tools:

        {tools}

        Use the following format:

        Question: the input question you must answer
        Thought: you should always think about what to do
        Action: the action to take, should be one of [{tool_names}]
        Action Input: the input to the action
        Observation: the result of the action
        ... (this Thought/Action/Action Input/Observation can repeat N times)
        Thought: I now know the final answer
        Final Answer: the final answer to the original input question

        Begin!

        Question: {input}
        Thought:{agent_scratchpad}
    """)

    agent = create_react_agent(llm, tools, prompt=prompt)
    query = input("Enter your query:")
    # for event in agent.stream(
    #     {"messages": [{"role": "user", "content": query}]},
    #     stream_mode="values",
    # ):
    #     event["messages"][-1].pretty_print()
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    result = agent_executor.invoke({"input": query})
    print(result["output"])




# import os
# from langchain.chat_models import init_chat_model

# def main2():
#     print("this is main2")

#     # llm = init_chat_model("google_genai:gemini-2.5-flash-lite-latest", api_key=GEMINI_API)
#     # llm.invoke("hi hello")
#     # from langchain.chat_models import ChatGoogleGenerativeAI

#     # llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=GEMINI_API)
#     # print(llm.list_models())
#     from langchain_google_genai import ChatGoogleGenerativeAI

#     llm = ChatGoogleGenerativeAI(
#         model="gemini-2.5-flash",
#         temperature=0,
#         max_tokens=None,
#         timeout=None,
#         max_retries=2,
#         # other params...
#         google_api_key=GEMINI_API
#     )
#     messages = [
#         (
#             "system",
#             "You are a helpful assistant that translates English to French. Translate the user sentence.",
#         ),
#         ("human", "I love programming."),
#     ]
#     ai_msg = llm.invoke(messages)
#     print(ai_msg)

# def google_genai():
#     from google import genai
#     from dotenv import load_dotenv
#     import os
#     load_dotenv()

#     GEMINI_API = os.getenv("GEMINI_API")

#     # The client gets the API key from the environment variable `GEMINI_API_KEY`.
#     client = genai.Client(api_key=GEMINI_API)

#     response = client.models.generate_content(
#         model="gemini-2.5-flash", contents="Explain how AI works in a few words"
#     )
#     print(response.text)

if __name__ == "__main__":
    main()
    # print("for testing")
    # llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=GEMINI_API)
    # # llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    # llm.invoke("Write me a ballad about LangChain")
    # print('dddd')
    # main2()
