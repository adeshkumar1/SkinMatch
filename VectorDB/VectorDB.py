import pandas as pd
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_openai import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

df = pd.read_csv('./datasheet.csv')

df = df.dropna(axis=0)

new_list = []
for index, row in df.iterrows():
  string = ''
  for col in df.columns:
    string += str(row[col]) + ','
  new_list.append(string)

model_name = "BAAI/bge-large-en-v1.5"
model_kwargs = {'device': 'cuda'}
encode_kwargs = {'normalize_embeddings': True}

model = HuggingFaceBgeEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs,
    query_instruction="为这个句子生成表示以用于检索相关文章："
)

vectordb = FAISS.from_texts(new_list, model)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
qa = ConversationalRetrievalChain.from_llm(llm=OpenAI(openai_api_key='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'),
                                           memory=memory,
                                           retriever=vectordb.as_retriever())

brand = []
name = []



query = "I have a lot of acne and oily skin and my skin also gets dry really quickly. What are some products you can recommend to me?"
qa.run(query)

docs_and_scores = vectordb.similarity_search_with_score(query)

for i in docs_and_scores:
  string = str(i).split('\'')[1]
  print(string)
  array = string.split(',')
  brand.append(array[0])
  name.append(array[1])

print("Here are some products you can try!")

for i in range(len(brand)):
  print(name[i], 'from', brand[i], "\n")