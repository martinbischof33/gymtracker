import streamlit as st
from .db_handler import get_db

def setup():
    # setup page configuration
    st.set_page_config(
        page_title="Gym Tracker",
        page_icon="🏋🏻",
        layout="centered",
        initial_sidebar_state="auto"
    )
    # save db conection to st.sessionstate 
    get_db()