from fastapi import APIRouter, Request, Body, Depends, HTTPException
from src.di import get_injector, Injector
from src.security import get_random_code, HashingService
from src.persistance import ResourceExists
from src.features.users import UserRepository
from ...domain import VerifyEmailRequest
from ...application import VerifyEmail


router = APIRouter(
    prefix="/email"
)

async def email_in_use_check(
    injector: Injector = Depends(get_injector),
    data: VerifyEmailRequest = Body(...)
):
    """
    Check if email is in use, 
    will throw 409 exceptions if a user is found in the repository
    Use with Depends() 
    """
    user_repository = injector.inject(UserRepository)
    hashing: HashingService = injector.inject(HashingService)
    
    checker = ResourceExists(
        repository=user_repository
    )

    email_in_use = await checker.validate(
        key="email_hash",
        value=hashing.hash_for_search(data=data.email),
        throw_error=False # no error thrown if not found 
    )

    if email_in_use:
        raise HTTPException(status_code=409, detail="Email in use")



@router.post("/", status_code=200)
def verify_email(
    request: Request,
    data: VerifyEmailRequest = Body(...),
    injector: Injector = Depends(get_injector),
    _: None = Depends(email_in_use_check)
):
    use_case: VerifyEmail = injector.inject(VerifyEmail)

    verification_code = get_random_code()

    return use_case.execute(
        to=data.email,
        verification_code=verification_code
    )