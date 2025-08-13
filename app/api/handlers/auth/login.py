from fastapi import Response, APIRouter, HTTPException
from app.database import async_session_maker
from app.metrics import SUCCESS_LOGINS, FAILED_LOGINS
from app.usecase.auth import usecase
from app.api.handlers.auth.schemas import SUserAuth
from app.usecase.auth.exceptions import UserNotFound, WrongPassword
from app.logger import logger

router = APIRouter()

@router.post("/login/")
async def register_user(
        response: Response,
        login_data:SUserAuth
):
    async with async_session_maker() as session:
        try:
            user = await usecase.login(
                response,
                login_data
            )
            SUCCESS_LOGINS.inc()
        except UserNotFound as e:
            FAILED_LOGINS.inc()
            logger.warning("User not found %s", e)
            raise HTTPException(detail="Username not found", status_code=404)
        except WrongPassword:
            FAILED_LOGINS.inc()
            logger.warning("Incorrect password")
            raise HTTPException(detail="Incorrect password for username: '%s' " %login_data.username, status_code=400)

        return {
            "message": "OK",
            "user_id": user.id
        }
