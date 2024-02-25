from ultralytics import YOLO
from pathlib import Path

model = YOLO(Path.cwd() / 'Model/acne2.pt')

results = model(source=1, show=True, conf=0.05, save=True)