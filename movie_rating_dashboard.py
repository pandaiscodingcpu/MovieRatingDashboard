# LOAD AND INSPECT THE DATA
# CHECK FOR MISSING VALUES
# DATA CLEANING
import pandas as pd
import streamlit as st

# Load the merged data
data = pd.read_csv("cleaned_movie_data.csv")

st.title("Movie Ratings Dashboard")

genre = st.selectbox("Select Genre", data['genres'].unique())
filtered_data = data[data['genres'].str.contains(genre, na=False)]

st.write(f"Top Movies in {genre}")
st.dataframe(filtered_data[['title', 'rating']].sort_values(by='rating', ascending=False).head(10))