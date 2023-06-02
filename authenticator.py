import streamlit as st
import pandas as pd
from xgboost import XGBClassifier

header=st.container()
dataset=st.container()
features=st.container()
model=st.container()
prediction=st.container()

@st.cache
def get_data(file_name):
	bank_notes=pd.read_csv(file_name)
	return bank_notes

with header:
	st.title('Authenticate your notes')
	st.text('Use this app to catch counterfeit bills')


with dataset:
	st.header('Bank note authentication')
	st.text('Data from the UCI ML repository')
	st.text('Check out a random sample of the data used')

	bank_notes=get_data('data-banknote-authentication.csv')
	st.write(bank_notes.sample(5))

with features:
	st.header('Relevant features')
	
	st.text('Enter the characteristics of your scanned note')
	
	var_wav, skew_wav=st.columns(2)
	Variance_Wavelet=var_wav.number_input('Variance Wavelet', min_value=-20.0, max_value=20.0, step=0.1)
	Skewness_Wavelet=skew_wav.number_input('Skewness Wavelet', min_value=-20.0, max_value=20.0, step=0.1)

	cur_wav,img_ent=st.columns(2)
	Curtosis_Wavelet=cur_wav.number_input('Curtosis_Wavelet', min_value=-20.0, max_value=20.0, step=0.1)
	Image_Entropy=img_ent.number_input('Image_Entropy', min_value=-20.0, max_value=20.0, step=0.1)



with model:
	X=bank_notes.drop('Class', axis=1).values
	y=bank_notes['Class'].values

	xgbc=XGBClassifier(random_state=101)
	xgbc.fit(X,y)



with prediction:
	if st.button('Predict'):
		pred=xgbc.predict([[Variance_Wavelet, Skewness_Wavelet, Curtosis_Wavelet, Image_Entropy]])

		if pred==0:
			st.text('Your note is authentic!')
		else:
			st.text('Your note is counterfeit!')




