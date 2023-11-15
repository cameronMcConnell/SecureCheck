from flask import Flask, request
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

# Load the model.
model = pickle.load(open('model.pkl', 'rb'))

# Gets the characters from input string
def getTokens(inputString):
    return [character for character in inputString]

# Create the vectorizer to use the tokens from the input (chars from strings)
vectorizer = TfidfVectorizer(tokenizer=getTokens)

# Create the server.
app = Flask(__name__)

@app.route('/predict')
def handle_post():
    x = vectorizer.fit_transform([request['data']])
    y_hat = model.predict(x)
    print(y_hat)
    return {'prediction': y_hat}