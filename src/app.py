from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from dotenv import load_dotenv, find_dotenv
import os
import uuid

from flask_cors import CORS

from mlapi import *

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)
else:
    print("CANNOT CONNECT TO .env FILE")

app = Flask(__name__)
CORS(app)

@app.route("/process_images", methods=["GET", "POST"])
def ProcessImages():
    if request.method == "POST":
        print('A')
        image = request.files['face-scans']
        print(image)
        filename = str(uuid.uuid4()) + ".png"
        file_path = os.path.join(os.path.dirname(__file__), 'face_images', filename)
        print(file_path)
        image.save(file_path)

        faceData = imageInModels(image)
        print('C')

        return jsonify({
            "message": "Image processed",
            "data": faceData
        }), 200
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)