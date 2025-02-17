import streamlit as st
import numpy as np
import pandas as pd
import time
import datetime
import calendar
from modules.nav import NavbarSurvey

if 'button_disabled' not in st.session_state:
    st.session_state.button_disabled = True

def get_index(options, value):
    if value in options:
        return options.index(value)
    else:
        return None

def calculate_age(dob):
    # Get the current date
    current_date = datetime.date.today()
    
    # Set the reference date to the end of the current month
    end_of_month = datetime.date(current_date.year, current_date.month, calendar.monthrange(current_date.year, current_date.month)[1])
    
    # Calculate age
    age = end_of_month.year - dob.year - ((end_of_month.month, end_of_month.day) < (dob.month, dob.day))
    
    return age

def domesticHelperValidation():
    if (st.session_state.data["r_s"] == r_s[11]):
        st.session_state.data["employment_status"] = "employed"
        # need continue

def question8validation():
    if (st.session_state.data["dob"] and st.session_state.data["age"] < 15):
        st.session_state.button_disabled = False
    elif (st.session_state.data["outside_stay"] and (st.session_state.data["outside_stay"] == outside_stay[1] or st.session_state.data["outside_stay"] == outside_stay[2])):
        st.session_state.button_disabled = False
    elif (st.session_state.data["inside_stay"] and (st.session_state.data["inside_stay"] == inside_stay[1])):
        st.session_state.button_disabled = False
    else:
        st.session_state.button_disabled = True    
    ageValidation()

def ageValidation():    
    if (st.session_state.data["dob"]):
        age = calculate_age(st.session_state.data["dob"])
        st.session_state.data["age"] = age

def highestQualificationValidation():
    # checking highest qualification if open qns A11 or others
    if get_index(acad, st.session_state.data["acad"]) in [0, 1, 2, 6, 7, 8, 9]:
        st.session_state.data["high_quali"] = True
    elif get_index(acad, st.session_state.data["acad"]) in [3, 4, 5]:
        st.session_state.data["high_quali"] = False

def highestQualificationLocalValidation():
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

def highestVocationalQualLocalValidation():
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

def labourForceValidation():
    if get_index(labour_force_status, st.session_state.data["labour_force_status"]) == 5:
        st.session_state.button_disabled = False
    elif get_index(labour_force_status, st.session_state.data["labour_force_status"]) in [0, 1, 2, 3, 4]:
        st.session_state.data["not_working"] = True
    if st.session_state.data["labour_force_status"]:
        st.session_state.button_disabled = False


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
    "Foreigner on Social Visit pass (eg. Long-Term Visit Pass(LTVP), Long-Term Visit Pass Plus(LTVP+)",
    "Foreigner on Dependent's Pass", "New born foreign baby or child without identification document yet", 
    "Forigner on Training Pass", "Foreigner on other types of identification"
]
inside_stay = ["Residential Unit", "Institutional Unit (e.g., old age home, prison, reformatory centre)"]
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
labour_force_status = [
"Working (including employee or self-employed and those in full-time, part-time, permanent, fied-term contract or casual/on-call employment)",
"Undergoing full-time National Service (NS)",
"Schooling but currently undergoing paid internship/traineeship/apprenticeship",
"Working while awaiting examination results or NS call-up",
"Working while schooling",
"Not working"
]
sg_stay = ["Singapore", "Outside Singapore"]
yn = ["Yes", "No"]
expectation_to_start = [
    "2 weeks or less from now",
    "More than 2 weeks and up to 1 month from now",
    "More than 1 month and up to 3 months from now",
    "More than 3 months from now"]
when_available = [
    "More than 2 weeks to 1 month from now",
    "More than 1 month to 3 months from now",
    "More than 3 months from now"
]

st.title("Section A")

# intialising session_state data
if "data" not in st.session_state:
    st.session_state.data = {}
    for i in [
        "name", "nric", "contact_no","dob","age", "r/s", "sex", "race", "types", "sg_stay", "inside_stay","outside_stay", "marital_status", 
        "acad", "part_2", "high_quali", "high", "high_sg", "sg_high_part", "voc/skill", "outside_sg_part", "high_skill", 
        "skill_quali", "skill_loc", "sg_high_part2","outside_sg_part2", "voc/skill_part", "high_sg2", "retired", "retirement_age", "labour_force_status",
        "not_working", "looking", "present", "expect", "secured", "12months", "available_in_2_weeks", "when_available",

        "employment_status", "job_title", "maintasks", "industry", "establishment", "full/part", "main_reason_parttime", "other_reason",
        "willing", "available", "monthly_income", "hours", "extra", "extra_hours", "time_off", "time_off_no", "best_describes", "contract_length",

        "length_of_looking", "while_looking", "worked_before", "last_occ", "last_main_tasks", "industry_last", "last_establishment",
        "last_employment_status", "last_full/part", "last_monthly_income", "reason_for_leaving", "reason_for_contract", "reason_for_temporary",
        "reason_for_illness",

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
    max_value="today",
    on_change=question8validation(),
)

