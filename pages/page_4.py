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
    
looking_in = [
    "Enrolled in school (eg. Secondary, JC, ITE, Poly, Private Institution or University) on a full-time or part-time basis, including awaiting the start of an academic year and students on term breaks",
    "Enrolled in a formal training programmes (eg. vocational training) on a full-time or part-time basis",
    "Awaiting NS call-up",
    "None of the above"
]
yn = ["Yes", "No"]
employment_type = [
    "Employee (ie. works for an employer in return for regular wages or salaries)",
    "Employer (ie. self-employed and engaged paid employee(s))",
    "Own Account Worker (ie. self-employed without paid employees)",
    "Contributing Family Worker (ie. helping in family business without receiving regular pay)"
    ]
full_part_time = [
    "Full-time - Refers to employment where the normal hours of work in the main job is at least 35 hours a week",
    "Part-time - Refers to employment where the normal hours of work in the main job is less than 35 hours a week"]
reasons = [
    "Retrenchment",
    "Temporary layoff without pay",
    "Cessation of business",
    "Dismisall",
    "Completion of contract / job",
    "Job was temporary in nature",
    "Pay was too low",
    "Poor working conditions",
    "Long working hours / work was too demanding",
    "Poor career prospects",
    "Felt my skills and qualitfications were not fully utilised in prevous job",
    "Issues with colleagues / boss",
    "No interest in the job",
    "Wanted to start my own business",
    "Illness / injury / accident", 
    "Retirement",
    "Housework",
    "Care for own children aged 12 and below",
    "Care for own children aged above 12",
    "Care for family (including grandchildren) / relatives",
    "On course / further study",
    "Others"
]
reasons_for_contract = [
    "The contract / job was not renewed",
    "I chose to leave the job upon completion of the contract / job"
]
reasons_for_temporary = [
    "I chose to leave the job as I took up temporarily:",
    "I lost the job because my employer has no more temporary assignments for me"
]
reasons_for_illness = [
    "I left the job on my own accord",
    "My employer terminated my service"
]
when_leave = [
    "Less than 1 month ago",
    "1 month to less than 1 year ago",
    "1 or more years ago"
]
chose_to_leave = [
    "While in search of another job",
    "During my school vacation",
    "While awaiting examination results or NS-call up",
    "To gain work experience",
    "Others"
]


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


st.title("Section C")
st.subheader("UNEMPLOYED PERSONS")

# C1
st.session_state.data["length_of_looking"] = st.number_input(
    "How long have you been looking for a job or work? (in weeks)",
    min_value=0,
    value=st.session_state.data["length_of_looking"]
)

# C2
st.session_state.data["while_looking"] = st.selectbox(
    "While currently looking for work, are you",
    looking_in,
    index=get_index(looking_in, st.session_state.data["while_looking"])
)

# C3
st.session_state.data["worked_before"] = st.selectbox(
    "Have you ever worked before (excluding full-time National Service)",
    yn,
    index=get_index(yn, st.session_state.data["worked_before"])
)

# need to redirect NO ans from C3 to form completion page
if st.session_state.data["worked_before"] == "No":
    st.session_state.button_disabled = False

