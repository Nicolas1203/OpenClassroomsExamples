import numpy as np
import pickle

from sklearn import datasets
from flask import Flask, request


# Load the dataset. We will take an index as input
# and output the model prediction for the corresponding data 
# in the database (it could also be something else, like an id)
diabetes_X, _ = datasets.load_diabetes(return_X_y=True)
# Use only one feature
diabetes_X = diabetes_X[:, np.newaxis, 2]

# Load some pretrained modle
model = pickle.load(open('trained_model.pkl', 'rb'))

# Init Flask app
app = Flask(__name__)

@app.route("/predict", methods=['GET'])
def predict():
	# Get the index from the request parameter
	data_index = request.args.get('index')
	# Get the corresponding input from database
	input = diabetes_X[int(data_index)]
	# Return the model prediction
	model_prediction = model.predict([input])
	# The type of the return must be string, dict, tuple for Flask
	return str(model_prediction)

app.add_url_rule('/predict', 'predict', predict)
app.run()
