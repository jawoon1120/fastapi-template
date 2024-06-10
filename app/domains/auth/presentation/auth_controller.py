from fastapi import APIRouter, Depends


router = APIRouter(tags=["auth"])

@router.post("/token")
async def issue_token():
    pass
