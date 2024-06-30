from pydantic import BaseModel

class CreateUserResponseDTO(BaseModel):
    id : int
    