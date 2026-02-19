import pytest
from uuid import uuid4
from fastapi import Request, HTTPException
from unittest.mock import MagicMock
from src.security import (
    user_verification,
    ExpiredToken
)


@pytest.fixture
def mock_injector():
    return MagicMock()


@pytest.fixture
def mock_request():
    return MagicMock(spec=Request)

def test_valid_token(
    mock_injector,
    mock_request
):
    mock_request.headers = {"Authorization": "Bearer valid_token"}
    mock_web_token_service = MagicMock()
    mock_injector.inject.return_value = mock_web_token_service
    mock_web_token_service.decode.return_value = {"verification_code": 123456}

    verification_code = user_verification(mock_request, mock_injector)
    assert isinstance(verification_code, int)
    assert verification_code == 123456


def test_missing_headers(
    mock_injector,
    mock_request
):
    mock_request.headers = {}
    mock_web_token_service = MagicMock()
    mock_injector.inject.return_value = mock_web_token_service
    mock_web_token_service.decode.return_value = {}

    with pytest.raises(HTTPException) as exc_info:
        user_verification(mock_request, mock_injector)

    assert exc_info.value.status_code == 401
    assert exc_info.value.detail == "Unautrhorized. Missing required auth headers"



def test_missing_headers(
    mock_injector,
    mock_request
):
    mock_request.headers = {"Authorization": "Bearer invali_valid_token"}
    mock_web_token_service = MagicMock()
    mock_injector.inject.return_value = mock_web_token_service
    mock_web_token_service.decode.return_value = {"user_id": uuid4()}

    with pytest.raises(HTTPException) as exc_info:
        user_verification(mock_request, mock_injector)

    assert exc_info.value.status_code == 401
    assert exc_info.value.detail == "Invalid token"


def test_user_authentication_expired_token(mock_request, mock_injector):
    mock_request.headers = {"Authorization": "Bearer expired_token"}
    mock_web_token_service = MagicMock()
    mock_web_token_service.decode.side_effect = ExpiredToken("Token expired")
    mock_injector.inject.return_value = mock_web_token_service

    with pytest.raises(HTTPException) as exc:
        user_verification(mock_request, mock_injector)
    assert exc.value.status_code == 401
    assert exc.value.detail == "Token expired"

