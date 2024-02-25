import pandas as pd
from openai import OpenAI
from pathlib import Path
from pinecone import Pinecone
from dotenv import load_dotenv
import os
load_dotenv()
#----------------------------------------------------------------------
class DBConnection:

    def __init__(self):
        
        self.client = OpenAI(
            api_key= os.getenv("OPENAI_KEY")
        )
        self.pc = Pinecone(api_key='b7fdfedc-9382-4981-b6ce-8630eede3eaf')
        self.index = self.pc.Index("skinmatch")
        self.path = Path.cwd() / 'VectorDB/testsheet.csv'
        self.MODEL = 'text-embedding-3-small'
        self.PRODUCTS = "products"
        self.output = []
        self.id = 0

    def createEmbeddings(self, df):
        for arr in df.values:
            res = self.client.embeddings.create(
                input=[data for data in arr], model=self.MODEL
            )
        embeddings = [record.embedding for record in res.data]
        return embeddings
    
    def upsertToDB(self, df, embeddings):
        meta = [{'text': [line1], 'brand': [line2], 'type': [line3], 'country': [line4], 'ingridients': [line5], 'afterUse': [line6]} for line1, line2, line3, line4, line5, line6 in zip(df['name'], df['brand'], df['type'], df['country'], df['ingridients'], df['afterUse'])]
        ids_batch = [str(n + self.id) for n in range(df.shape[0])]
        self.id += df.shape[0]
        toupsert = zip(ids_batch, embeddings, meta)
        print(ids_batch)
        self.index.upsert(vectors=toupsert, namespace=self.PRODUCTS)

    def queryToDB(self, query):
        xq = self.client.embeddings.create(input=query, model=self.MODEL).data[0].embedding
        res = self.index.query(namespace=self.PRODUCTS, vector=[xq], top_k=5, include_metadata=True)
        for match in res['matches']:
            arr = []
            arr.append(str(match['metadata']['text']).replace("['","").replace("']",""))
            arr.append(str(match['metadata']['brand'])[2:-2])
            arr.append(str(match['metadata']['type']).replace("['","").replace("']",""))
            arr.append(str(match['metadata']['country']).replace("['","").replace("']",""))
            arr.append(str(match['metadata']['ingridients']).replace("['","").replace("']",""))
            arr.append(str(match['metadata']['afterUse']).replace("['","").replace("']",""))
            self.output.append(arr)
        return self.output

def split_dataframe_into_batches(df, batch_size):
    """
    Split a pandas DataFrame into batches of a specified size.
    
    Args:
    - df: pandas DataFrame
    - batch_size: int, size of each batch
    
    Returns:
    - list of pandas DataFrames, each representing a batch
    """
    num_batches = len(df) // batch_size + (1 if len(df) % batch_size != 0 else 0)
    return [df.iloc[i * batch_size:(i + 1) * batch_size] for i in range(num_batches)]

if __name__ == "__main__":

    df = pd.read_csv(Path.cwd() / 'VectorDB/datasheet.csv')#loads the csv file
    df = df.dropna(axis=0) #gets rid of any null rows with null values

    dbc = DBConnection() #connects to db
    x = 8540
    while(x != df.shape[0]):
        emb = dbc.createEmbeddings(df[x:x+20]) #uses openai to embed the data
        dbc.upsertToDB(df[x:x+20], emb)
        x += 20
        print("finish")
    # print(dbc.queryToDB("I have oily skin, what products would you reccomend?"))