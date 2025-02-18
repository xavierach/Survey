import streamlit as st
import numpy as np
import pandas as pd
import time
from modules.nav import NavbarSurvey

if 'button_disabled' not in st.session_state:
    st.session_state.button_disabled = True

def get_index(options, value):
    if value in options:
        return options.index(value)
    else:
        return None

employment_type = [
    "Employee (ie. works for an employer in return for regular wages or salaries)",
    "Employer (ie. self-employed and engaged paid employee(s))",
    "Own Account Worker (ie. self-employed without paid employees)",
    "Contributing Family Worker (ie. helping in family business without receiving regular pay)"
    ]
full_part_time = [
    "Full-time - Refers to employment where the normal hours of work in the main job is at least 35 hours a week",
    "Part-time - Refers to employment where the normal hours of work in the main job is less than 35 hours a week"]
main_reason = [
    "Pursuing full-time / part-time studies (eg. Secondary, JC, ITE, Poly. Private Institution or University)",
    "Awaiting the start of an academic year",
    "Awaiting NS call-up",
    "Attending courses / training",
    "Personal health / medical reasons",
    "Care for own children aged 12 and below",
    "Care for own chldren aged above 12",
    "Other family responsibilities (eg. housework)",
    "Other personal commitment",
    "Could not find a full-time job",
    "Have sufficient financial support / means",
    "Retired from full-time employment",
    "Others"
    ]
yn = ["Yes", "No"]
types = [
    "Singapore Citizen", " Singapore Permanent Resident (PR)", "Foreigner on Employment Pass", 
    "Foreigner on S Pass", "Foreigner on Work Permit", "Foreigner on Student's Pass", 
    "Foreigner on Social Visit pass (eg. Long-Term Visit Pass(LTVP), Long-Term Visit Pass Plus(LTVP+))",
    "Foreigner on Dependent's Pass", "New born foreign baby or child without identification document yet", 
    "Forigner on Training Pass", "Foreigner on other types of identification"
]
descriptions = [
    "Permanent employee",
    "Casual/on-call employee",
    "Fixed-term contract employee"
]
contract_length = [
    "Less than 1 month",
    "1 month to less than 3 months",
    "3 months to less than 6 months",
    "6 months to less than 1 year",
    "1 year",
    "More than 1 year to 2 years",
    "More than 2 years"
]


st.title("Section B")
st.subheader("EMPLOYED PERSONS")

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
        "reason_for_illness", "chose_to_leave",

        "reason_not_looking", "ever_worked", "when_left", "months", "years"
    ]:
        st.session_state.data[i] = None

    



st.write("Tip: If you were holding more than 1 job last week, please answer Qns 1-6 with reference to the job for which you usually work the longest hours.")
st.write("")

# B1
st.write("What was your employment status last week?")
st.session_state.data["employment_status"] = st.selectbox(
    "Note: Self-employed persons refer to persons who operate their own business or trade. They may or may not employ paid employees. Examples include: taxi drivers, private-hire car drivers, food delivery riders, real estate agents, insurance sales agents, private babysitters/confinement ladies, private tutors, instructors, consultants, designers, persons who take on short-term, assignment-based work such as cleaners", 
    employment_type,
    index=get_index(employment_type, st.session_state.data["employment_status"]) 
)

# B2
st.write("")
st.write("What was your occupation last week?")
st.session_state.data["job_title"] = st.text_input("Job title", value=st.session_state.data["job_title"])
st.session_state.data["maintasks"] = st.text_input("Please descirbe the main tasks / duties performed in your job")

# B3
st.write("")
st.write("What was the industry you were working in last week?")
st.session_state.data["industry"] = st.text_input("(Please give the nature of business/main activity undertaken by your establishment)", value=st.session_state.data["industry"])

# B4
st.session_state.data["establishment"] = st.text_input("What was the name of the establishment you were working in last week", value=st.session_state.data["establishment"])

if st.session_state.data["establishment"]:
    st.session_state.button_disabled = False

if st.button(label="Submit", disabled=st.session_state.button_disabled):
    st.switch_page("pages/page_6.py")