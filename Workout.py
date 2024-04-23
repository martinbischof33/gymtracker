import streamlit as st

from src.authenticate import authenticate
from src.configure import setup


setup()
authenticate()

st.title("🏋🏻 Gym Tracker")
