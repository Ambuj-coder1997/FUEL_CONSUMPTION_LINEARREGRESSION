import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data


data = load_model()

regressor = data["model"]


def show_predict_page():
    st.title("Software for Fuel Consumption Prediction in L/h using Linear Regression Model")
    st.sidebar.image("https://upload.wikimedia.org/wikipedia/en/thumb/1/1c/IIT_Kharagpur_Logo.svg/268px-IIT_Kharagpur_Logo.svg.png?20160427114101",
                     use_column_width=True)
    st.write("""### We need some information to predict the Fuel Consumption""")

    Tractor_PTO = st.number_input('Enter PTO Power')
    Engine_Speed = st.number_input('Enter Engine Speed')
    Speed_Depression = st.number_input('Enter Speed Depression')

    ok = st.button("Calculate Fuel Consumption")
    if ok:
        X = np.array([[Tractor_PTO, Engine_Speed, Speed_Depression]])
        X = X.astype(float)

        salary = regressor.predict(X)
        st.subheader(f"The estimated Fuel Consumption(L/h) is {salary[0]:.2f}")



