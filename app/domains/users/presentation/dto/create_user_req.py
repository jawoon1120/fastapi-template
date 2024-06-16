from pydantic import BaseModel

class CreateUserRequestDTO(BaseModel):
    email:str
    password:str