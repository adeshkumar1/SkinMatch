import pandas as pd
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from pathlib import Path
from langchain_openai import OpenAIEmbeddings
from VectorDB import getQuery



