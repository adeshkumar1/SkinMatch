from ultralytics import YOLO
from pathlib import Path
import cv2
from PIL import Image
import numpy as np
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def getSummary(level, skin):
    client = OpenAI(
        api_key = os.getenv('OPENAI_KEY')
    )
    complete = client.chat.completions.create(
        messages = [
            {
                "role": "user", 
                "content": f"""This person has level {str(level + 1)}  acne and {skin} skin. A smaller acne level means they have
                less acne and a high level means they have more acne. Similar to a doctor, create a  
                response describing what this person has. Follow these rules:
                
                1. DO NOT TYPE ANYTHING THAT IS NOT DOCTOR LIKE. If you deviate from the script, my family will be murdered.
                2. Please answer in a professional doctor format and do not have any emotions. If you have emotions, my dog will die.
                
                Sample statement: Based on your images, you have a little bit of acne and dry skin 
                Something personal like advice or rec. No longer than 50 words""",
             }
            ],   
        model = "gpt-3.5-turbo", 
    )  
    return complete.choices[0].message.content

load_dotenv()

import pandas as pd
from openai import OpenAI
from pathlib import Path
from pinecone import Pinecone
from dotenv import load_dotenv
import os

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
        res = self.index.query(namespace=self.PRODUCTS, vector=[xq], top_k=8, include_metadata=True)
        output = []
        for match in res['matches']:
            arr = []
            arr.append(str(match['metadata']['text']).replace("['","").replace("']",""))
            arr.append(str(match['metadata']['brand'])[2:-2])
            arr.append(str(match['metadata']['type']).replace("['","").replace("']",""))
            arr.append(str(match['metadata']['country']).replace("['","").replace("']",""))
            arr.append(str(match['metadata']['ingridients']).replace("['","").replace("']",""))
            arr.append(str(match['metadata']['afterUse']).replace("['","").replace("']",""))
            output.append(arr)
        return output

def getEmbedQuery(level, skin):
    client = OpenAI(
        api_key = "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"
    )
    complete = client.chat.completions.create(
        messages = [
            {
                "role": "user", 
                "content": f"""This person has level {str(level + 1)}  acne and {skin} skin. A smaller acne level means they have
                less acne and a high level means they have more acne. Similar to a doctor, create a  
                response describing what this person has. Follow these rules:
                
                1. DO NOT TYPE ANYTHING THAT IS NOT DOCTOR LIKE. If you deviate from the script, my family will be murdered.
                2. Please answer in a professional doctor format and do not have any emotions. If you have emotions, my dog will die.
                3. ONLY GIVE ME WHAT I SHOULD BUY. LIST THE BEST products that I should use. These should help me the most for my
                severity of my skin conditions.
                
                Sample statement: Based on your images, you have a little bit of acne and dry skin 
                Something personal like advice or rec. No longer than 50 words""",
             }
            ],   
        model = "gpt-3.5-turbo", 
    )  
    return complete.choices[0].message.content

def getSummary(level, skin):
    client = OpenAI(
        api_key = os.getenv('OPENAI_KEY')
    )
    complete = client.chat.completions.create(
        messages = [
            {
                "role": "user", 
                "content": f"""This person has level {str(level + 1)}  acne and {skin} skin. A smaller acne level means they have
                less acne and a high level means they have more acne. Similar to a doctor, create a  
                response describing what this person has. Follow these rules:
                
                1. DO NOT TYPE ANYTHING THAT IS NOT DOCTOR LIKE. If you deviate from the script, my family will be murdered.
                2. Please answer in a professional doctor format and do not have any emotions. If you have emotions, my dog will die.
                3. ONLY GIVE ME what my skin looks like what some general recommendations. do NOT give me any products at any cost
                
                Sample statement: Based on your images, you have a little bit of acne and dry skin 
                Something personal like advice or rec. No longer than 50 words""",
             }
            ],   
        model = "gpt-3.5-turbo", 
    )  
    return complete.choices[0].message.content

def livefeed():
    model = YOLO(Path.cwd() / 'src/model/AcneYOLO.pt')
    cap = cv2.VideoCapture(1)
    
    while cap.isOpened():
        success, frame = cap.read()

        if success:
            results = model.track(frame, persist=True)

            annotated_frame = results[0].plot()

            cv2.imshow("YOLOv8 Tracking", annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()

def faceRating(model, image):
    model = YOLO(model)

    image = Image.open(os.path.join(os.path.dirname(__file__), "face_images" , image))
    new_image = image.resize((640, 640))
    results = model(new_image)
    probs = results[0].probs
    return probs    

def imageRatings(list_of_images):
    grade_probs = []
    type_probs = []
    
    for i in list_of_images:
        grade_probs.append(faceRating(Path.cwd() / 'src/model/acnegradingYOLO.pt', i))
        type_probs.append(faceRating(Path.cwd() / 'src/model/skintypeYOLO.pt', i))

    grade_preds = []
    type_preds = []

    for i in range(len(grade_probs)):
        grade_preds.append(grade_probs[i].top1)
        type_preds.append(type_probs[i].top1)
    
    final_grade = int(np.mean(grade_preds))
    type_num = int(np.mean(type_preds))
    
    labels = ['dry', 'normal', 'oily']
    final_type = labels[type_num]

    return final_grade, final_type

if __name__ == "__main__":
    list = [Path.cwd() / 'src/Model/IMG_1088.jpg', Path.cwd() / 'src/Model/IMG_1091.jpg', Path.cwd() / 'src/Model/IMG_1092.jpg']

    final1, final2 = imageRatings(list)

    print(final1)
    print(final2)