import streamlit as st

from src import setup,DatabaseHandler,Category

setup()
db: DatabaseHandler = st.session_state.db

# save them into session state
st.session_state.categories =  db.get_categories()

st.title("🏃🏻‍♂️Exercises")


with st.form(key="exercise_form",clear_on_submit=True,border=False):
    name = st.text_input(label="Name of exercise",value=None,placeholder="Enter the name of the Exercise",key="name_exercise")
    muscle = st.text_input(label="Target Muscle (Group)",placeholder="Enter the name of the muscle", key="muscle")
    categories = [category.name for category in st.session_state.categories]
    category = st.selectbox(label="Category",options=categories,index=0,key="category")
    base_weight = st.number_input(label="Base Weight",placeholder="Enter the base weight of the Exercise", key="base_weight")
    is_timed = st.toggle(label="Is this a timed exersize?",value=False,key="is_timed")

    if st.form_submit_button(label="Confirm", type="primary"):

        category_id = [c.id for c in st.session_state.categories if c.name == category][0]
        db.add_exercise(name,category_id,base_weight,is_timed,muscle)
        st.session_state.new_exersize = True
        st.rerun()

if st.session_state.get("new_exersize",False):
    st.success("New exercise created",icon="✅")
    st.session_state.new_exersize = False


with st.expander("Delete Exercise",expanded=False):
    exersices = db.get_exercises()
    remove_exercises_names = st.multiselect(
        label="Exercises",
        options=[exercise.name for exercise in exersices],
        default=None,
        placeholder="Which exercises should be deleted",
        key="remove_exercise"
    )

    if st.button(label="Delete",type="primary"):
        ids = list(map(lambda obj: obj.id, filter(lambda obj: obj.name in remove_exercises_names,exersices)))
        db.delete_exercises(ids)
        st.rerun()

# with st.expander(label="Exercise List",expanded=False):
#     exersices = db.get_exercises()
#     exersices # TODO Format the output into a table
