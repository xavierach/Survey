import streamlit as st
import numpy as np
import pandas as pd
import time
from modules.nav import NavbarSurvey

NavbarSurvey()

st.title("Answer Survey")

if "mem_no" not in st.session_state:
    st.session_state.mem_no = 1

st.write("Member Number")
st.write(st.session_state.mem_no)

if "data" not in st.session_state:
    st.session_state.data = {}
    for i in ["name", "nric", "rls", "dob", "age", "sex", "race", "ident type", "stay", "sg stay", "marital status", "acad & quali", "place", "certificates", "retirement", "curr status", "looking", "12months", "want to work", "availability", "not looking", "worked"]:
        st.session_state.data[i] = None

with st.form(key="Demographic"):
    st.subheader("Demographic Details")

    st.session_state.data["name"] = st.text_input("Name", value=st.session_state.data.get("name"))
    st.session_state.data["nric"] = st.text_input("NRIC / Birth Certificate / FIN No", value=st.session_state.data.get("nric"))
    st.session_state.data["rls"] = st.text_input("Relationship to Household Reference Person", value=st.session_state.data.get("rls"))
    st.session_state.data["dob"] = st.date_input("Date of birth", value=st.session_state.data.get("dob"))
    st.session_state.data["age"] = st.number_input("Age", step=1, min_value=0, value=st.session_state.data.get("age"))

    sex = ["Male", "Female", "Prefer Not To Say"]
    if st.session_state.data.get("sex") == None:
        st.session_state.data["sex"] = st.radio("Sex", sex, index=None)
    else:
        st.session_state.data["sex"] = st.radio("Sex", sex, index=sex.index(st.session_state.data.get("sex")))
    
    race =["Chinese", "Malay", "Indian", "Eurasian", "Others"]
    if st.session_state.data.get("race") == None:
        st.session_state.data["race"] = st.radio("Race", race, index=None)
    else:
        st.session_state.data["race"] = st.radio("Race", race, index=race.index(st.session_state.data.get("race")))

    types = ["Singapore Citizen", " Singapore Permanent Resident (PR)", "Foreigner on Employment Pass", "Foreigner on S Pass", "Foreigner on Work Permit", "Foreigner on Student's Pass", "Foreigner on Social Visit pass (eg. Long-Term Visit Pass(LTVP), Long-Term Visit Pass Plus(LTVP+))", "Foreigner on Dependent's Pass", "New born foreign baby or child without identification document yet", "Forigner on Training Pass", "Foreigner on other types of identification"]
    if st.session_state.data.get("ident type") == None:
            st.session_state.data["ident type"] = st.radio("Identification Type", types, index=None)
    else:
        st.session_state.data["ident type"] = st.radio("Identification Type", types, index=types.index(st.session_state.data.get("ident type")))

    stay = ["Singapore", "Outside Singaore"]
    if st.session_state.data.get("stay") == None:
        st.session_state.data["stay"] = st.radio("Where are you currently staying?", stay, index=None)
    else:
        st.session_state.data["stay"] = st.radio("Where are you currently staying?", stay, index=stay.index(st.session_state.data.get("stay")))

    sg_stay = ["Residential Unit", "Institutional Unit (eg. old age home, prison. reformatory centre)"]
    if st.session_state.data.get("sg stay") == None:
        st.session_state.data["sg stay"] = st.radio("Where do you stay in Singapore", sg_stay, index=None)
    else:
        st.session_state.data["sg stay"] = st.radio("Where do you stay in Singapore", sg_stay, index=sg_stay.index(st.session_state.data.get("sg stay")))

    marrital_status = ["Single", "Married", "Widowed", "Divorced", "Separated"]
    if st.session_state.data.get("marital status") == None:
            st.session_state.data["marital status"] = st.radio("Marital Status", marrital_status, index=None)
    else:
        st.session_state.data["marital status"] = st.radio("Marital Status", marrital_status, index=marrital_status.index(st.session_state.data.get("marital status")))

    if st.form_submit_button(label="Continue"):
        st.switch_page("pages/page_3.py")
        time.sleep(2)
    
    if st.form_submit_button("Back"):
        st.switch_page("pages/page_1.py")
