import streamlit as st

from src import setup,DatabaseHandler

setup()

db : DatabaseHandler = st.session_state.db

st.title("🏋🏻 Track Workout")


with st.expander(
    "Create "
):
    with st.form(
        key="workout_form",
        clear_on_submit=True,
        border=True
    ):
        st.selectbox(
            label="Exercise Type",
            options=["Pull","Push","Leg", "Cardio"],
            index=0,
            key="exercise_type"
            ) 
        st.toggle(
            label="Is the workout calesthenics?",
            value=False,
            key="is_calisthenics"
            )

        if st.form_submit_button(label="Confirm"):
            db.add_workout(category=st.session_state.exercise_type,is_calisthenics=st.session_state.is_calisthenics) 
            st.success("Workout created")
        