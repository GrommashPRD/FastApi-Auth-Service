from fastapi import Response, APIRouter

router = APIRouter()

@router.post("/logout/")
async def logout_user(response: Response):
    response.set_cookie("access_token", "", httponly=True, expires=0)

    return {
        "message": "OK"
    }