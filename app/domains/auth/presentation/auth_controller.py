
from typing import Annotated
from fastapi import APIRouter, Depends, status, HTTPException

from app.domains.auth.application.auth_service import AuthService
from app.domains.auth.domain.token import TokenPayload
from app.domains.auth.presentation.dto.get_token_req_dto import TokenReqDTO
from app.domains.auth.presentation.dto.get_token_res_dto import TokenResDTO

router = APIRouter(tags=["auth"])

@router.post(
    "/tokens",
)
async def issue_token(
    body: TokenReqDTO,
    auth_service : Annotated[AuthService, Depends(AuthService)]
) -> TokenResDTO:
    
    user = await auth_service.authenticate_user(email=body.email, password=body.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token =  auth_service.create_access_token(
        token_payload=TokenPayload(
            user_id=user.id,
            user_email=user.email,
        )
    )

    return TokenResDTO(access_token=access_token, token_type="bearer")
