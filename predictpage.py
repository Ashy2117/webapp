import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

def show_predictpage():
     st.title("Weather Prediction")

     st.write("""### We need some information to predict""")

     state=(
     "bengaluru",
     "india"
        )

     state = st.selectbox("state",state)


     import datetime
     user_date = st.date_input("Select your Date",
                            value = datetime.date(2020, 1, 1),
                            min_value = datetime.date(2010, 1, 12),
                            max_value = datetime.date(2025, 1, 12)
                            )
     

     st.write(user_date)

     ok= st.button("Predict")
     if ok:
        X= np.array([[user_date]])
        print(X)

        salary= (X)
        