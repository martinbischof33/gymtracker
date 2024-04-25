from datetime import date
import streamlit as st

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

from src import Base
from src.models  import Workout,Exercise,MappingWorkoutExercise,BodyMeasurement,Category


DB_PATH = "sqlite:///db.sqlite"

class DatabaseHandler:

    def __init__(self) -> None:
        self.engine = create_engine(DB_PATH)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.create_tables()
        # create the categories the first time the db is created
        if not self.get_categories():
            self.create_categories()

    def create_tables(self) -> None:
        Base.metadata.create_all(self.engine)

    def create_categories(self) -> None:
        for c in ["Pull", "Push", "Leg", "Cardio", "Something Else"]:
            cat = Category(name=c)
            self.session.add(cat)
        self.session.commit()

    def add_workout(self,category_id:int, is_calisthenics:bool) -> None:
        today = date.today()
        workout_count:int = self.session.query(func.count(Workout.id)).filter(Workout.date == today).scalar()

        workout: Workout = Workout(
            date=today,
            category_id= category_id,
            session = workout_count + 1,
            is_calisthenics = is_calisthenics,    
            is_running=True
        )
        self.session.add(workout)
        self.session.commit()

    def add_exercise(self,name:str,category_id:int,base_weight:float,is_timed:bool,muscle:str) -> None:
        exercise: Exercise = Exercise(
            name=name,
            category_id= category_id,
            base_weight=base_weight,
            is_timed=is_timed,
            target_muscle_group=muscle,
        )
        self.session.add(exercise)
        self.session.commit()

    def get_categories(self) -> list[Category]:
        return self.session.query(Category).all()
    
    def get_exercises(self) -> list[Exercise]:
        return self.session.query(Exercise).all()
        
    def is_running(self) -> bool:
        return self.session.query(func.count(Workout.id)).filter(Workout.is_running == True).scalar() > 0
    
    def finish_current_workout(self) -> None:
        running_workout = self.session.query(Workout).filter(Workout.is_running == True).first()
        if running_workout:
            running_workout.is_running = False
            self.session.commit()

    def delete_exercises(self,ids:list[int]):
        self.session.query(Exercise).filter(Exercise.id.in_(ids)).delete(synchronize_session=False)
        self.session.commit()

def get_db() -> None:
    if st.session_state.get("db") is None:
        st.session_state.db = DatabaseHandler()
    

    



    
