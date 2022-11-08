from pydantic import BaseModel

class ItemSerializer(BaseModel):
    id:int
    name:str
    description:str

    class Config:
        orm_mode = True

class ItemCreateUpdateSerializer(BaseModel):
    name:str
    description:str

    class Config:
        orm_mode = True
