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
        "reason_for_illness",

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

# B5
st.write("")
st.write("Was the job you were working in last week a full-time or part-time job?")
st.session_state.data["full/part"] = st.selectbox(
    "Tip: For employees, the normal hours of work reders to the hours of work that are fixed under legal, collective of contractual agreements. It **excludes** overtime hours (whether paid or unpaid) and meal breaks",
    full_part_time,
    index=get_index(full_part_time, st.session_state.data["full/part"])
    )

if get_index(full_part_time, st.session_state.data["full/part"]) == 1:
    # B6 
    st.session_state.data["main_reason_parttime"] = st.selectbox(
        "What was the main reason that you were working part-time rather than full-time?",
        main_reason,
        index=get_index(main_reason, st.session_state.data["main_reason_parttime"])
    )
    if get_index(main_reason, st.session_state.data["main_reason_parttime"]) == 12:
        st.session_state.data["other_reason"] = st.text_input("Please specify", value=st.session_state.data["other_reason"])

    # B7
    st.write("")
    st.write("Are you willing to work additional hours?")
    st.session_state.data["willing"] = st.selectbox(
        "Note: This refers to whether you are willing to work additional hours in general and is not restricted to your current part-time job. This could include willingness to work longer hours in current / another part-time job or taking up a full-time job.",
        yn,
        index=get_index(yn, st.session_state.data["willing"])
    )

    # B8
    st.write("")
    st.write("Are you available for additional work?")
    if st.session_state.data["willing"] == "Yes":
        st.session_state.data["available"] = st.selectbox(
            "Note: This refers to whether you are availble to work additional hours in general and is not restricted to your current part-time job. This could include availability to work longer hours in current / another part-time job or taking up a full-time job.",
            yn,
            index=get_index(yn, st.session_state.data["available"])
        )

    st.write("")
    st.write("Tip: If you were holding **more than** 1 job last week, please answer B9-B12 with reference to all jobs.")


if st.session_state.data["willing"] == "No" or get_index(full_part_time, st.session_state.data["full/part"]) == 0 or st.session_state.data["available"] != None:
    # B9
    st.write("")
    st.write("What was your gross monthly income from employment last month (excluding bonus or 13th month Annual Wage Supplement)?")
    st.session_state.data["monthly_income"] = st.number_input(
        st.markdown('''
                    Note: **Gross monthly income from employment** refers to income earned from employment in **all** jobs  
                    **For employees**, it refers to the gross monthly wages or salaries before deductions of employee CPF contributions and personal income tax. 
                    It comprises basic wages, overtime pay, commissions, tips and other allowances but **excludes** employer CPF contributions.  
                    **For self-employed persons**, gross monthly income refers to the average monthly profits from their business, trade or profession (ie. total receipts less business expenses incurred) before dudection of income tax.
                    '''),
        value=st.session_state.data["monthly_income"],
        min_value=0
    )

    # B10
    st.write("")
    st.write("How many hours a week do you typically work at your job(s), excluding meal breaks but including paid and unpaid overtime?")
    st.session_state.data["hours"] = st.number_input(
        st.markdown('''
                    **Note: This is regardless whether you are temporarily absent from work, on leave, or worked more/fewer hours than usual.**  
                    Tip: For self-employed work, please include both your regular paid and unpaid hours in a normal week of work (eg. hours spent looking for customers, doing background research prior to taking on an assignment, etc. Meal breaks should be excluded)
                    '''),
                    value=st.session_state.data["hours"],
                    min_value=0
    )

    # B11
    st.write("")
    st.write("Last week, did you work any extra hours (eg. paid or unpaid overtime) that you do not usually work?")
    st.session_state.data["extra"] = st.selectbox(
        "Tip: This includes hours of work put in over the weekends or outside of the office, eg. via teleworking or teleconference, but excluses time spent on standby.",
        yn,
        index=get_index(yn, st.session_state.data["extra"])
    )
    if st.session_state.data["extra"] == "Yes":
        st.session_state.data["extra_hours"] = st.number_input(
            "Please indicate number of extra hours:",
            value=st.session_state.data["extra_hours"],
            min_value=0
            )

    # B12   
    st.session_state.data["time_off"] = st.selectbox(
        "Did you take any time off form work or were away on leave last week (eg.annual leave, childcare leave, off-in-lieu), public holiday, illness/injury or any other reason?",
        yn,
        index=get_index(yn, st.session_state.data["time_off"])
    )
    if st.session_state.data["time_off"] == "Yes":
        st.session_state.data["time_off_no"] = st.number_input(
            "Please indicate number of hours of absence:",
            value=st.session_state.data["time_off_no"],
            min_value=0
            )

if get_index(types, st.session_state.data["types"]) in [0,1]:
    # B13
    st.write("")
    st.write("Which of the following best describes your type of employment?")
    st.session_state.data["best_describes"] = st.selectbox(
        "Tip: If you were holding more than 1 job last week, please answer with reference to the job for which you usually work the longest hours.",
        descriptions,
        index=get_index(descriptions, st.session_state.data['best_describes'])
    )
    if get_index(descriptions, st.session_state.data["best_describes"]) == 2:
        st.session_state.data["contract_length"] = st.selectbox(
            "Length of contract:",
            contract_length,
            index=get_index(contract_length, st.session_state.data["contract_length"])
        )

if st.session_state.data["willing"] == "Yes" and st.session_state.data["available"]:
    st.session_state.button_disabled = False
if st.session_state.data["time_off_no"]:
    st.session_state.button_disabled = False

if st.button(label="Submit", disabled=st.session_state.button_disabled):
    st.switch_page("pages/page_6.py")