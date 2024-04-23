from sqlalchemy import Column,Date, Integer
from sqlalchemy.sql import func
from src import Base

class Exercise(Base):
    __tablename__ = "exercise"
    id = Column(Integer,primary_key=True)
    date = Column(Date,default=func.current_date())
    

class Workout(Base):
    ...
    

class Category(Base):
    ...
    

class Measuremenet(Base):
    ...