'''
Created on Oct 11, 2018

@author: Sarwat Fatima
'''

import pandas as pd 
import datetime

# This function was used to extract only date from dataframe column
def extract_date(series):
    temp = pd.DatetimeIndex(series)
    return temp.date

# This function was used to convert the string date into a datetime type. 
def convert_date(string_date):
    d = datetime.datetime.strptime(string_date, '%Y-%m-%d').date()
    return d

# This function was used to clean the dataframe, extract new features and filtered relevant features
def clean_data(df):
    # Dropping unneccessary column names 
    df.drop(['name','category','main_category', 'country', 'currency', 'goal','pledged',
             'usd pledged'], axis=1, inplace=True)
    # Preprocessing the dates 
    df['launched'] = extract_date(df['launched'])
    df['deadline'] = df['deadline'].apply(lambda x: convert_date(x))
    
    # Extracting derived feature from dates i.e. number of days the campaign was run 
    df['campaign_days'] = (df['deadline'] - df['launched']) / pd.offsets.Day(1)
    df.drop(['launched', 'deadline'], axis=1, inplace=True)
    
    # Replaced the text labels into a number label 
    df['state'].replace('failed', 0, inplace=True)
    df['state'].replace('canceled', 0, inplace=True)
    df['state'].replace('successful', 1, inplace=True)
    
    # Creating training data with labels 
    X = df[['backers', 'usd_pledged_real','usd_goal_real','campaign_days']]
    y = df['state'].get_values().tolist()
    
    return X, y

if __name__ == '__main__':
    pass