'''
Created on Oct 11, 2018

@author: Sarwat Fatima
'''

import pandas as pd 
import datetime

def extract_date(series):
    temp = pd.DatetimeIndex(series)
    return temp.date

def convert_date(string_date):
    d = datetime.datetime.strptime(string_date, '%Y-%m-%d').date()
    return d

def clean_data(df):
    
    df.drop(['name','category','main_category', 'country', 'currency', 'goal','pledged',
             'usd pledged'], axis=1, inplace=True)
    df['launched'] = extract_date(df['launched'])
    df['deadline'] = df['deadline'].apply(lambda x: convert_date(x))
    df['campaign_days'] = (df['deadline'] - df['launched']) / pd.offsets.Day(1)
    df.drop(['launched', 'deadline'], axis=1, inplace=True)
    df['state'].replace('failed', 0, inplace=True)
    df['state'].replace('canceled', 0, inplace=True)
    df['state'].replace('successful', 1, inplace=True)
    
    X = df[['backers', 'usd_pledged_real','usd_goal_real','campaign_days']]
    y = df['state'].get_values().tolist()
    
    return X, y

if __name__ == '__main__':
    pass