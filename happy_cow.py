import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('happy.csv')
options = [i.replace ("_", " ").title () for i in df.columns.values]

st.title("In Search for Happiness")
option_x = st.selectbox("Select data X axis",
                      options)
option_y = st.selectbox("Select data Y axis",
                      options)
st.subheader(f"{option_x} and {option_y}")

x_axis = df.iloc[:, options.index (option_x)]
y_axis = df.iloc[:, options.index (option_y)]

figure = px.scatter(x=x_axis, y=y_axis, labels={"x": option_x, "y": option_y})
st.plotly_chart (figure)