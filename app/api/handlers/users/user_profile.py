from fastapi import APIRouter, HTTPException
from app.database import async_session_maker
from app.dependencies import CurrentUserDep
from app.repository.users.models import User
from app.usecase.users import usecase
from app.usecase.users.exceptions import UserNotAuthorization

router = APIRouter()

@router.get("/my_profile")
async def profile(
        user: User = CurrentUserDep
):
    async with async_session_maker() as session:
        try:
            user = await usecase.user_profile(user)
        except UserNotAuthorization:
            raise HTTPException(detail="Log in for check this page", status_code=401)

        return {
            'message': 'OK',
            'information': user
        }