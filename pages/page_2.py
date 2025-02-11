import streamlit as st
import numpy as np
import pandas as pd
import time
import datetime
from modules.nav import NavbarSurvey

def get_index(options, value):
    if value in options:
        return options.index(value)
    else:
        return None

NavbarSurvey()

# answer options for questions
r_s = [
    "Household Reference Person", "Husband/Wife", "Son/Daughter", "Son-in-law/Daughter-in-law",
    "Parent", "Parent-in_law", "Sibling/Sibling-in-law", "Grandchild/Grandchild-in-law", 
    "Grandparent/Grandparent-in-law", "Other Relative (eg. great-grandparent, great-grandchild)",
    "Partner", "Domestic Helper", "Unrelated Person (eg. tenant, friend, confinement lady, chauffeur)"
]
sex = ["Male", "Female"]
race =["Chinese", "Malay", "Indian", "Eurasian", "Others"]
types = [
    "Singapore Citizen", " Singapore Permanent Resident (PR)", "Foreigner on Employment Pass", 
    "Foreigner on S Pass", "Foreigner on Work Permit", "Foreigner on Student's Pass", 
    "Foreigner on Social Visit pass (eg. Long-Term Visit Pass(LTVP), Long-Term Visit Pass Plus(LTVP+))",
    "Foreigner on Dependent's Pass", "New born foreign baby or child without identification document yet", 
    "Forigner on Training Pass", "Foreigner on other types of identification"
]
outside_stay = ["≤ 6 Months", "> 6 to < 12 Months", "≥ 12 Months"]
martial_status = ["Single", "Married", "Widowed", "Divorced", "Separated"]
acad = ["NITEC", "Higher NITEC", "Master NITEC", "O\' level", "N\' level", "A\' level", "Diploma", "Bachelor\'s", "Master\'s", "Other professional qualifications"]
sg_high_quali = [
    "National University of Singapore (including the former University of Singapore)",
    "Nanyang Technological University (including the former Nanyang University and Nanyang Technological Institute)",
    "National Institute of Education (including the National Institue of Early Childhood Development under its ambit)",
    "Singapore Management University",
    "Singapore University of Technology and Design",
    "Singapore Institute of Technology (including qualifications awarded by its overseas partner universities/institutions)",
    "Singapore University of Social Sciences (SUSS) [formerly known as SIM University (UniSIM)]",
    "Local Polytechnics (ie. Ngee Ann Polytechnic, Nanyang Polytechnic, Republic Polytechnic, Singapore Polytechnic, Temasek Polytechnic)",
    "Institute of Technical Education",
    "Public Sector Training Institutions (eg. BCA Academy, Singapore Aviation Academy), including those awarded by their overseas partner universities/institutions",
    "Nanyang Academy of Fine Arts (including qualifications awarded by its overseas partner universities/institutions)",
    "LASALLE College of the Arts (including qualifications awarded by its overseas partner universities/institutions)",
    "Other private education institutions in Singapore [eg. SIM Global Education (SIM GE), Kaplan Higher Education Institution/Academy, PSB Academy, Management Development Institute of Singapore (MDIS)], including those awarded by their overseas partner universities/institutions"
]
sg_stay = ["Singapore", "Outside Singapore"]
yn = ["Yes", "No"]

st.title("Section A")

# intialising session_state data
if "data" not in st.session_state:
    st.session_state.data = {}
    for i in [
        "name", "nric", "contact_no", "r/s", "sex", "race", "type", "sg_stay", "outside_stay", "marital_status", "acad", "part_2", "high_quali", "high", "high_sg", "sg_high_part", "voc/skill", "outside_sg_part", "high_skill"

    ]:
        st.session_state.data[i] = None

with st.form(key="For all persons"):
    st.subheader("FOR ALL PERSONS")

    # qns A1
    st.session_state.data["nric"] = st.text_input("S/No.", value=st.session_state.data.get("nric"))
    # qns A2
    st.session_state.data["name"] = st.text_input("Name", value=st.session_state.data.get("name"))
    
    # qns A3
    st.markdown("""
        Relationship to Household Reference Person  
        Note: Then household reference person may refer to the oldest member, the main income earner, the owner-occupier of the house or the person who manages the affairs of the household.
    """)
    st.session_state.data["r/s"] = st.selectbox(
        "Select relationship:",
        r_s,
        index=get_index(r_s, st.session_state.data.get("r/s"))
    )

    # qns A4
    st.write(" ")
    st.session_state.data["dob"] = st.date_input(
        "Date of birth", 
        value=st.session_state.data.get("dob"),
        min_value=datetime.date(1900, 1, 1), 
        max_value="today"
    )

    # qns A5
    st.session_state.data["sex"] = st.selectbox(
        "Sex", 
        sex, 
        index=get_index(sex, st.session_state.data.get("sex"))
        )

    # qns A6
    st.markdown("""
        Race  
        Note: For those with double-barelled race, please indicate the first-component race, eg. for an Indian Chinese, please indicate as Indian
    """)
    st.session_state.data["race"] = st.selectbox(
        "Select race", 
        race, 
        index=get_index(race, st.session_state.data.get("race"))
    )

    # qns A7
    st.session_state.data["types"] = st.selectbox(
        "Identification Type", 
        types, 
        index=get_index(types, st.session_state.data.get("type"))
    )

    # qns A8
    st.session_state.data["sg_stay"] = st.radio(
        "Singapore, staying in", 
        sg_stay, 
        index = get_index(sg_stay, st.session_state.data.get("sg_stay"))
    )
    st.session_state.data["outside_stay"] = st.radio(
        "Outside Singapore", 
        outside_stay,
        index = get_index(outside_stay, st.session_state.data.get("outside_stay"))
    )

    # switching pages based on answers
    if st.form_submit_button(label="Continue"):
        if (st.session_state.data["sg_stay"]==sg_stay[1] or st.session_state.data["outside_stay"]==outside_stay[1] or st.session_state.data["outside_stay"]==outside_stay[2]):
            st.switch_page("pages/page_6.py")
        else:
            part_2 = True
            st.session_state.data["part_2"] = True

    # to previous page
    if st.form_submit_button("Back"):
        st.switch_page("pages/page_1.py")

