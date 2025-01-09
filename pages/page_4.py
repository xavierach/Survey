import streamlit as st
import numpy as np
import pandas as pd
import time
from modules.nav import NavbarSurvey

NavbarSurvey()

st.title("Answer Survey")

if "data" not in st.session_state:
    st.session_state.data = {}
    for i in ["name", "nric", "rls", "dob", "age", "sex", "race", "ident type", "stay", "sg stay", "marrital status", "acad & quali", "place", "certificates", "retirement", "curr status", "looking", "12months", "want to work", "availibility", "not working", "worked"]:
        st.session_state.data[i] = None

with st.form(key="Not_working"):
    st.subheader("Persons Not Working")

    YN = ["Yes" ,"No"]
    if st.session_state.data.get("looking") == None:
        st.session_state.data["looking"] = st.radio("Were you actively looking for jobs in the past 4 weeks?", YN, index=None)
    else:
        st.session_state.data["looking"] = st.radio("Were you actively looking for jobs in the past 4 weeks?", YN, index=YN.index(st.session_state.data.get("looking")))
    
    if st.session_state.data.get("12months") == None:
        st.session_state.data["12months"] = st.radio("If no, what about any point in time from 12 months ago till now", YN, index=None)
    else:
        st.session_state.data["12months"] = st.radio("If no, what about any point in time from 12 months ago till now", YN, index=YN.index(st.session_state.data.get("12months")))
    
    if st.session_state.data.get("want to work") == None:
        st.session_state.data["want to work"] = st.radio("At present, do you want to work?", YN, index=None)
    else:
        st.session_state.data["want to work"] = st.radio("At present, do you want to work?", YN, index=YN.index(st.session_state.data.get("want to work")))
    
    if st.session_state.data.get("availibility") == None:
        st.session_state.data["availibility"] = st.radio("Are you availble to work in the next 2 weeks?", YN, index=None)
    else:
        st.session_state.data["availibility"] = st.radio("Are you availble to work in the next 2 weeks?", YN, index=YN.index(st.session_state.data.get("availibility")))

    if st.form_submit_button(label="Continue"):
        st.switch_page("pages/page_5.py")
        time.sleep(2)

    if st.form_submit_button(label="Back"):
        st.switch_page("pages/page_3.py")