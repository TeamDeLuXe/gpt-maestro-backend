import streamlit as st
import pandas as pd

data = pd.read_csv("data.csv")
st.title("Dashboard interactif")
st.line_chart(data['valeurs'])