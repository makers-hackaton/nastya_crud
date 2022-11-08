from db import Base
from sqlalchemy import String, Integer, Text, Column

class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(Text)




# from pydantic import BaseModel

# from typing import Optional
# from uuid import UUID, uuid4
# from enum import Enum


# class Gender(str, Enum):
#     male = 'male'
#     female = 'female'   

# class User(BaseModel):
#     id: Optional[UUID] = uuid4()
#     first_name: str
#     last_name: str
#     gender: Gender
#     is_admin: bool = False
#     is_active: bool = False

