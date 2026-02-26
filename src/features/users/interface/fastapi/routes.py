from uuid import UUID
from fastapi import APIRouter, Request, Depends, Body
from src.di import get_injector, Injector
from src.security import (
    user_verification, 
    user_authentication, 
    PermissionsException
)
from ...domain import (
    UserPublic,
    CreateUserRequest,
    UserLoginRequest
)
from ...application import (
    DeleteUser,
    CreateUser,
    UserLogin
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", status_code=200, response_model=UserPublic)
async def create_user(
    request: Request,
    data: CreateUserRequest = Body(...),
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


@router.post("/login", status_code=200, response_model=UserPublic)
def user_login(
    request: Request,
    data: UserLoginRequest = Body(...),
    injector: Injector = Depends(get_injector)
):
    use_case: UserLogin = injector.inject(UserLogin)

    return use_case.execute(
        email=data.email,
        password=data.password
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