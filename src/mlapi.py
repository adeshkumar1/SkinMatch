from ultralytics import YOLO
from pathlib import Path

def imageInModels(image):
    model = YOLO(Path.cwd() / 'src/Model/AcneYOLO.pt')
    # results = model(source=1, show=True, conf=0.05, save=True)
    results = "test"
    return results


