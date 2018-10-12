'''
Created on Oct 11, 2018

@author: Sarwat Fatima
'''

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from model_functions import clean_data
import pickle
    
if __name__ == '__main__':
    
    df = pd.read_csv("ks-projects-201801.csv")
    filename = 'finalized_model.sav'
    
    X, y = clean_data(df)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    
    clf = LogisticRegression(random_state=0).fit(X_train, y_train)
    
    pickle.dump(clf, open(filename, 'wb'))
    
    pass