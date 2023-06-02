# Authenticating Bank Notes
![vlcsnap-2016-12-04-10h40m29s884](https://github.com/Sabacon/Authenticating-Bank-Notes-with-XGBoost-Classifier/assets/121859090/8439ef9d-8866-4e0d-8903-fb72c2cabd56)

## Problem definition
Predicting the authenticity of bank notes. This is a binary classification task. 

## Data
Data was extracted from both authentic and forged notes using an industrial camera. Wavelet transformation tool was used to extract features from the digitized images.

The features are:
* Variance_Wavelet
* Skewness_Wavelet
* Curtosis_Wavelet
* Image_Entropy

More about the data can be found at the UCI Machine Learning Repository. https://archive.ics.edu/ml/datasets/banknote+authentication

## Process
Data cleaning and feature engineering was not necessary.

Jumped right into modelling after EDA.

I trained tree based models and upon validation, XGBoost classifier rose to the top.

Hyperparameter tuning was not required.

## Results
All the trained model performed superbly with the selected model posting scores greater than 0.99 on all the metrics. [Take a look](https://sabacon-authenticating-bank-notes-with-xgb-authenticator-qr8oee.streamlit.app/)

## Deployment
I built a simple app using Streamlit to classify the scanned notes.
![Screenshot (11449)](https://github.com/Sabacon/Authenticating-Bank-Notes-with-XGBoost-Classifier/assets/121859090/939d9c3f-aa4c-442c-be8a-83cded0b00c3)
