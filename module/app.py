'''
This code is used to activate a local server, and then I will use Postman to act as front end.
'''
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import matplotlib
import torch
from observe_audio_function_ver3 import load_audio, SAMPLE_RATE
# Set Matplotlib backend if needed, Agg is not interactive backend.
# To prevent warning from "Starting a Matplotlib GUI outside of the main thread will likely fail."
matplotlib.use('Agg')  # Set the backend to 'Agg' before importing pyplot

AUDIO_FOLDER_NAME = "data/audio_files"
IMAGE_FOLDER_NAME = "data/image_files"
PTH_PATH = "app/model_9_ENG_ver1.pth"

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Flask API started on Pythonanywhere. Hi there!'

@app.route('/test', methods=['GET'])
def get_test():
    return '8/11 Hello world!!'

@app.route('/predict', methods=['POST'])
def predict():
    if not os.path.exists(AUDIO_FOLDER_NAME):
        os.makedirs(AUDIO_FOLDER_NAME)
    if not os.path.exists(IMAGE_FOLDER_NAME):
        os.makedirs(IMAGE_FOLDER_NAME)

    # print(f"Clean the files in {IMAGE_FOLDER_NAME}.")
    for i in os.listdir(IMAGE_FOLDER_NAME):
        i_path = os.path.join(IMAGE_FOLDER_NAME, i)
        os.remove(i_path)

    
    
    # Check if any file was uploaded
    if not any(request.files.values()):
        return jsonify({'error': 'No files uploaded'}), 400

    # Currently, each audio changed into one image, and do one prediction
    for file_key in request.files:
        # dealt with updated files, with the correct key typed in Postman
        audio = request.files[file_key]

        # Save the uploaded file to a temporary location
        audio_path = os.path.join(AUDIO_FOLDER_NAME, audio.filename)
        audio.save(audio_path)
        audio1 , sr = load_audio(audio_path, sr=SAMPLE_RATE)
        
        # directly remove the audio
        os.remove(audio_path)
    
    return jsonify({"audio":len(audio1),
                    "sr":sr})