import pandas as pd
import streamlit as st

REQUIRED_COLUMNS = ["STAFF NAME"]

def load_files(files):
    dataframes = []

    for file in files:
        df = pd.read_excel(file, engine="openpyxl")

        # Clean columns
        df.columns = df.columns.str.strip().str.upper()

        # Drop empty rows
        df.dropna(how="all", inplace=True)

        # Validate
        if "STAFF NAME" not in df.columns:
            st.error(f"{file.name} missing STAFF NAME column")
            continue

        dataframes.append(df)

    return dataframes
