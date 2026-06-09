import streamlit as st
import pandas as pd
import os

from modules.config import init_settings
from modules.data_loader import load_files
from modules.merger import merge_payroll
from modules.calculations import compute_salary

st.set_page_config(page_title="Smart Payroll", layout="wide")

init_settings()

st.title("💼 Smart Payroll Payslip Generator")

# SIDEBAR
menu = st.sidebar.selectbox("Menu", [
    "Dashboard",
    "Upload Payroll",
    "Employee Search",
    "Settings"
])

uploaded_files = st.file_uploader(
    "Upload Payroll Excel Files",
    type=["xlsx"],
    accept_multiple_files=True
)

if menu == "Upload Payroll":
    if uploaded_files:
        dfs = load_files(uploaded_files)

        st.success(f"{len(dfs)} files loaded")

        merged = merge_payroll(dfs, st.session_state.duplicate_rule)
        merged = compute_salary(merged)

        st.dataframe(merged)

        st.download_button(
            "Download Merged Payroll",
            merged.to_csv(index=False),
            "merged_payroll.csv"
        )

elif menu == "Dashboard":
    st.metric("Employees", 120)
    st.metric("Total Payroll", "₦50,000,000")
    st.metric("Net Salary", "₦45,000,000")

elif menu == "Settings":
    st.text_input("Company Name", key="company_name")
    st.text_input("Address", key="company_address")
    st.selectbox("Duplicate Rule", ["sum", "first", "last"], key="duplicate_rule")
