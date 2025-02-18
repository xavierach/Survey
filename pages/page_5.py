import streamlit as st
import numpy as np
import pandas as pd
import time
from modules.nav import NavbarSurvey
import json
import os
import boto3

if 'button_disabled' not in st.session_state:
    st.session_state.button_disabled = True

# Define the name of the S3 bucket and the file you want to upload
bucket_name = 'survey-output'

# Create a Boto3 S3 client
s3 = boto3.client('s3')


def get_index(options, value):
    if value in options:
        return options.index(value)
    else:
        return None

st.title("Section D")
st.subheader("Persons Outside The Labour Force")

reason_for_no_job = [
    "Pursuing full-time / part-time studies (eg. Secondary, JC, ITE, Poly. Private Institution or University)",
    "Pursuing part-time study",
    "Awaiting the start of an academic year",
    "Awaiting NS call-up",
    "Awaiting examination results",
    "Attending courses / training",
    "Housework",
    "Care for own children aged 12 and below",
    "Care for own chldren aged above 12",
    "Care for families (including grandchildren) / relative",
    "Care for persons who are not family / relatives",
    "Doing vouluntary / community work",
    "Poor health",
    "Permanently ill / disabled",
    "Retired / No desire to work due to old age",
    "Have sufficient financial support / means",
    "Gave up active job search as I believe there is no suitable work available",
    "Employers' discrimination (eg. prefer younger workers)",
    "Lack necessary qualification, training, skills or experience",
    "Taking a break",
    "Foreigner without work pass",
    "Others"
]
yn = ["Yes", "No"]
when_leave = [
    "Less than 1 month ago",
    "1 month to less than 1 year ago",
    "1 or more years ago"
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


st.session_state.data["reason_not_looking"] = st.selectbox(
    "What is your main reason for not working and not looking for a job?",
    reason_for_no_job,
    index=get_index(reason_for_no_job, st.session_state.data["reason_not_looking"])
)

st.session_state.data["ever_worked"] = st.selectbox(
    "Have you ever worked before (excluding full-time National Service)?",
    yn, 
    index=get_index(yn, st.session_state.data["ever_worked"])
)

if st.session_state.data["ever_worked"] == "Yes":
    st.session_state.data["when_left"] = st.selectbox(
        "When did you leave your last job?",
        when_leave,
        index=get_index(when_leave, st.session_state.data["when_left"])
    )
    if get_index(when_leave, st.session_state.data["ever_worked"]) == 1:
        st.session_state.data["months"] = st.number_input(
            "Please indicate number of months:",
            value=st.session_state.data["months"]
        )
    elif get_index(when_leave, st.session_state.data["ever_worked"]) == 2:
        st.session_state.data["years"] = st.number_input(
            "Please indicate number of years:",
            value=st.session_state.data["years"]
        )

if st.session_state.data["reason_not_looking"] and st.session_state.data["ever_worked"] == "Yes" and st.session_state.data["when_left"]:
    st.session_state.button_disabled = False
if st.session_state.data["ever_worked"] == "No":
    st.session_state.button_disabled = False

if st.button(label="Submit", disabled=st.session_state.button_disabled):
    file_name = "data.json"
    st.session_state.data["dob"] = str(st.session_state.data["dob"])

    # Upload the file to S3
    json_string = json.dumps(st.session_state.data)

    # Upload JSON data to S3 bucket
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)

    print(f'{file_name} uploaded successfully to {bucket_name}.')

    st.session_state.data = {}
    st.switch_page("pages/page_6.py")
