from fastapi import APIRouter, Body, Depends, Request
from src.security import user_authentication
from src.di import Injector, get_injector
from ...domian import AccountPublic, CreateAccountRequest
from ...application import CreateAccount


router = APIRouter(
    prefix="/banking",
    tags=["Banking"],
    dependencies=[Depends(user_authentication)]
)

@router.post("/accounts/", status_code=201, response_model=AccountPublic)
def create_account(
    request: Request,
    data: CreateAccountRequest = Body(...),
    injector: Injector = Depends(get_injector)
):
    """
    Insert bank account info into db
 
    """
    use_case: CreateAccount = injector.inject(CreateAccount)
    return use_case.execute(
        data=data
    )