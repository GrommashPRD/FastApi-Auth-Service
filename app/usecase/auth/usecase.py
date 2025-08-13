from app.api.handlers.auth.schemas import SUserAuth
from app.repository.users.repo import UsersRepo
from sqlalchemy.ext.asyncio import AsyncSession
from app import auth
from app.repository.exceptions import RecordAlreadyExist
from app.usecase.auth.exceptions import UserAlreadyExist, UserNotFound, WrongPassword


async def registration(
        session: AsyncSession,
        registration_data: SUserAuth,
):
    hashed_password = auth.hash_password(registration_data.password)
    try:
        user = await UsersRepo.add_new(
            session,
            check_conditions={"username": registration_data.username},
            username=registration_data.username,
            password=hashed_password
        )
    except RecordAlreadyExist:
        raise UserAlreadyExist(detail="Username already exist")

    session.add(user)
    await session.commit()

    return user

async def login(
        response,
        login_data: SUserAuth
):

    user = await UsersRepo.find_one_or_none(username=login_data.username)

    if not user:
        raise UserNotFound(detail=login_data.username)
    elif not auth.verify_password(login_data.password, user.password):
        raise WrongPassword(detail="Incorrect password")

    access_token = auth.create_access_token({"sub": str(user.id)})

    response.set_cookie(
        "access_token",
        access_token,
        httponly=True,
    )

    return user
