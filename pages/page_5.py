import streamlit as st
import numpy as np
import pandas as pd
import time
from modules.nav import NavbarSurvey
import json
import os

NavbarSurvey()

st.title("Answer Survey")

if "data" not in st.session_state:
    st.session_state.data = {}
    for i in ["name", "nric", "rls", "dob", "age", "sex", "race", "ident type", "stay", "sg stay", "marrital status", "acad & quali", "place", "certificates", "retirement", "curr status", "looking", "12months", "want to work", "availibility", "not working", "worked"]:
        st.session_state.data[i] = None

with st.form("Ouside_labour_force"):
    st.subheader("Persons Outside The Labour Force")

    not_looking = ["Pursuing full-time study (eg. Secondary, JC, ITE, Poly, private institution or University)", "Pursuing part-time study", "Awaiting the start of academic year", "Awaiting NS call-up", "Awaiting examination results", "Attending courses/training", "Housework", "Care for own children aged 12 and below", "Care for familites (including own children aged above 12 and grandchildren) / relatives", "Care for persons who are not family/relatives", "Doing voluntary/community work", "Poor health", "Permanently ill/disabled", "Retired / No desire to work due to old age", "Have sufficient financial support/means", "Believes no suitable work available", "Employers' discrimination (eg. prefer younger workers)", "Taking a break", "Foreigner without work pass", "Others"]
    if st.session_state.data.get("not looking") == None:
        st.session_state.data["not looking"] = st.radio("What is our main reason for not working and not looking for a job?", not_looking, index=None)
    else:
        st.session_state.data["not looking"] = st.radio("What is our main reason for not working and not looking for a job?", not_looking, index=not_looking.index(st.session_state.data.get("not looking")))
    
    YN = ["Yes", "No"]
    if st.session_state.data.get("worked") == None:
            st.session_state.data["worked"] = st.radio("Have you ever worked before (Excluding Full-Time National Service)?", YN, index=None)
    else:
        st.session_state.data["worked"] = st.radio("Have you ever worked before (Excluding Full-Time National Service)?", YN, index=YN.index(st.session_state.data.get("worked")))

    if st.form_submit_button("Submit form"):
        file_name = "data" + str(st.session_state.mem_no) + ".json"
        st.session_state.mem_no = st.session_state.mem_no + 1
        st.session_state.data["dob"] = str(st.session_state.data["dob"])
        file_path = os.path.join('export', file_name)
        # Write the data to the JSON file
        with open(file_path, 'w') as json_file:
            json.dump(st.session_state.data, json_file, indent=4)

        st.session_state.data = {}
        time.sleep(5)
        st.switch_page("pages/page_2.py")
    
    if st.form_submit_button(label="Back"):
        st.switch_page("pages/page_4.py")
