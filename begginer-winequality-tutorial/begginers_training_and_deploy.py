import pandas as pd
import numpy as np
import pickle
import flask
from sklearn import linear_model
from flask import request

# loading the dataset
ds = pd.read_csv('./winequality-red.csv', delimiter=",")

# getting a single column
label = ds['quality']

# getting all others columns except 'quality'
# axis: 0 select lines; 1 select columns;
features = ds.drop('quality', axis=1)

# prediction code
regression_model = linear_model.LinearRegression()
regression_model.fit(features, label)

# serializing the model to a file
pickle.dump(regression_model, open("./model.pkl", "wb"))

# loading the dumped model from file
model = pickle.load(open(file="./model.pkl", mode="rb"))

# creating a simple webserver
app = flask.Flask(__name__)
app.debug = True

@app.route('/hello', methods=['POST', 'GET'])
def index():
    # grabs the data tagged as 'name'
    name = request.args.get('name')
    # sending a hello back to the requester
    return "Hello " + name

@app.route('/predict', methods=['POST'])
def predict():
    # grabs a set of wine features from the request body
    feature_array = request.get_json()['feature_array']

    # our model prediction based on input array
    prediction = model.predict([feature_array]).tolist()

    # preparing a response object and storing the model's predictions
    response = {}
    response['predictions'] = prediction

    return flask.jsonify(prediction)

app.run(host='127.0.0.1', port=8080)