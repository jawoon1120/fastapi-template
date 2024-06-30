from fastapi import HTTPException
from fastapi.security import HTTPBearer
from jwt import ExpiredSignatureError
from starlette.requests import Request
import jwt

from app.configs.app_config import get_algorithm, get_token_secret_key

SECRET_KEY = get_token_secret_key()
ALGORITHM = get_algorithm()

class AuthRequired(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(AuthRequired, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            raise HTTPException(status_code=401, detail="header에 토큰이 없습니다")

        token_type, token = auth_header.split(" ")

        if token_type != "Bearer":
            raise HTTPException(status_code=401, detail="토큰이 Bearer 타입이 아닙니다")

        try:
            request.state.token_info = jwt.decode(jwt=token, key=SECRET_KEY, algorithms=ALGORITHM)
        except ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="토큰이 만료되었습니다")
        except Exception:
            raise HTTPException(status_code=401, detail="토큰이 유효하지 않습니다")