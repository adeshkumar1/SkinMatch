from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from dotenv import load_dotenv, find_dotenv
import os

from flask_cors import CORS

from mlapi import *

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)
else:
    print("CANNOT CONNECT TO .env FILE")

app = Flask(__name__)

CORS(app)

@app.route("/download_images", methods=["POST"])
def DownloadImages():
    if request.method == "POST":
        print("Downloading Images")
        image = request.files['face-scans']
        filename = request.headers.get('Content-Disposition').split('filename=')[1][1:-1]
        image.save(os.path.join(os.path.dirname(__file__), 'face_images', filename))
        # faceData = imageInModels(image)

        return jsonify({
            "message": "Image Saved",
        }), 200
    
@app.route("/process_images", methods=["GET", "POST"])
def ProcessImages():
    if request.method == "POST":
        print("Processing Images")
        data = request.get_json()
        imagePaths = data.get('paths', [])
        finalGrade, finalType = imageRatings(imagePaths)
        print(finalGrade, finalType)

        return jsonify({
            "message": "Results analyzed",
            "data": finalGrade
        }), 200

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)