ageValidation()
    

# qns A5
st.session_state.data["sex"] = st.selectbox(
    "Sex", 
    sex, 
    index=get_index(sex, st.session_state.data.get("sex"))
    )

# qns A6
st.markdown("""
    Race  
    Note: For those with double-barelled race, please indicate the **first-component** race, eg. for an Indian Chinese, please indicate as Indian
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
    "Where are you currently staying?", 
    sg_stay, 
    index = get_index(sg_stay, st.session_state.data.get("sg_stay"))
)

if (st.session_state.data["sg_stay"]==sg_stay[1]):    
    st.session_state.data["outside_stay"] = st.radio(
        "Outside Singapore", 
        outside_stay,
        on_change=question8validation(),
        index = get_index(outside_stay, st.session_state.data.get("outside_stay"))
    )

    if (st.session_state.data["outside_stay"] == outside_stay[1] or st.session_state.data["outside_stay"] == outside_stay[2]):
        st.session_state.button_disabled = False
    else:
        st.session_state.button_disabled = True

elif (st.session_state.data["sg_stay"]==sg_stay[0]):
    st.session_state.data["inside_stay"] = st.radio(
        "Staying in", 
        inside_stay,
        on_change=question8validation(),
        index = get_index(inside_stay, st.session_state.data.get("inside_stay"))
    )
else:
    st.write("")

# opening additional questions from answers above
# qns A9
if (st.session_state.button_disabled == True
    and (st.session_state.data["outside_stay"]
    or st.session_state.data["inside_stay"])):
    st.session_state.data["marital_status"] = st.selectbox(
        "Martial Status", 
        martial_status, 
        index=get_index(martial_status, st.session_state.data.get("marital_status"))
        )

    ### Look at Foreign Domestic Helpers part in page 3

    # qns A10
    st.write("")
    st.markdown('''
        What is your highest academic grade passed or qualification attained?
    ''')
    st.session_state.data["acad"] = st.selectbox(
        "[Excluding Workforce Skills Qualifications (WSQ) and Employability Skills System (ESS) certificates]", 
        acad, 
        on_change=highestQualificationValidation(),
        index=get_index(acad, st.session_state.data["acad"])
    )
    highestQualificationValidation()

# open qns A11 if highest qualification is correct
if st.session_state.data["high_quali"] == True:
    # A11
    st.markdown('''
        **Note:** Persons who obtained their highes qualification in **Singapore** were awarded by an education institution based in Singapore
        or by an overseas institution through a partner institution based in Singapore (eg. person attained an overseas degree
        through a private school based in Singapore).  
        
        Persons who obtained their highest qualification **outside Singapore** must have studies overseas in an education institution based abroad.
    ''')

    st.session_state.data["high"] = st.selectbox(
        "Where did you obtain your highest qualification?",
        sg_stay,
        on_change=highestQualificationLocalValidation(),
        index = get_index(sg_stay, st.session_state.data["high"])
    )
    highestQualificationLocalValidation()

# if highest quali in sg, open qns A12 to A13
if st.session_state.data["sg_high_part"] == True:
    # qns A12
    st.session_state.data["high_sg"] = st.selectbox(
        "Which institution awarded your highest qualification attained",
        sg_high_quali,
        index = get_index(sg_high_quali, st.session_state.data["high_sg"])
    )

# if highest quali outside sg
if st.session_state.data["outside_sg_part"] == True or st.session_state.data["high_sg"]:
    # qns A13
    st.session_state.data["voc/skill"] = st.radio(
        "Have you ever obtained any Vocational or Skills certificates/qualifications, (eg. Workforce Skills Qualifications (WSQ) and Employability Skills System (ESS) certificates)?",
        yn,
        index = get_index(yn, st.session_state.data["voc/skill"])
    )

# checking if A13 is "yes"
if st.session_state.data["voc/skill"] == "Yes":
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
        on_change=highestVocationalQualLocalValidation(),
        index = get_index(sg_stay, st.session_state.data["skill_loc"])
    )
    highestVocationalQualLocalValidation()

if st.session_state.data["sg_high_part2"] == True:
    # A16
    st.session_state.data["high_sg2"] = st.selectbox(
        "Which institution awarded your highest vocational or skills certicate / qualification attained?",
        sg_high_quali,
        index = get_index(sg_high_quali, st.session_state.data["high_sg2"])
    )

# A17
if ((st.session_state.data["age"] is not None 
    and st.session_state.data["age"] > 40)
    and st.session_state.data["sg_high_part2"] 
    or st.session_state.data["outside_sg_part2"] == True 
    or st.session_state.data["high_quali"] == False
    or st.session_state.data["voc/skill"] == "No"
    and get_index(types, st.session_state.data["types"]) in [0,1]):
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
st.session_state.data["labour_force_status"] = st.selectbox(
    "What is your current labour force status?",
    labour_force_status,
    on_change=labourForceValidation(),
    index = get_index(labour_force_status, st.session_state.data["labour_force_status"])
)
labourForceValidation()

# A19 if not working
if st.session_state.data["labour_force_status"] == "Not working":
    st.write()
    st.write("Were you actively looking for jobs in the past 4 weeks?")
    st.session_state.data["looking"] = st.selectbox(
        "Note: If you have taken steps to start your own business in the past 4 weeks (eg. arranging for financial resources, applying for permits, licenses, looking for premises), please answer \"Yes\" as well",
        yn,
        index=get_index(yn, st.session_state.data["looking"])
    )

if st.session_state.data["looking"] == "No":
    # A20
    st.session_state.data["12months"] = st.selectbox(
        "If no, what about at any point in time from 12 months ago till now?",
        yn,
        index=get_index(yn, st.session_state.data["12months"])
    )

    # A21
    st.session_state.data["present"] = st.selectbox(
        "At present, do you want to work?",
        yn, 
        index=get_index(yn, st.session_state.data["present"])
    )

if st.session_state.data["12months"] == "Yes":
    # A22
    st.session_state.data["secured"] = st.selectbox(
        "Have you already secured a job?",
        yn, 
        index=get_index(yn, st.session_state.data["secured"])
    )

if st.session_state.data["secured"] == "Yes":
    # A23
    st.session_state.data["expect"] = st.selectbox(
        "How soon do you expect to start working in this new job?",
        expectation_to_start,
        index=get_index(expectation_to_start, st.session_state.data["expect"])
    )

# A24
if (st.session_state.data["looking"] == "Yes"
    or st.session_state.data["present"] == "No"
    or st.session_state.data["secured"] == "No"
    or st.session_state.data["expect"]):
    if get_index(expectation_to_start, st.session_state.data["expect"]) == 0:
        st.session_state.data["availble_in_2_weeks"] = "Yes"
    st.session_state.data["availble_in_2_weeks"] = st.selectbox(
        "Are you available to work in the next 2 weeks?",
        yn,
        index=get_index(yn, st.session_state.data["available_in_2_weeks"])
    )

# A25
if st.session_state.data["looking"] == "Yes" and st.session_state.data["available_in_2_weeks"] == "No":
    st.session_state.data["when_available"] = st.selectbox(
        "When will you be available to work?",
        when_available,
        index=get_index(when_available, st.session_state.data["when_available"])
    )



#Submit button
if st.button(label="Submit", disabled=st.session_state.button_disabled):
    if (st.session_state.data["dob"] and st.session_state.data["age"] < 15):
        st.switch_page("pages/page_6.py")
    elif (st.session_state.data["outside_stay"] and (st.session_state.data["outside_stay"] == outside_stay[1] or st.session_state.data["outside_stay"] == outside_stay[2])):
        st.switch_page("pages/page_6.py")
    elif (st.session_state.data["inside_stay"] and (st.session_state.data["inside_stay"] == inside_stay[1])):
        st.switch_page("pages/page_6.py")

    if ((st.session_state.data["looking"] == "Yes" and st.session_state.data["available_in_2_weeks"] == "Yes")
        or (st.session_state.data["looking"] == "No" and st.session_state.data["available_in_2_weeks"] == "Yes" and get_index(st.session_state.data["expect"]) in [0, 1, 2])):
        st.switch_page("pages/page_4.py")
    elif (st.session_state.data["available_in_2_weeks"] == "No" 
          or (st.session_state.data["looking"] == "Yes" and st.session_state.data["available_in_2_weeks"] == "Yes"
              and (st.session_state.data["present"] == "No" or st.session_state.data["secured"] == "No" or get_index(st.session_state.data["expect"]) == 3))):
        st.switch_page("pages/page_5.py")
    elif get_index(labour_force_status, st.session_state.data["labour_force_status"]) not in [2, 5]:
        st.switch_page("pages/page_3.py")
    elif get_index(labour_force_status, st.session_state.data["labour_force_status"]) == 1:
        st.switch_page("pages/page_7.py")
    else:
        st.switch_page("pages/page_6.py")