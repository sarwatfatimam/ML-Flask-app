'''
Created on Oct 11, 2018

@author: Sarwat Fatima
'''

from flask import Flask, request, redirect, url_for, flash, jsonify
from model_train import clean_data
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import json, pickle
import pandas as pd

# Creating Flask app instance 
app = Flask(__name__)

# Defining the url that would be used to access the predictions 
@app.route('/api/predict/', methods=['POST'])

def predict():

    # loading the saved model 
    modelfile = 'model.sav' 
    model = pickle.load(open(modelfile, 'rb'))
    
    # getting the json data from the API request 
    jsonfile = request.get_json()

    # Converting the json data into a dataframe 
    data = pd.read_json(eval(json.dumps(jsonfile['X_test'])),orient='index')
    
    # defining a dictionary for saving the response 
    res = dict()

    # using the model to predict lables on the requested data 
    ypred = model.predict(data)
    
    # Inserting labels and final classification accuracy into the dictionary 
    for i in range(len(ypred)):

            res[i] = ypred[i]
            
    res['score'] = accuracy_score(jsonfile['y_test'], ypred)
    
    # returning a json object 
    return jsonify(res['score'])   


if __name__ == '__main__':
    
    print("loaded OK")
    
    # Running the app 
    app.run(threaded=True)
    
    pass