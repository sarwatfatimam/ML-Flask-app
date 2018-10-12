'''
Created on Oct 12, 2018

@author: Sarwat Fatima

'''

import requests, json
from model_functions import clean_data
from sklearn.model_selection import train_test_split
import pandas as pd

BASE_URL = 'http://127.0.0.1:5000/api/predict/'
url = '[http://127.0.0.1:5000/api/makecalc/](http://127.0.0.1:5000/api/makecalc/)'

def request():
    
    df = pd.read_csv("ks-projects-201801.csv")
    
    X, y = clean_data(df)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    
    X_test = X_test.to_json(orient='index')
    
    train_data = {'X_test': X_test, 'y_test': y_test}
    
    json_data = json.dumps(train_data)
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    response = requests.post(BASE_URL, data=json_data, headers=headers)
    
    return response

if __name__ == '__main__':
    
    r = request()
    print(r, r.text)
    
    pass