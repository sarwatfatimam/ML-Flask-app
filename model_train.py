'''
Created on Oct 11, 2018

@author: Sarwat Fatima
'''

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from model_functions import clean_data
import pickle, json
    
if __name__ == '__main__':
    
    # Reading data into a dataframe 
    df = pd.read_csv("ks-projects-201801.csv")
    
    # file used for storing the model 
    model_filename = 'model.sav'
    
    # cleaning data i.e. removing unnecessary columns and getting derived features
    X, y = clean_data(df)
    
    # Splitting data into 80 20 ratio
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    
    # creating a json object with X_test and y_test 
    X_test = X_test.to_json(orient='index')
    test_data = {'X_test': X_test, 'y_test': y_test}
    
    #json_data = json.dumps(train_data)
    
    # Saving the test data into a json file as well 
    #pickle.dump(json_data, open(test_filename, 'wb'))
    with open('test_data.json', 'w') as outfile:
            json.dump(test_data, outfile)
    
    # Training the classifier
    clf = LogisticRegression(random_state=0).fit(X_train, y_train)
    
    # Saving the trained classifier into a file
    pickle.dump(clf, open(model_filename, 'wb'))
    
    pass