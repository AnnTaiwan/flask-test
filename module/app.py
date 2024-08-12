'''
This code is used to activate a local server, and then I will use Postman to act as front end.
'''
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Flask API started on Pythonanywhere. Hi there!'

@app.route('/test', methods=['GET'])
def get_test():
    return 'Hello world!! This is test page.'

@app.route('/add', methods=['POST'])
def add_two_numbers():
    # Extract data from the JSON request
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")
    
    # Perform the addition
    if a is not None and b is not None:
        ans = a + b
        return jsonify({"result": ans})
    else:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    app.run(debug=False)