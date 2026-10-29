import streamlit as st
import pandas as pd
st.set_page_config(page_title="AI Data Quality Copilot", layout="wide")
st.title("AI Data Quality & Root-Cause Analysis Copilot")
st.write("Upload a CSV dataset to identify missing values, duplicate records, and potential data quality issues.")
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("Dataset uploaded!")
    col1,col2,col3 = st.columns(3)
    col1.metric("Total Rows", df.shape[0])
    col2.metric("Total Columns", df.shape[1])
    col3.metric("Duplicate Rows", int(df.duplicated().sum()))
    st.subheader("Missing Values")
    missing = df.isnull().sum()
    missing = missing[missing>0].sort_values(ascending=False)
    if not missing.empty:
        st.bar_chart(missing)
    st.subheader("Data Quality Report")
    st.dataframe(df.isnull().sum().reset_index(name="Missing"))
    st.download_button("Download Report", data=df.isnull().sum().to_csv().encode(), file_name="report.csv")
