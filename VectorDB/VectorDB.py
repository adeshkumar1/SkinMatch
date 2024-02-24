import pandas as pd
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from pathlib import Path
from langchain_openai import OpenAIEmbeddings

df = pd.read_csv(Path.cwd() / 'VectorDB/datasheet.csv')

df = df.dropna(axis=0)

new_list = []
for index, row in df.iterrows():
  string = ''
  for col in df.columns:
    string += str(row[col]) + ','
  new_list.append(string)


print("start")

vectordb = Chroma.from_texts(new_list, OpenAIEmbeddings(model="text-embedding-3-large", openai_api_key='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'))



