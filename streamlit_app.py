from vega_datasets import data
import streamlit as st
import altair as alt
import pandas as pd
import plotly.express as px

def main():
    df = pd.read_csv(st.file_uploader("Please upload a file for analysis",type=['csv'], accept_multiple_files=False,))
    page = st.sidebar.selectbox("Choose a page", ["Homepage", "Exploration"])

    if page == "Homepage":
        st.header("This is your data explorer.")
        st.write("Please select a page on the left.")
        st.write(df)
    elif page == "Exploration":
        st.title("Data Exploration")
        x_axis = st.selectbox("Choose a variable for the x-axis", df.columns, index=3)
        y_axis = st.selectbox("Choose a variable for the y-axis", df.columns, index=4)
        print(x_axis)
        fig = px.bar(df,x=x_axis,y=y_axis)
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)


if __name__ == "__main__":
    main()
