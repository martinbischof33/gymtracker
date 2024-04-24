from datetime import date
import streamlit as st

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

from src import Base
from src.models  import Workout,Exercise,MappingWorkoutExercise,BodyMeasurement




class DatabaseHandler:

    def __init__(self) -> None:
        self.engine = create_engine("sqlite:///db.sqlite")
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.create_tables()

    def create_tables(self) -> None:
        Base.metadata.create_all(self.engine)
        
    def add_workout(self,category:str,is_calisthenics:bool) -> None:
        
        today = date.today()
        workout_count:int = self.session.query(func.count(Workout.id)).filter(Workout.date == today).scalar()
        
        
        workout: Workout = Workout(
            date=today,
            category= category,
            session = workout_count + 1,
            is_calisthenics = is_calisthenics,    
        )
        self.session.add(workout)
        self.session.commit()
        
    

def get_db() -> None:
    if st.session_state.get("db") is None:
        st.session_state.db = DatabaseHandler()
    

    



    
    