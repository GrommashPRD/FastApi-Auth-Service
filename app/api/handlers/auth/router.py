from fastapi import APIRouter

from app.api.handlers.auth.registration import router as registration
from app.api.handlers.auth.login import router as login
from app.api.handlers.auth.logout import router as logout

router = APIRouter(
    prefix="/auth",
    tags=["Авторизация"]
)

router.include_router(registration)
router.include_router(login)
router.include_router(logout)
