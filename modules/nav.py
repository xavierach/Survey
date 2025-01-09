import streamlit as st

def NavbarSurvey():
    with st.sidebar:
        st.page_link("pages/page_1.py", label="Surveys")
        st.page_link("pages/page_2.py", label="Demographic Details")
        st.page_link("pages/page_3.py", label="Education and Employment Details")
        st.page_link("pages/page_4.py", label="Persons Not Working")
        st.page_link("pages/page_5.py", label="Persons Outside The Labour Force")