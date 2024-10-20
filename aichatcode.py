from langchain import RunnableWithMessageHistory, LLMClient, Retriever
from openai import ChatGPT

# Configure OpenAI credentials
api_key = 
chat_gpt = ChatGPT(api_key)

# Configure LangChain
retriever = Retriever(k=1)  # K-nearest neighbors retrieval with k=1

# Define the ConversationalChain
chain = ConversationalChain(
    llm=chat_gpt,  # OpenAI LLM client
    retriever=retriever,  # Retriever for context retrieval
    combine_docs_chain_kwargs={"prompt": "Here is our conversation so far:", "max_tokens": 512},
)

# Start conversation
while True:
    user_input = input("You: ")
    chain.update(user_input)
    response = chain.next()
    print(f"OpenAI: {response}")
