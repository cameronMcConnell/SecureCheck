# General packages
import pandas as pd
import numpy as np
import pickle

# Scikit-Learn packages
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

'''
Model Used: Logistic Regression
Accuracy: 81.91%
'''

# Gets the characters from input string
def getTokens(inputString):
    return [character for character in inputString]

# Read in the dataframe
dataframe = pd.read_csv('./data.csv', on_bad_lines='skip').dropna()

# Convert to np array for processing
passwords = np.array(dataframe['password'])

# Get the predicted labels
y = dataframe['strength']

# Create the vectorizer to use the tokens from the input (chars from strings)
vectorizer = TfidfVectorizer(tokenizer=getTokens)

# Get main training feature
x = vectorizer.fit_transform(passwords)

# Split the data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Create the model, default values
model = LogisticRegression(max_iter=2000)

# Fit/train the model with the training data
model.fit(x_train, y_train)

# Save the model to local file system
pickle.dump(model, open('./model.pkl', 'wb'))