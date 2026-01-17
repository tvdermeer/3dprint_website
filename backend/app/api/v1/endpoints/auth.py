"""
Authentication and User API endpoints.
"""

from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.database import get_db
from app.core.security import (
    create_access_token,
    create_password_reset_token,
    verify_password_reset_token,
)
from app.schemas.user import (
    UserCreate,
    UserResponse,
    PasswordResetRequest,
    PasswordResetConfirm,
    UserUpdate,
)
from app.services.user_service import UserService
from app.utils.email import send_password_reset_email

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login/access-token", response_model=dict)
def login_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests.
    """
    user = UserService.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password",
        )
    elif not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user"
        )
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    return {
        "access_token": create_access_token(
            data={"sub": str(user.id)}, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }


@router.post(
    "/signup", response_model=UserResponse, status_code=status.HTTP_201_CREATED
)
def create_user_signup(user_in: UserCreate, db: Session = Depends(get_db)) -> Any:
    """
    Create new user without the need to be logged in.
    """
    user = UserService.get_user_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system",
        )
    user = UserService.create_user(db, user_in)
    return user


@router.post("/password-recovery/{email}", response_model=dict)
def recover_password(email: str, db: Session = Depends(get_db)) -> Any:
    """
    Password Recovery
    """
    user = UserService.get_user_by_email(db, email=email)

    if not user:
        # We generally do not want to reveal if a user exists or not
        # so we return success regardless.
        # But for development/debugging it might be useful to know.
        # For this exercise, I'll return success to prevent user enumeration.
        return {"msg": "If the user exists, a password recovery email has been sent."}

    password_reset_token = create_password_reset_token(email=email)
    send_password_reset_email(to_email=email, token=password_reset_token)
    return {"msg": "Password recovery email sent"}


@router.post("/reset-password", response_model=dict)
def reset_password(body: PasswordResetConfirm, db: Session = Depends(get_db)) -> Any:
    """
    Reset password
    """
    email = verify_password_reset_token(body.token)
    if not email:
        raise HTTPException(status_code=400, detail="Invalid token")

    user = UserService.get_user_by_email(db, email=email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")

    user_update = UserUpdate(password=body.new_password)
    UserService.update_user(db, user, user_update)

    return {"msg": "Password updated successfully"}
