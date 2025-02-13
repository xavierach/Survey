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

# NavbarSurvey()

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
        "name", "nric", "contact_no", "r/s", "sex", "race", "types", "sg_stay", "outside_stay", "marital_status", 
        "acad", "part_2", "high_quali", "high", "high_sg", "sg_high_part", "voc/skill", "outside_sg_part", "high_skill", 
        "skill_quali", "skill_loc", "sg_high_part2","outside_sg_part2", "voc/skill_part", "high_sg2", "retired", "retirement_age",

        "employment_status", "job_title", "maintasks", "industry", "establishment", "full/part", "main_reason_parttime", "other_reason",
        "willing", "available", "monthly_income", "hours", "extra", "extra_hours", "time_off", "time_off_no", "best_describes", "contract_length",

        "length_of_looking", "while_looking", "worked_before", "last_occ", "last_main_tasks", "industry_last", "last_establishment",
        "last_employment_status", "last_full/part", "last_monthly_income", "reason_for_leaving",

        "reason_not_looking", "ever_worked", "when_left", "months", "years"
    ]:
        st.session_state.data[i] = None


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
    index=get_index(types, st.session_state.data.get("types"))
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

if (st.session_state.data["sg_stay"]==sg_stay[1] or st.session_state.data["outside_stay"]==outside_stay[1] or st.session_state.data["outside_stay"]==outside_stay[2]):
    st.switch_page("pages/page_6.py")
elif (st.session_state.data["sg_stay"]==sg_stay[0] or st.session_state.data["outside_stay"]==outside_stay[0]):
    st.session_state.data["part_2"] = True
else:
    st.session_state.data["part_2"] = False


# opening additional questions from answers above
if st.session_state.data["part_2"] == True:
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


    # checking highest qualification if open qns A11 or others
    if get_index(acad, st.session_state.data["acad"]) in [0, 1, 2, 6, 7, 8, 9]:
        st.session_state.data["high_quali"] = True
    else:
        st.session_state.data["high_quali"] = False


# open qns A11 if highest qualification is correct
if st.session_state.data["high_quali"] == True:
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

    # checking if highest quali is in sg
    if st.session_state.data["high"] == "Singapore":
        st.session_state.data["sg_high_part"] = True
        st.session_state.data["outside_sg_part"] = False
    elif st.session_state.data["high"] == "Outside Singapore":
        st.session_state.data["outside_sg_part"] = True
        st.session_state.data["sg_high_part"] = False
    else:
        st.session_state.data["sg_high_part"] = False
        st.session_state.data["outside_sg_part"] = False

# if highest quali in sg, open qns A12 to A13
if st.session_state.data["sg_high_part"] == True:
    # qns A12
    st.session_state.data["high_sg"] = st.selectbox(
        "Which institution awarded your highest qualification attained",
        sg_high_quali,
        index = get_index(sg_high_quali, st.session_state.data["high_sg"])
    )

# if highest quali outside sg
if st.session_state.data["outside_sg_part"] == True or st.session_state.data["sg_high_part"] == True:
    # qns A13
    st.session_state.data["voc/skill"] = st.radio(
        "Have you ever obtained any Vocational or Skills certificates/qualifications, (eg. Workforce Skills Qualifications (WSQ) and Employability Skills System (ESS) certificates)?",
        yn,
        index = get_index(yn, st.session_state.data["voc/skill"])
    )

    if st.session_state.data["voc/skill"] == "Yes":
        st.session_state.data["voc/skill_part"] = True

# checking if A13 is "yes"
if st.session_state.data["voc/skill_part"] == True:
    # A14
    st.session_state.data["high_skill"] = st.text_input(
        "What is the highest vocational or skills ceritficate/qualification you have attained?",
        value = st.session_state.data["high_skill"]
    )

# A15
if st.session_state.data["high_skill"] != None:
    st.session_state.data["skill_loc"] = st.selectbox(
        "Where did you obtain your highest vocational or skills certificate / qualification?",
        sg_stay,
        index = get_index(sg_stay, st.session_state.data["skill_loc"])
    )

    # checking if skill highest quali is in sg
    if st.session_state.data["skill_loc"] == "Singapore":
        st.session_state.data["sg_high_part2"] = True
        st.session_state.data["outside_sg_part2"] = False
    elif st.session_state.data["skill_loc"] == "Outside Singapore":
        st.session_state.data["outside_sg_part2"] = True
        st.session_state.data["sg_high_part2"] = False
    else:
        st.session_state.data["sg_high_part2"] = False
        st.session_state.data["outside_sg_part2"] = False

if st.session_state.data["sg_high_part2"] == True:
    # A16
    st.session_state.data["high_sg2"] = st.selectbox(
        "Which institution awarded your highest vocational or skills certicate / qualification attained?",
        sg_high_quali,
        index = get_index(sg_high_quali, st.session_state.data["high_sg2"])
    )

# A17
if (st.session_state.data["sg_high_part2"] == True or st.session_state.data["outside_sg_part2"] == True) and get_index(types, st.session_state.data["types"]) in [0,1]:
    st.session_state.data["retired"] = st.selectbox(
        "Have you ever retired from any job?",
        yn,
        index = get_index(yn, st.session_state.data["retired"])
    )
    if st.session_state.data["retired"] == "Yes":
        st.session_state.data["retirement_age"] = st.number_input(
            "At what age did you retire?",
            step=1,
            min_value=0,
            max_value=150,
            value=st.session_state.data["retirement_age"]
        )

# A18
