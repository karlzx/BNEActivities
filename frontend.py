import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import folium
import time
from streamlit_folium import folium_static
st.set_page_config(layout="wide")
st.header("🔥 Brisbane Activities (Beta)🔥 ")
st.write("Can't figure out what to do? Enter the filters below and find out what you can do around bris. More features TBA")

activity_df = pd.read_csv('NewActivity.csv')



price = activity_df['Price'].unique()
times = activity_df['Time'].unique()
duration = activity_df['Duration'].unique()
tag = activity_df['Tag'].unique()

st.write('___________')

col11, col12, col13 = st.columns(3)
# col1, col2 = st.columns(2)
with col11:
    st.header('Filter')
    priceop = st.multiselect('What Price Range?',price)
    timeop = st.multiselect('What Time Range?',times)
    durationop = st.multiselect('What Duration Range?',duration)
    tagop = st.multiselect('What activity type?',tag)


if len(priceop) is not 0:
    activity_df = activity_df[activity_df["Price"].isin(priceop)]
if len(timeop) is not 0:
    activity_df = activity_df[activity_df["Time"].isin(timeop)]
if len(durationop) is not 0:
    activity_df = activity_df[activity_df["Duration"].isin(durationop)]
if len(tagop) is not 0:
    activity_df = activity_df[activity_df["Tag"].isin(tagop)]


pages = range(1,len(activity_df),10)





# print(locs)

with col12:
    st.header('Activities')
    if len(pages)>1:
        page = st.slider('Page', 1, len(pages), 1)

        if page is not len(pages):
            culled_df = activity_df[pages[page-1]-1:pages[page]-1]
        else:
            culled_df = activity_df[pages[page-1]-1:len(activity_df)]

    else:
        culled_df = activity_df

    st.table(culled_df[["Tag","Short Activity","Price","Time","Duration"]])

    main_map = folium.Map(location=(-27.4705, 153.0260), zoom_start=10)

    for index, row in culled_df.iterrows():
        folium.Marker(
        location=[row['latitude'],  row['longitude']],
        popup=row['Short Activity'],
        icon=folium.Icon(color="red", icon="info-sign"),
        ).add_to(main_map)

with col13:
    st.header('Map')
    folium_static(main_map)
st.write('___________')
st.header("Can't Decide?")
if st.button('Pick a Random Activity for me'):
    with st.spinner('Randomising...'):
        time.sleep(1)
    st.success("Here's your activity!")
    chosen = activity_df.sample()
    st.write(chosen)
    st.balloons()