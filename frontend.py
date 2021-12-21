import streamlit as st
import pandas as pd
import numpy as np


st.header("Brisbane Activities (Beta) 👀")


activity_df = pd.read_csv('NewActivity.csv')


price = activity_df['Price'].unique()
time = activity_df['Time'].unique()
duration = activity_df['Duration'].unique()


priceop = st.multiselect('What Price Range?',price)
timeop = st.multiselect('What Time Range?',time)
durationop = st.multiselect('What Duration Range?',duration)

activity_df = activity_df[activity_df["Price"].isin(priceop)]
activity_df = activity_df[activity_df["Time"].isin(timeop)]
activity_df = activity_df[activity_df["Duration"].isin(durationop)]
print(activity_df)
col1, col2 = st.columns(2)



with col1:
     st.map(activity_df) 
with col2:
     st.table(activity_df[["Short Activity","Price"]])
print(price)