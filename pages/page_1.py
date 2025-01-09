import streamlit as st
import numpy as np
import pandas as pd

st.title("Surveys")

if st.button("Start Survey"):
    st.switch_page("pages/page_2.py")
