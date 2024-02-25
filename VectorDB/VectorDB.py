import pandas as pd
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from pathlib import Path
from langchain_openai import OpenAIEmbeddings
import csv
import chromadb

client = chromadb.PersistentClient(path='/Users/adesh/Desktop/Hackathon/hackathon/VectorDB')
client.heartbeat()

def getVectorDB(path):
    print("--------------------")
    df = pd.read_csv(path)

    df = df.dropna(axis=0)
    df = df[:5]

    new_list = []
    for index, row in df.iterrows():
        string = ''
    for col in df.columns:
        string += str(row[col]) + ','
    new_list.append(string)
    vectordb = Chroma.from_texts(new_list, OpenAIEmbeddings(model="text-embedding-3-large", openai_api_key='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'))
    return vectordb

def getQuery(query, vectordb):
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    qa = ConversationalRetrievalChain.from_llm(llm=OpenAI(openai_api_key='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'),
                                            memory=memory,
                                            retriever=vectordb.as_retriever())
    brand = []
    name = []

    qa.run(query)

    docs_and_scores = vectordb.similarity_search_with_score(query)
    for i in docs_and_scores:
        string = str(i).split('\'')[1]
        array = string.split(',')
        brand.append(array[0])
        name.append(array[1])

    output = "Here are some products you can try 😁 \n"

    for i in range(len(brand)):
        output += name[i] + ' from ' + brand[i] + "\n"

    return output

path = Path.cwd() / 'VectorDB/datasheet.csv'
vectordb = getVectorDB(path)


for i in range(5):
    print(getQuery("I have oily skin can you recoomend me some products", vectordb))