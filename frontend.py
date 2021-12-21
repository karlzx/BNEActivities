import streamlit as st
import pandas as pd
import numpy as np


st.header("Brisbane Activities (Beta) 👀")
st.write("Can't figure out what to do? Enter the filters below and find out what you can do around bris. More features TBA")

activity_df = pd.read_csv('NewActivity.csv')


price = activity_df['Price'].unique()
time = activity_df['Time'].unique()
duration = activity_df['Duration'].unique()
tag = activity_df['Tag'].unique()


priceop = st.multiselect('What Price Range?',price)
timeop = st.multiselect('What Time Range?',time)
durationop = st.multiselect('What Duration Range?',duration)
tagop = st.multiselect('What Type of Activity Range?',tag)

activity_df = activity_df[activity_df["Price"].isin(priceop)]
activity_df = activity_df[activity_df["Time"].isin(timeop)]
activity_df = activity_df[activity_df["Duration"].isin(durationop)]
activity_df = activity_df[activity_df["Tag"].isin(tagop)]
print(activity_df)
col1, col2 = st.columns(2)



with col1:
     st.map(activity_df) 
with col2:
     st.table(activity_df[["Tag","Short Activity","Price","Time","Duration"]])
print(price)