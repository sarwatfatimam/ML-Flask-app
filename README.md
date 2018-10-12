# ML-Flask-app
This repository contains a Flask API which predicts the success or failure of a Kickstarter projects. 

## Data

The data was taken from this link: https://www.kaggle.com/kemical/kickstarter-projects#ks-projects-201801.csv 

## Running the app on Windows Powershell 

1. Open Windows Powershell and go to the folder containing the code. Run following commands to run flask server. 


```
$env:FLASK_APP = "model_predict.py"
$env:FLASK_env = "development"
flask run 

```
2. Open another Windows Powershell and go to the folder containing the code. Run the following commands to send request to the flask server. 

```
python api_request.py

```

3. If everything works fine, it should return the accuracy score. 

