from sqlalchemy import Column, Date, Integer, ForeignKey, String, Float, Boolean, Time
from sqlalchemy.sql import func
from src import Base


class Exercise(Base):
    __tablename__ = "exercise"
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String, nullable=False)
    category_id: int = Column(Integer, ForeignKey("category.id"), nullable=False)
    base_weight: float = Column(Float, nullable=False, default=0)
    is_timed: bool = Column(Boolean, nullable=False, default=False)
    target_muscle_group = Column(String, nullable=False)


class Workout(Base):
    __tablename__ = "workout"  # list of excersises on one day (1:n) 
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    date: Date = Column(Date, default=func.current_date(), nullable=False)
    category_id: int = Column(Integer, ForeignKey("category.id"), nullable=False)
    session: int = Column(Integer, nullable=False, default=1)  # what session of the day is the workout
    is_calisthenics = Column(Boolean, nullable=False, default=False)
    person: str = Column(String, nullable=False, default="Martin")
    is_running: bool = Column(Boolean, nullable=False, default=False)


class MappingWorkoutExercise(Base):
    __tablename__ = "mapping_w_e"
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    workout_id: int = Column(Integer, ForeignKey("workout.id"))
    exercise_id: int = Column(Integer, ForeignKey("exercise.id"))
    set: int = Column(Integer, nullable=False, default=3)
    repetition: int = Column(Integer, nullable=True)
    weight: float = Column(Float, nullable=True)
    is_weight_seperated: bool = Column(Boolean, nullable=False, default=False)  # if weight is separated on both sides.
    duration: Time = Column(Time, nullable=True)


class Category(Base):
    __tablename__ = "category"
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String, nullable=False)


class BodyMeasurement(Base):
    __tablename__ = "body_measurement"
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    date: Date = Column(Date, default=func.current_date(), nullable=False)
    weight: float = Column(Float,nullable=False)
    bodyfat_percentage: float = Column(Float, nullable=False)
    muscle_percentage: float = Column(Float, nullable=False)
    water_percentage: float = Column(Float, nullable=False)
    belly_circumference: float = Column(Float, nullable=False)
    waistline_circumference: float = Column(Float, nullable=False)
    biceps_circumference: float = Column(Float, nullable=False)
    upper_leg_circumference: float = Column(Float, nullable=False)
    lower_leg_circumference: float = Column(Float, nullable=False)
