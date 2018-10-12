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

app = Flask(__name__)

@app.route('/api/predict/', methods=['POST'])


def predict():
    
    jsonfile = request.get_json()

    data = pd.read_json(eval(json.dumps(jsonfile['X_test'])),orient='index')

    print(data)
    
    res = dict()

    ypred = model.predict(data)

    for i in range(len(ypred)):

            res[i] = ypred[i]
            
    res['score'] = accuracy_score(jsonfile['y_test'], ypred)
    
    print(res['score'])
    
    return jsonify(res['score'])        


if __name__ == '__main__':
    
    modelfile = 'finalized_model.sav' 

    model = pickle.load(open(modelfile, 'rb'))

    print("loaded OK")
    
    app.run(threaded=True)
    
    pass