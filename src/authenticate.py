# Third Party Imports
import streamlit as st
import streamlit_authenticator as stauth

# Built-in Imports
import yaml
from yaml.loader import SafeLoader


PATH_AUTHENTICATOR_CREDENTIALS = ".streamlit/config.yaml"


def authenticate() -> None:

    # Get credentials from the yaml file
    with open(PATH_AUTHENTICATOR_CREDENTIALS) as file:
        config = yaml.load(file, Loader=SafeLoader)

    # Create the authenticator
    authenticator = stauth.Authenticate(
        config["credentials"],
        config["cookie"]["name"],
        config["cookie"]["key"],
        config["cookie"]["expiry_days"],
    )

    # Login with cookie or show login form
    authenticator.login()

    st.session_state["authenticator"] = authenticator

    if st.session_state["authentication_status"]:
        authenticator.logout(location="sidebar")
    elif st.session_state["authentication_status"] is False:
        st.error("Username/password is incorrect")
    elif st.session_state["authentication_status"] is None:
        st.warning("Please enter your username and password")
    else:
        st.error("Login failed")

    # ! Only show the app if the user is authenticated
    if not st.session_state["authentication_status"]:
        st.stop()
