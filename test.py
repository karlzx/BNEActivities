import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import folium
from streamlit_folium import folium_static
st.header("Testing Instance")

main_map = folium.Map(location=(-27.4705, 153.0260), zoom_start=10)

#
folium.Marker(
    location=[-27.3595,  153.0382],
    # popup=data.iloc[i]['name'],
).add_to(main_map)

# folium.CircleMarker(location=[-27.3595, 153.0382],
#         fill=True,
#         color=None,
#         fill_opacity=0.7,
#         radius=5,
#         ).add_to(main_map)


folium_static(main_map)
