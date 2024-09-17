import os 
import numpy as np    
import pandas as pd   
import pydeck as pdk  
import streamlit as st   
# Setting page config wide mode and adding title favicon
st.set_page_config(layout="wide",page_title="NYC Ridesharing Demo",page_icon=":taxi:")
#Load Data Once
@st.cache_resource
def load_data():
    path = "uber-raw-data-set14.csv.gz"
    if not os.path.isfile(path):
        path = f"https://github.com/streamlit/demo-uber-nyc-pickups/raw/main/{path}"
    data = pd.read_csv(
        path,
        nrows=100000,   # approx 10% of data
        names= [
            "date/time",
            "lat",
            "lon",

        ],
        skiprows=1   # don't read header

    )  