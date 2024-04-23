import streamlit as st

from sqlalchemy import create_engine,Column
from sqlalchemy.orm import sessionmaker

from src import Base




class DatabaseHandler:

    def __init__(self) -> None:
        self.engine = create_engine("sqlite:///db.sqlite")
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.create_tables()

    def create_tables(self) -> None:
        Base.metadata.create_all(self.engine)
        


def get_db() -> None:
    if st.session_state.get("db") is None:
        st.session_state.db = DatabaseHandler()
    

    



    
    