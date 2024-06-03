
from pydantic import BaseModel


class EnquiryDetail(BaseModel):
    name: str
    author: str
    description: str