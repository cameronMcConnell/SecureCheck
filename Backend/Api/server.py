from flask import Flask, request
from flask_cors import CORS
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

# Load the model.
model = pickle.load(open('model.pkl', 'rb'))

# Load passwords.
passwords = pickle.load(open('passwords.pkl', 'rb'))

# Gets the characters from input string.
def getTokens(inputString):
    return [character for character in inputString]

# Fit and create the vectorizer.
vectorizer = TfidfVectorizer(tokenizer=getTokens).fit(passwords)

# Create the server.
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Handle POST from the frontend.
@app.route('/predict', methods=['POST'])
def handle_post():
    data = [request.json['data']]
    x = vectorizer.transform(data)
    y_hat = model.predict(x)
    return {'prediction': str(y_hat[0])}