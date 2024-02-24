import pandas as pd
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from pathlib import Path
from langchain_openai import OpenAIEmbeddings

def getQuery(str):
    vectordb = Chroma(persist_directory="./chroma_db", embedding_function=OpenAIEmbeddings(model="text-embedding-3-large", openai_api_key='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'))
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    qa = ConversationalRetrievalChain.from_llm(llm=OpenAI(openai_api_key='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'),
                                            memory=memory,
                                            retriever=vectordb.as_retriever())

    brand = []
    name = []

    qa.run(str)

    docs_and_scores = vectordb.similarity_search_with_score(str)

    for i in docs_and_scores:
        string = str(i).split('\'')[1]
        print(string)
        array = string.split(',')
        brand.append(array[0])
        name.append(array[1])

    print("Here are some products you can try 😁! ")

    for i in range(len(brand)):
        print(name[i], 'from', brand[i], "\n")