if st.session_state.data["worked_before"] == "Yes":
    # C4
    st.session_state.data["last_occ"] = st.text_input(
        "Job title",
        value=st.session_state.data["last_occ"]
    )
    st.session_state.data["last_main_tasks"] = st.text_input(
        "Please describe the main tasks / duties performed in your last job",
        value=st.session_state.data["last_main_tasks"]
    )


    # C5
    st.write()
    st.write("Which industry did you work in your last job?")
    st.session_state.data["industry_last"] = st.text_input(
        "Please give the nature of business / main activity undertaken by the establishment you last worked in",
        value=st.session_state.data["industry_last"]
    )

    # C6
    st.session_state.data["last_establishment"] = st.text_input(
        "What was the name of the establishment you were working in last week", 
        value=st.session_state.data["last_establishment"]
    )

    # C7
    st.write()
    st.write("What was your employment status last week?")
    st.session_state.data["last_employment_status"] = st.selectbox(
        "Note: Self-employed persons refer to persons who operate their own business or trade. They may or may not employ paid employees. Examples include: taxi drivers, private-hire car drivers, food delivery riders, real estate agents, insurance sales agents, private babysitters/confinement ladies, private tutors, instructors, consultants, designers, persons who take on short-term, assignment-based work such as cleaners", 
        employment_type,
        index=get_index(employment_type, st.session_state.data["last_employment_status"]) 
    )

    # C8
    st.write("")
    st.write("Were you working full-time or part-time **in your last job**?")
    st.session_state.data["last_full/part"] = st.selectbox(
        "Tip: For employees, the normal hours of work reders to the hours of work that are fixed under legal, collective of contractual agreements. It **excludes** overtime hours (whether paid or unpaid) and meal breaks",
        full_part_time,
        index=get_index(full_part_time, st.session_state.data["last_full/part"])
        )
    
    # C9
    st.write("")
    st.markdown('''
                    Note: **Gross monthly income from employment** refers to income earned from employment in **all** jobs  
                    **For employees**, it refers to the gross monthly wages or salaries before deductions of employee CPF contributions and personal income tax. 
                    It comprises basic wages, overtime pay, commissions, tips and other allowances but **excludes** employer CPF contributions.  
                    **For self-employed persons**, gross monthly income refers to the average monthly profits from their business, trade or profession (ie. total receipts less business expenses incurred) before dudection of income tax.
                    ''')
    st.session_state.data["last_monthly_income"] = st.number_input(
        "What was your gross monthly income from employment last month (excluding bonus or 13th month Annual Wage Supplement)?",
        min_value=0,
        value=st.session_state.data["last_monthly_income"]
    )

    # C10
    st.session_state.data["reason_for_leaving"] = st.selectbox(
        "What was the **main** reason you left your last job? **(Please indicate only 1 option)**",
        reasons,
        index=get_index(reasons, st.session_state.data["reason_for_leaving"])
    )

# until C10 need to add logic for the options in C10 and redirect appropriately
if get_index(reasons, st.session_state.data["reason_for_leaving"]) == 4:
    # C11
    st.session_state.data["reason_for_contract"] = st.selectbox(
        "Please elaborate on the main reason for leaving your last job:",
        reasons_for_contract,
        index=get_index(reasons_for_contract, st.session_state.data["reason_for_contract"])
    )

elif get_index(reasons, st.session_state.data["reason_for_leaving"]) == 5:
    # C12
    st.session_state.data["reason_for_temporary"] = st.selectbox(
        "Please elaborate on the main reason for leaving your last job:",
        reasons_for_temporary,
        index=get_index(reasons_for_temporary, st.session_state.data["reason_for_temporary"])
    )
    if get_index(reasons_for_temporary, st.session_state.data["reason_for_temporary"]) == 0:
        st.session_state.data["chose_to_leave"] = st.selectbox(
            "Why?",
            chose_to_leave,
            index=get_index(chose_to_leave, st.session_state.data["chose_to_leave"])
        )

elif get_index(reasons, st.session_state.data["reason_for_leaving"]) == 14:
    # C13
    st.session_state.data["reason_for_illness"] = st.selectbox(
        "Please elaborate on the main reason for leaving your last job:",
        reasons_for_illness,
        index=get_index(reasons_for_illness, st.session_state.data["reason_for_illness"])
    )

if get_index(reasons, st.session_state.data["reason_for_leaving"]) not in [4, 5, 14] or st.session_state.data["reason_for_contract"] or st.session_state.data["reason_for_temporary"]:
    # C14
    st.session_state.data["when_left"] = st.selectbox(
        "When did you leave your last job?",
        when_leave,
        index=get_index(when_leave, st.session_state.data["when_left"])
    )
    if get_index(when_leave, st.session_state.data["when_left"]) == 1:
        st.session_state.data["months"] = st.number_input(
            "Please indicate number of months:",
            value=st.session_state.data["months"]
        )
    elif get_index(when_leave, st.session_state.data["when_left"]) == 2:
        st.session_state.data["years"] = st.number_input(
            "Please indicate number of years:",
            value=st.session_state.data["years"]
        )

if st.session_state.data["when_left"]:
    st.session_state.button_disabled = False


if st.button(label="Submit", disabled=st.session_state.button_disabled):
    st.switch_page("pages/page_6.py")