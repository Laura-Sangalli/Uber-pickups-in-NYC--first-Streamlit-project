import streamlit as st
import pandas as pd
import numpy as np

# Define the title 
st.title('Uber pickups in NYC')

date_column = 'date/time'
url = 'https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'

# The utilization of the function bellow is read the csv file and change the type
# of the date/time column for datetime format, instead of object format. 
@st.cache_data
def load_data(nrows):
    data = pd.read_csv(url, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[date_column] = pd.to_datetime(data[date_column])
    return data

# these lines will be showed in the app, sinalizing the intern process ocuring
# the load_data function is a function to show the data in the app 
data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state = st.text('Loading data... done!')

# bellow, we finally will show the data in the app 
st.subheader('Raw data')
st.write(data)

# creation of a histogram that sows the number of pickups by hour in NYC
st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[date_column].dt.hour, bins = 24, range=(0,24))[0]
st.bar_chart(hist_values)

# creating a map of the distribution of uber pickups along NYC 
st.subheader('Map of all pickups')
st.map(data)