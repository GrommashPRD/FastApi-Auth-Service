from fastapi import Request, HTTPException, Depends
from jose import jwt, JWTError

from app.config import settings
from datetime import datetime

from app.repository.users.repo import UsersRepo
from app.usecase.users.exceptions import UserNotAuthorization


def get_token(request: Request):
    token = request.cookies.get('access_token')
    if not token:
        raise UserNotAuthorization(status_code=401, detail="Not authorized")
    return token

async def get_curr_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token,
            key=settings.SECRET_KEY,
            algorithms=settings.ALGORITHM
        )
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    expire: str = payload.get('exp')
    if not expire or (int(expire) < datetime.utcnow().timestamp()):
        raise HTTPException(status_code=401, detail="Invalid token")
    user_id: str = payload.get('sub')
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = await UsersRepo.find_by_id(str(user_id))
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")

    return user


CurrentUserDep = Depends(get_curr_user)

