from app.repository.base import BaseDAO
from app.repository.users.models import User


class UsersRepo(BaseDAO):
    model = User
