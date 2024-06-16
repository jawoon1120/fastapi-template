from datetime import timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.configs.app_config import get_token_expire_minutes
from app.domains.auth.application.auth_service import AuthService
from app.domains.auth.presentation.dto.get_token_res_dto import TokenResDTO

ACCESS_TOKEN_EXPIRE_MINUTES = get_token_expire_minutes()
router = APIRouter(tags=["auth"])

@router.post("/token")
async def issue_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    auth_service : Annotated[AuthService, Depends(AuthService)]
) -> TokenResDTO:
    
    user = auth_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token =  auth_service.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    return TokenResDTO(access_token=access_token, token_type="bearer")
