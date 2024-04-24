import streamlit as st
from src import authenticate,get_db

def setup():
    # setup page configuration
    st.set_page_config(
        page_title="Gym Tracker",
        page_icon="🏋🏻",
        layout="centered",
        initial_sidebar_state="auto"
    )
    # login form
    authenticate()
    # save db conection to st.sessionstate 
    get_db()