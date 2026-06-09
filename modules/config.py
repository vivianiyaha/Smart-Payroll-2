import streamlit as st

def init_settings():
    if "company_name" not in st.session_state:
        st.session_state.company_name = "Smart Payroll Ltd"
        st.session_state.company_address = "Lagos, Nigeria"
        st.session_state.month = "June"
        st.session_state.year = "2026"
        st.session_state.duplicate_rule = "Sum Values"
        st.session_state.logo = None
