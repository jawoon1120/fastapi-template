from datetime import datetime, timedelta, timezone
from app.domains.auth.domain.token import TokenPayload
from app.domains.users.application.user_service import UserService
from fastapi import Depends
from app.configs.app_config import get_algorithm, get_token_expire_minutes, get_token_secret_key
from passlib.context import CryptContext
import jwt

from app.domains.users.infra.user_entity import UserEntity

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = get_algorithm()
SECRET_KEY = get_token_secret_key()
ACCESS_TOKEN_EXPIRE_MINUTES = get_token_expire_minutes()

class AuthService:
    def __init__(
        self,
        user_service: UserService = Depends(UserService)
    ):
        self.user_service: UserService = user_service
        pass

    async def authenticate_user(self, email: str, password: str) -> UserEntity:
        user = await self.user_service.get_user_or_none(email=email)
        if not user:
            return False
        if not self.verify_password(password, user.password):
            return False
        return user

    def create_access_token(self, token_payload: TokenPayload):
        to_encode = dict(token_payload)
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    def verify_password(self, plain_password:str, hashed_password:str):
        return pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password:str) -> str:
        return pwd_context.hash(password)
