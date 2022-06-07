import streamlit as st
import numpy as np
import pandas as pd
from PIL import  Image

def app():
    #st.markdown("## Data Upload")
    st.title("Tracking Dashboard")
    display = Image.open('MindAffect_Logo.png')
    display = np.array(display)
    st.image(display, width=400)
    # Upload the dataset and save as csv
    st.markdown("### Upload a csv file for analysis")
    st.write("\n")
    uploaded_file = st.file_uploader("Choose a file", type = ['csv', 'xlsx'])
    global data
    if uploaded_file is not None:
        try:
            data = pd.read_csv(uploaded_file)
        except Exception as e:
            print(e)
            data = pd.read_excel(uploaded_file)

    if st.button("Load Data"):
        
        # Raw data 
        st.dataframe(data)
        data.to_csv('data/main_data.csv', index=False)
        numeric_cols = data.select_dtypes(include=np.number).columns.tolist()
        categorical_cols = list(set(list(data.columns)) - set(numeric_cols))
        
