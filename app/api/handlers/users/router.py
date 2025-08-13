from fastapi import APIRouter

from app.api.handlers.users.user_profile import router as profile

router = APIRouter(
    prefix="/user",
    tags=["Работа с информацией пользователя"]
)

router.include_router(profile)
