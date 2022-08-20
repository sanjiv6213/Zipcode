import streamlit as st
from geopy.geocoders import Nominatim
import pandas as pd

st.title("US Zipcodes")
file=pd.read_csv("F:\VScode\sampleprgm\zipcodes\zipcodes.csv")
geolocator = Nominatim(user_agent="geoapiExercises")

state=list(file['State Name'].drop_duplicates())
zipcode=list(file['Zip Code'].drop_duplicates())

#states=st.selectbox("States:",state)
#st.write("The state is",states)

zipcodes=st.selectbox("Zipcodes",zipcode)
st.write("The zipcode is",zipcodes)


location = geolocator.geocode(zipcodes)
st.header(location)




