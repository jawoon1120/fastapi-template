
class Token():
    access_token: str
    token_type: str


class TokenPayload():
    user_id: int
    user_email:str

    def __init__(self, user_id:int, user_email:str):
        self.user_id = user_id
        self.user_email = user_email

    def __iter__(self):
        yield 'user_id', self.user_id
        yield 'user_email', self.user_email