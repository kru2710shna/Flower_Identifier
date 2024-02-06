import numpy as np
from flask import Flask
from flask import request, jsonify  ,render_template
import pickle 
# create app name 
app = Flask(__name__)

#load the picke model 
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/predict", methods = ["POST"])
def Predict():
    float_features = [float(c) for c in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    
    return render_template("index.html", prediction_text= "The flower is {}".format(prediction))

if __name__ == "__main__":
    app.run(debug=True)