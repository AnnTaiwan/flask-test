'''
This code is used to activate a local server, and then I will use Postman to act as front end.
'''
from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Flask API started on Pythonanywhere. Hi there!'

@app.route('/test', methods=['GET'])
def get_test():
    return '8/11 Hello world!!'