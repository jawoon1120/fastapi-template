from __future__ import annotations
from datetime import datetime, timedelta, timezone
from fastapi import Depends
from typing import TYPE_CHECKING

from app.configs.app_config import get_algorithm, get_token_secret_key
from passlib.context import CryptContext
import jwt

if TYPE_CHECKING:
    from app.domains.users.application.user_service import UserService

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = get_algorithm()
SECRET_KEY = get_token_secret_key()

class AuthService:
    def __init__(self):
        self.user_service: 'UserService' = Depends('UserService')

    async def authenticate_user(self, email: str, password: str):
        user = await self.user_service._get_user_or_none(email=email)
        if not user:
            return False
        if not self._verify_password(password, user.password):
            return False
        return user


    def create_access_token(data: dict, expires_delta: timedelta| None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    def _verify_password(plain_password:str, hashed_password:str):
        return pwd_context.verify(plain_password, hashed_password)

