import streamlit as st
import numpy as np
import pandas as pd

def main():
    st.title("Home")
    if st.button("Log In"):
        st.switch_page("pages/page_1.py")

if __name__ == "__main__":
    main()