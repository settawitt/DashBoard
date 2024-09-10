import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt  
# Add title and intro text
st.title('Earthquake Data Explorer')
st.text('This web app to allow exploration Earthquake Data')
# Create file uploader object
upload_file = st.file_uploader('Upload file containing earthquake data')
# check see if a file has been uploaded
if upload_file is not None:
  
    # Read file to dataframe using pandas
    df = pd.read_csv(upload_file)
    # creating session dataframe statistics
    st.header('Statistics of DataFrame')
    st.write(df.describe())
    
    # Create section dataframe header
    st.header('Header DataFrame')
    st.write(df.head())
    # Create section matplotlib figure
    st.header('Plot Data')
    fig , ax = plt.subplots(1,1)
    ax.scatter(x=df['Depth'],y=df['Magnitude'])
    ax.set_xlabel('Depth')
    ax.set_ylabel('Magnitude')
    st.pyplot(fig)