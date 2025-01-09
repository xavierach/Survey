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
    
with st.form(key="edu_and_emp"):
    st.subheader("Education and Employment Details")
    
    acad_quali = ["O\' Level", "N\' Level", "A\' Level", "Diploma", "Bachelor\'s", "Master\'s"]
    if st.session_state.data.get("acad & quali") == None:
             st.session_state.data["acad & quali"] = st.selectbox("What is your highest academic grade pased or qualification attained", acad_quali, index=None)
    else:
        st.session_state.data["acad & quali"] = st.selectbox("What is your highest academic grade pased or qualification attained", acad_quali, index=acad_quali.index(st.session_state.data.get("acad & quali")))

    place = ["Singapore", "Outside Singapore"]
    if st.session_state.data.get("place") == None:
            st.session_state.data["place"] = st.radio("Where is the place of study for your highest qualification attained?", place, index=None)
    else:
        st.session_state.data["place"] = st.radio("Where is the place of study for your highest qualification attained?", place, index=place.index(st.session_state.data.get("place")))

    YN = ["Yes", "No"]
    if st.session_state.data.get("certificates") == None:
        st.session_state.data["certificates"] = st.radio("Have you ever obtained any vocational or skills certificates / qualifications, including Workforce Skills Qualidations (WSQ) and Employability Skills System (ESS) certificates by SkillsFuture Singapore (SSG) or the former Singapore Workforce Development Agency (WDA)", YN, index=None)
    else:
        st.session_state.data["certificates"] = st.radio("Have you ever obtained any vocational or skills certificates / qualifications, including Workforce Skills Qualidations (WSQ) and Employability Skills System (ESS) certificates by SkillsFuture Singapore (SSG) or the former Singapore Workforce Development Agency (WDA)", YN, index=YN.index(st.session_state.data.get("certificates")))
    
    if st.session_state.data.get("retirement") == None:
        st.session_state.data["retirement"] = st.radio("Have you ever retired from any job?", YN, index=None)
    else:
        st.session_state.data["retirement"] = st.radio("Have you ever retired from any job?", YN, index=YN.index(st.session_state.data.get("retirement")))
    
    status = ["Working (including empliyee or self-employed and those in full-time, part-time, permanent, fixed-term contract or casual / on-call umployment)", "Undergoing full-time National Service (NS) [i.e. Mandatory 2-year national service for Singapore males, usually aged 17 to 21]", "Schooling but currently working in vacation job", "Schooling but currently undergoing paid internship", "Working while awaiting examination results or NS call-up", "Working while schooling", "Working (excluding full-time NS) but temporarily absent from work due to COVID-19 situation", "Not working"]
    if st.session_state.data.get("curr status") == None:
            st.session_state.data["curr status"] = st.radio("What is you current labour force status", status, index=None)
    else:
        st.session_state.data["curr status"] = st.radio("What is you current labour force status", status, index=status.index(st.session_state.data.get("curr status")))

    if st.form_submit_button(label="Continue"):
        st.switch_page("pages/page_4.py")
        time.sleep(2)

    if st.form_submit_button(label="Back"):
        st.switch_page("pages/page_2.py")
