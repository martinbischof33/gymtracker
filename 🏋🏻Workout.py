import streamlit as st

from src import setup, DatabaseHandler,Category

# Setup the application
setup()

# Create an instance of DatabaseHandler
db: DatabaseHandler = st.session_state.db
st.session_state.categories = db.get_categories()


# Display the title of the application
st.title("🏋🏻 Start Workout")

if db.is_running():
    if st.session_state.get("new_workout",False):
        st.success("Workout Created",icon="✅")
        st.session_state.new_workout = False
    else:
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
        category = st.selectbox(
            label="Exercise Type",
            options=[category.name for category in st.session_state.categories],
            index=0,
            key="category"
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
            category_id = [c.id for c in st.session_state.categories if c.name == category][0]
            db.add_workout(category_id=category_id, is_calisthenics=is_calisthenics)
            st.session_state.new_workout = True
            # Rerun the application
            st.rerun()