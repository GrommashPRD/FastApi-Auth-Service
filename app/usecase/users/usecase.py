from app.repository.users.models import User
from app.repository.users.repo import UsersRepo
from app.usecase.users.exceptions import UserNotAuthorization
from typing import Dict


async def user_profile(
        user: User
) -> Dict:
    if not user:
        raise UserNotAuthorization(detail="Log in for check this page")
    user_info = await UsersRepo.find_by_id(id=user.id)
    user_info_dict = {
        "user id": user_info.id,
        "username": user_info.username,
        "created_at": user_info.created_at,
        "updated_at": user_info.updated_at
    }

    return user_info_dict


