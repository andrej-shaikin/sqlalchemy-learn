from sqlalchemy import Column, Integer, String

from db import BaseModel


class Student(BaseModel):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    patronymic = Column(String)
    age = Column(Integer)
    username = Column(String)
