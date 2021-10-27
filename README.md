# Car Price Prediction  <img src = "https://cdn-icons.flaticon.com/png/512/1300/premium/1300302.png?token=exp=1635356767~hmac=9226ae1acbcf8c23fbb188d55bd0b9e8" width="48">

This repository consists of files required for end to end implementation and deployment of Machine Learning Car Price Prediction web application created with Flask and deployed on the Heroku platform.

## Table Of Contents
* [App Link](#app-link)
* [About the App](#about-the-app)
* [Deployment on Heroku](#deployment-on-heroku)
* [Technologies Used](#technologies-used)

## App Link
If you want to view the deployed model, click on the following link:
[https://carpricepredictionv1.herokuapp.com/](https://carpricepredictionv1.herokuapp.com/)

A glimpse of the web app:

![APP GIF](https://github.com/kshitij-raj/Car-Price-Prediction/blob/main/readme_resources/App.gif)

• If you encounter this webapp as shown in the picture given below, it is occuring just because **free dynos for this particular month provided by the Heroku platform have been completely used.** You can access the webpage on 1st of the next month.

![Heroku-Error](https://github.com/kshitij-raj/Car-Price-Prediction/blob/main/readme_resources/heroku_error.png)

## About the App
The Car Price Prediction is a flask web application which predicts car prices based on given independent features like Car_Name,	Year,	Selling_Price,	Present_Price,	Kms_Driven,	Fuel_Type,	Seller_Type,	Transmission, and Owner. The dataset is available at [Kaggle](https://www.kaggle.com/nehalbirla/vehicle-dataset-from-cardekho), and it's provided by cardekho.com. 

To install the required packages and libraries, run this command in the project directory after cloning the repository:
```bash
pip install -r requirements.txt
```
## Deployement on Heroku
Signup in order to create virtual app. You can either connect your github profile or download Heroku cli to manually to deploy this project.

[![](https://github.com/kshitij-raj/Car-Price-Prediction/blob/main/readme_resources/Heroku.png)](https://heroku.com)

The next step would be to follow the instruction given in the [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web app.

## Technologies Used
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [gunicorn](https://gunicorn.org/)
- [scikit learn](https://scikit-learn.org/stable/)
