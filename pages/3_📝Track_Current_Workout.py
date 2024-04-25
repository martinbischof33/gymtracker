import streamlit as st
import time

from src import setup,DatabaseHandler

setup()

db: DatabaseHandler = st.session_state.db

st.title("📝 Track Current Workout")
    
if db.is_running():
    finish_workout_button = st.button("Finish")

    if finish_workout_button:
        db.finish_current_workout()
        st.balloons()
        time.sleep(2.5)
        st.switch_page("🏋🏻Workout.py")
else:
    st.success("Workout successfully finished")

