from app.database import async_session_maker
from sqlalchemy import select, insert, and_
from app.repository.exceptions import  RecordAlreadyExist


class BaseDAO:
    model = None

    @classmethod
    async def find_by_id(cls, id: str):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=id)
            result = await session.execute(query)
            return result.scalars().first()

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().first()

    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def add_new(cls, session, check_conditions: dict = None, **data):

        if check_conditions is None:
            check_conditions = {}

        if check_conditions:
            existing_record_stmt = select(cls.model).where(
                and_(getattr(cls.model, key) == value for key, value in check_conditions.items())
            )

            existing_record = await session.execute(existing_record_stmt)

            if existing_record.scalars().first():
                raise RecordAlreadyExist("Record already exists.", status_code=409)

        new_record_instance = cls.model(**data)

        return new_record_instance