from ultralytics import YOLO
from pathlib import Path
import cv2
from PIL import Image
import numpy as np

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

    image = Image.open(image)
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
        grade_preds.append(np.argmax(grade_probs[i].numpy()))
        type_preds.append(np.argmax(type_probs[i].numpy()))
    
    final_grade = int(np.mean(grade_preds))
    type_num = int(np.mean(type_preds))
    
    labels = ['dry', 'normal', 'oily']
    final_type = labels[type_num]

    return final_grade, final_type