import streamlit as st

from src import setup, DatabaseHandler

# Setup the application
setup()

# Create an instance of DatabaseHandler
db: DatabaseHandler = st.session_state.db

# Display the title of the application
st.title("🏋🏻 Start Workout")

if db.is_running():
    st.warning("There is already a Workout!",icon="💪🏻")
    switch = st.button("Switch to Workout Tracking", type="secondary")
    if switch:
        st.switch_page("pages/3_📝Track_Current_Workout.py")
    
else:
    # Create a form for adding a workout
    with st.form(
        key="workout_form",
        clear_on_submit=True,
        border=False
    ):
        # Select the exercise type
        exercise_type = st.selectbox(
            label="Exercise Type",
            options=["Pull", "Push", "Leg", "Cardio"],
            index=0,
            key="exercise_type"
        )
        # Toggle whether the workout is calesthenics or not
        is_calisthenics = st.toggle(
            label="Is the workout calesthenics?",
            value=False,
            key="is_calisthenics"
        )
        # Submit the form to add the workout
        if st.form_submit_button(label="Confirm", type="primary"):
            # Add the workout to the database
            db.add_workout(category=exercise_type, is_calisthenics=is_calisthenics)
            # Display a success message
            st.success("Workout created")
            # Rerun the application
            st.rerun()