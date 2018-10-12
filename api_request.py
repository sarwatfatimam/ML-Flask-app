'''
Created on Oct 12, 2018

@author: Sarwat Fatima

'''

import requests, json

# Defining the base url to be used for sending the request 
BASE_URL = 'http://127.0.0.1:5000/api/predict/'

def request():
    
    # loading the json file which contains the 20% of testing dataset
    datafile = open ('test_data.json').read()
    test_data = json.loads(datafile)     

    # Sending the json data in the request 
    json_data = json.dumps(test_data)
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    response = requests.post(BASE_URL, data=json_data, headers=headers)
    
    return response

if __name__ == '__main__':
    
    r = request()
    print(r, r.text)
    
    pass