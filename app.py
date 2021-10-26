from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
import os

path = os.path.join('Models','randoforest_regression_model.pkl')

app = Flask(__name__)
model = pickle.load(open(path,'rb'))


@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict",methods=['POST'])
def predict():
    if request.method == 'POST':
        current_Year = 2021 
        Year = int(request.form['Year'])
        if Year > current_Year:
            return render_template('index.html',prediction_text="You can't sell this car")
        Present_Price = int(request.form['Present_Price'])
        Kms_Driven = int(request.form['Kms_Driven'])
        Owner = int(request.form['Owner'])
        Fuel_Type_Petrol = request.form['Fuel_Type_Petrol']

        if Fuel_Type_Petrol == 'Petrol':
            Fuel_Type_Petrol = 1
            Fuel_Type_Diesel = 0

        elif Fuel_Type_Petrol == 'Diesel':
            Fuel_Type_Petrol = 0
            Fuel_Type_Diesel = 1
        else:
            Fuel_Type_Petrol = 0
            Fuel_Type_Diesel = 0
        
        Year =  current_Year - Year

        Seller_Type_Individual = request.form['Seller_Type_Individual']
        if Seller_Type_Individual == 'Individual':
            Seller_Type_Individual = 1
        else:
            Seller_Type_Individual = 0

        Transmission_Manual = request.form['Transmission_Manual']
        if Transmission_Manual == 'Manual':
            Transmission_Manual = 1
        else:
            Transmission_Manual = 0

        prediction = model.predict([[Present_Price,Kms_Driven,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual]])
        output = round(prediction[0],0)

        if output < 0:
            return render_template('index.html',prediction_text="You can't sell this car")
        else:
            return render_template('index.html',prediction_text="You can sell this car at {}".format(output))
    else:
        render_template('templates/index.html')

if __name__ == "__main__":
    app.run(debug=True)
    app.config['TEMPLATES_AUTO_RELOAD'] = True