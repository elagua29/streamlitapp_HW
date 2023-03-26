import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

VSC_HW = pd.read_csv('VSC_HW.csv')

st.write(VSC_HW)

st.sidebar.header("Pick two variables for this scatterplot")
x_val = st.sidebar.selectbox("Pick your x-axis",VSC_HW.select_dtypes(include=np.number).columns.tolist())
y_val = st.sidebar.selectbox("Pick your y-axis",VSC_HW.select_dtypes(include=np.number).columns.tolist())

scatter = alt.Chart(VSC_HW, title=f"Correlation between {x_val} and {y_val}").mark_point().encode(
    alt.X(x_val,title=f"{x_val}"),
    alt.Y(y_val,title=f"{y_val}"),
    tooltip= [x_val,y_val])

st.altair_chart(scatter, use_container_width=True)

corr = round(VSC_HW[x_val].corr(VSC_HW[y_val]),2)
st.write(f"The correlation between {x_val} and {y_val} is {corr}")









