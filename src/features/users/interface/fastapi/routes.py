from uuid import UUID
from fastapi import APIRouter, Request, Depends
from src.di import get_injector, Injector
from src.security import authenticate_user
from ...domain import (
    UserPublic
)

router = APIRouter(
    prefix="/users"
)

@router.post("/", status_code=200, response_model=UserPublic)
async def create_user(
    request: Request
):
    pass

@router.delete("/", status_code=200, response_model=UserPublic)
async def delete_user(
    request: Request,
    user_id: UUID = Depends(authenticate_user),
    injector: Injector = Depends(get_injector)
):
    pass 