# opening additional questions from answers above
if st.session_state.data["part_2"] == True:
    with st.form(key="part 2"):
        # qns A9
        st.session_state.data["marital_status"] = st.selectbox(
            "Martial Status", 
            martial_status, 
            index=get_index(martial_status, st.session_state.data.get("marital_status"))
            )
        
        ### Look at Foreign Domestic Helpers part in page 3

        # qns A10
        st.write("")
        st.markdown('''
            What is you highes academic grade passed or qualification attained?
        ''')
        st.session_state.data["acad"] = st.selectbox(
            "[Excluding Workforce Skills Qualifications (WSQ) and Employability Skills System (ESS) certificates]", 
            acad, 
            index=get_index(acad, st.session_state.data["acad"])
        )

        # setting answer to see if 
        if st.form_submit_button(label="Continue"):
            # checking highest qualification if open qns A11 or others
            if get_index(acad, st.session_state.data["acad"]) in [0, 1, 2, 6, 7, 8, 9]:
                st.session_state.data["high_quali"] = True

        if st.form_submit_button("Back"):
            st.switch_page("pages/page_1.py")

# open qns A11 if highest qualification is correct
if st.session_state.data["high_quali"] == True:
    with st.form(key="part_3"):
        # A11
        st.markdown('''
            **Note:** Persons who obtained their highes qualification in **Singapore** were awarded by an education institution based in Singapore
            or by an overseas institution through a partner institution based in Singapore (eg. person attained an overseas degree
            through a private school based in Singapore).  
            
            Persons who obtained their highes qualification **outside Singapore** must have studies overseas in an education institution based abroad.
        ''')
        st.session_state.data["high"] = st.selectbox(
            "Where did you obtain your highest qualification?",
            sg_stay,
            index = get_index(sg_stay, st.session_state.data["high"])
        )

        if st.form_submit_button(label="Continue"):
            # checking if highest quali is in sg
            if st.session_state.data["high"] == "Singapore":
                st.session_state.data["sg_high_part"] = True
            else:
                st.session_state.data["outside_sg_part"] = True

# if highest quali in sg, open qns A12 to A13
if st.session_state.data["sg_high_part"] == True:
    with st.form(key="sg_high_part"):
        # qns A12
        st.session_state.data["high_sg"] = st.selectbox(
            "Which institution awarded your highest qualification attained",
            sg_high_quali,
            index = get_index(sg_high_quali, st.session_state.data["high_sg"])
        )

        # qns A13
        st.session_state.data["voc/skill"] = st.radio(
            "Have you ever obtained any Vocational or Skills certificates/qualifications, (eg. Workforce Skills Qualifications (WSQ) and Employability Skills System (ESS) certificates)?",
            yn,
            index = get_index(yn, st.session_state.data["voc/skill"])
        )
        if st.form_submit_button(label="Continue"):
            if st.session_state.data["voc/skill"] == "yes":
                st.session_state.data["high_skill"] = True

# if highest quali outside sg
if st.session_state.data["outside_sg_part"] == True:
    with st.form(key="outside_sg_part"):
        # qns A13
        st.session_state.data["voc/skill"] = st.radio(
            "Have you ever obtained any Vocational or Skills certificates/qualifications, (eg. Workforce Skills Qualifications (WSQ) and Employability Skills System (ESS) certificates)?",
            yn,
            index = get_index(yn, st.session_state.data["voc/skill"])
        )
        if st.form_submit_button(label="Continue"):
            if st.session_state.data["voc/skill"] == "yes":
                st.session_state.data["high_skill"] = True

if st.session_state.data["high_skill"] == True:
    with st.form(key="high_skill"):
        st.session_state.data["high_skill"] = st.selectbox(
            "What is the highest vocational or skills ceritficate/qualification you have attained?",
            sg_high_quali,
            index = get_index(sg_high_quali, st.session_state.data["high_skill"])
        )
        if st.form_submit_button(label="Continue"):
            pass