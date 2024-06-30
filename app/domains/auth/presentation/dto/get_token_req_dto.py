from pydantic import BaseModel


class TokenReqDTO(BaseModel):
    email: str
    password: str