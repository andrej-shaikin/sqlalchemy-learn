from sqlalchemy import Column, Integer, String

from db import BaseModel


class Student(BaseModel):
    __tablename__ = "students"

    id = Column(type_=Integer, primary_key=True, text="Identifier", index=True, unique=True, autoincrement=True)
    first_name = Column(type_=String, text="First name")
    last_name = Column(type_=String, text="Last name")
    patronymic = Column(type_=String, text="Patronymic")
    age = Column(type_=Integer, text="Age")
