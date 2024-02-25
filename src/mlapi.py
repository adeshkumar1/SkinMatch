from ultralytics import YOLO
from pathlib import Path
import cv2
from PIL import Image
import numpy as np
import os
from openai import OpenAI

def getSummary(level, skin):
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