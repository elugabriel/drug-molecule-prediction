from flask import Flask, render_template, url_for, flash, redirect, request
import pickle
import numpy as np
from sklearn import *

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    FASA_H = request.form.get("FASA_H")
    FASA_P = request.form.get("FASA_P")
    PEOE_VSA_FHYD = request.form.get("PEOE_VSA_FHYD")
    PEOE_VSA_FPNEG = request.form.get("PEOE_VSA_FPNEG")
    PEOE_VSA_FPOL = request.form.get("PEOE_VSA_FPOL")
    Q_VSA_FHYD = request.form.get("Q_VSA_FHYD")
    Q_VSA_FPNEG = request.form.get("Q_VSA_FPNEG")
    Q_VSA_FPOL = request.form.get("Q_VSA_FPOL")
    Q_VSA_PNEG = request.form.get("Q_VSA_PNEG")
    SlogP = request.form.get("SlogP")
    
    num = [float(x) for x in request.form.values()]
    value = [np.array(num)]
    prediction = model.predict(value)

    """
    if prediction ==1:
        prediction = "Active"
    else:
        prediction = "Non-active"
    """
    
    return render_template('index.html', prediction=prediction)



if __name__ == '__main__':
    app.run(debug=True)