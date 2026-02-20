from uuid import UUID
from fastapi import APIRouter, Request, Depends
from src.di import get_injector, Injector
from src.security import (
    user_verification, 
    user_authentication, 
    PermissionsException
)
from ...domain import (
    UserPublic,
    CreateUserSchema,
)
from ...application import (
    DeleteUser,
    CreateUser
)

router = APIRouter(
    prefix="/users",
)

@router.post("/", status_code=200, response_model=UserPublic)
async def create_user(
    request: Request,
    data: CreateUserSchema,
    verification_code: int = Depends(user_verification),
    injector: Injector = Depends(get_injector)
):
    if int(verification_code) != int(data.verification_code):
        raise PermissionsException(detail="Verification failed", status_code=401)
    
    use_case: CreateUser = injector.inject(CreateUser)
    
    return await use_case.execute(
        data=data,
        profile_type="OWNER"
    )

@router.delete("/", status_code=200, response_model=UserPublic)
async def delete_user(
    request: Request,
    user_id: UUID = Depends(user_authentication),
    injector: Injector = Depends(get_injector)
):
    use_case: DeleteUser = injector.inject(DeleteUser)

    return await use_case.execute(
        user_id=user_id
    )