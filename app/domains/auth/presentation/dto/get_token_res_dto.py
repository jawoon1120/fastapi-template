from pydantic import BaseModel


class TokenResDTO(BaseModel):
    access_token: str
    token_type: str