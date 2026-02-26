import pytest
from uuid import uuid4
from fastapi import Request, HTTPException
from unittest.mock import MagicMock
from src.security import (
    user_verification,
    ExpiredToken,
    InvalidToken
)


@pytest.fixture
def mock_injector():
    return MagicMock()


@pytest.fixture
def mock_request():
    return MagicMock(spec=Request)


@pytest.fixture
def mock_web_token_service():
    return MagicMock()


@pytest.fixture
def mock_encryption_service():
    return MagicMock()


def test_valid_token_with_encrypted_code(
    mock_injector,
    mock_request,
    mock_web_token_service,
    mock_encryption_service
):
    """Test successful verification with encrypted verification code."""
    encrypted_code = "encrypted_123456"
    decrypted_code = 123456
    
    mock_request.headers = {"Authorization": "Bearer valid_token"}
    
    # Mock the injector to return different services based on type
    def inject_side_effect(service_type):
        if service_type.__name__ == "WebTokenService":
            return mock_web_token_service
        elif service_type.__name__ == "EncryptionService":
            return mock_encryption_service
        return None
    
    mock_injector.inject.side_effect = inject_side_effect
    
    mock_web_token_service.decode.return_value = {"verification_code": encrypted_code}
    mock_encryption_service.decrypt.return_value = decrypted_code

    verification_code = user_verification(mock_request, mock_injector)
    
    assert isinstance(verification_code, int)
    assert verification_code == 123456
    mock_web_token_service.decode.assert_called_once_with("valid_token")
    mock_encryption_service.decrypt.assert_called_once_with(encrypted_code)


def test_missing_authorization_header(
    mock_injector,
    mock_request
):
    """Test that missing Authorization header raises 401."""
    mock_request.headers = {}

    with pytest.raises(HTTPException) as exc_info:
        user_verification(mock_request, mock_injector)

    assert exc_info.value.status_code == 401
    assert "Unautrhorized" in exc_info.value.detail
    assert "Missing required auth headers" in exc_info.value.detail


def test_invalid_authorization_format(
    mock_injector,
    mock_request
):
    """Test that invalid Authorization format raises 401."""
    mock_request.headers = {"Authorization": "InvalidFormat token"}

    with pytest.raises(HTTPException) as exc_info:
        user_verification(mock_request, mock_injector)

    assert exc_info.value.status_code == 401
    assert "Unautrhorized" in exc_info.value.detail


def test_missing_verification_code_in_token(
    mock_injector,
    mock_request,
    mock_web_token_service
):
    """Test that token without verification_code raises 401."""
    mock_request.headers = {"Authorization": "Bearer valid_token"}
    
    mock_injector.inject.return_value = mock_web_token_service
    mock_web_token_service.decode.return_value = {"user_id": uuid4()}

    with pytest.raises(HTTPException) as exc_info:
        user_verification(mock_request, mock_injector)

    assert exc_info.value.status_code == 401
    assert exc_info.value.detail == "Invalid token"


def test_expired_token(
    mock_injector,
    mock_request,
    mock_web_token_service
):
    """Test that expired token raises 401."""
    mock_request.headers = {"Authorization": "Bearer expired_token"}
    
    mock_injector.inject.return_value = mock_web_token_service
    mock_web_token_service.decode.side_effect = ExpiredToken("Token expired")

    with pytest.raises(HTTPException) as exc_info:
        user_verification(mock_request, mock_injector)
    
    assert exc_info.value.status_code == 401
    assert exc_info.value.detail == "Token expired"


def test_invalid_token(
    mock_injector,
    mock_request,
    mock_web_token_service
):
    """Test that invalid token raises 401."""
    mock_request.headers = {"Authorization": "Bearer invalid_token"}
    
    mock_injector.inject.return_value = mock_web_token_service
    mock_web_token_service.decode.side_effect = InvalidToken("Invalid token signature")

    with pytest.raises(HTTPException) as exc_info:
        user_verification(mock_request, mock_injector)
    
    assert exc_info.value.status_code == 401
    assert exc_info.value.detail == "Invalid token signature"


def test_decryption_failure(
    mock_injector,
    mock_request,
    mock_web_token_service,
    mock_encryption_service
):
    """Test that decryption failure raises 401."""
    mock_request.headers = {"Authorization": "Bearer valid_token"}
    
    def inject_side_effect(service_type):
        if service_type.__name__ == "WebTokenService":
            return mock_web_token_service
        elif service_type.__name__ == "EncryptionService":
            return mock_encryption_service
        return None
    
    mock_injector.inject.side_effect = inject_side_effect
    
    mock_web_token_service.decode.return_value = {"verification_code": "encrypted_code"}
    mock_encryption_service.decrypt.side_effect = ValueError("Decryption failed")

    with pytest.raises(HTTPException) as exc_info:
        user_verification(mock_request, mock_injector)
    
    assert exc_info.value.status_code == 401
    assert exc_info.value.detail == "Decryption failed"


def test_non_numeric_verification_code(
    mock_injector,
    mock_request,
    mock_web_token_service,
    mock_encryption_service
):
    """Test that non-numeric decrypted code raises 401."""
    mock_request.headers = {"Authorization": "Bearer valid_token"}
    
    def inject_side_effect(service_type):
        if service_type.__name__ == "WebTokenService":
            return mock_web_token_service
        elif service_type.__name__ == "EncryptionService":
            return mock_encryption_service
        return None
    
    mock_injector.inject.side_effect = inject_side_effect
    
    mock_web_token_service.decode.return_value = {"verification_code": "encrypted_code"}
    mock_encryption_service.decrypt.return_value = "not_a_number"

    with pytest.raises(HTTPException) as exc_info:
        user_verification(mock_request, mock_injector)
    
    assert exc_info.value.status_code == 401