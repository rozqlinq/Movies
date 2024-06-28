import matplotlib
import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import pickle
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


pickled_model = pickle.load(open('movies_classifier_model.pkl', 'rb'))

# APP INTERFACE
st.set_page_config(layout='centered')

st.title('Movie Box Office Success Predictor')
st.write("""Welcome to Movie Box Office Success Predictor app!
            bla bla bla""")

categories = {'AAA': 3, 'A': 2, 'B': 1, 'C':0}

with st.form(key = 'information', clear_on_submit=True):
    budget = st.number_input('Enter approximate BUDGET of your movie (in $ mln)')
    marketing_spend = st.number_input('Enter approximate MARKETING SPEND of your movie (in $ mln)')
    duration = st.number_input('Enter approximate DURATION of your movie (in min)')
    social_media = st.number_input('Enter approximate score of SOCIAL MEDIA BUZZ of your movie (out of 100)')
    num_screens = st.number_input('Enter approximate NUMBER OF SCREENS of your movie')
    mov_cat = st.selectbox('Enter CATEGORY of your movie',
                       ['AAA','A', 'B', 'C'])
    genre = st.selectbox('Enter GENRE of your movie',
                       ['Drama','Horror', 'Action', 'Sci-Fi', 'Comedy'])

    genres = {'Action': False, 'Comedy': False, 'Drama': False, 'Horror':False, 'Sci-Fi':False}
    genres[genre] = True
    
    # PREDICTION
    if st.form_submit_button('Predict'):
        data = pd.DataFrame({
            'Movie_Category': categories[mov_cat],
            'Budget': [budget],
            'Duration': [duration],
            'Num_Screens': [num_screens],
            'Marketing_Spend':[marketing_spend],
            'Social_Media_Buzz': [social_media],
            'Genre_Action': genres['Action'],
            'Genre_Comedy': genres['Comedy'],
            'Genre_Drama': genres['Drama'],
            'Genre_Horror': genres['Horror'],
            'Genre_Sci-Fi': genres['Sci-Fi']
        })
        prediction = pickled_model.predict(data)
     


        result = ''
        if prediction[0]==0:
                    result = 'Low'
        elif prediction[0]==1:
                    result = 'Medium'
        elif prediction[0]==2:
                    result = 'High'


        st.success(f"Predicted Probability: result")




