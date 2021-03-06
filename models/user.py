import sqlalchemy as sa
from sqlalchemy import Column, DateTime, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base
from config import config
from helpers.irc import irc
from middleware.errors import CustomHTTPException
from models.role import Role
from models.user_group import UserGroup
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=True, unique=True)
    password = Column(String, nullable=False)
    name = Column(String, nullable=True)
    image = Column(String, nullable=True, default='/media/avatars/default.png')
    facebook_id = Column(String, nullable=True)
    google_id = Column(String, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    @staticmethod
    async def get_user_by_facebook_id(facebook_id: str) -> list:
        async with config['db'].acquire() as conn:
            query = sa.select([sa_user.c.id,
                               sa_user.c.email,
                               sa_user.c.password,
                               sa_user.c.name,
                               sa_user.c.image
                               ]) \
                .select_from(sa_user) \
                .where(sa_user.c.facebook_id == facebook_id)
            users = list(map(lambda x: dict(x), await conn.execute(query)))
            return users[0] if len(users) == 1 else None

    @staticmethod
    async def get_user_by_google_id(google_id: str) -> list:
        async with config['db'].acquire() as conn:
            query = sa.select([sa_user.c.id,
                               sa_user.c.email,
                               sa_user.c.password,
                               sa_user.c.name,
                               sa_user.c.image
                               ]) \
                .select_from(sa_user) \
                .where(sa_user.c.google_id == google_id)
            users = list(map(lambda x: dict(x), await conn.execute(query)))
            return users[0] if len(users) == 1 else None

    @staticmethod
    async def get_user_by_email(email: str) -> list:
        async with config['db'].acquire() as conn:
            query = sa.select([sa_user.c.id,
                               sa_user.c.email,
                               sa_user.c.password,
                               sa_user.c.name,
                               sa_user.c.image
                               ]) \
                .select_from(sa_user) \
                .where(sa_user.c.email == email)
            return list(map(lambda x: dict(x), await conn.execute(query)))

    @staticmethod
    async def get_user_by_id(user_id: int):
        async with config['db'].acquire() as conn:
            query = sa.select([sa_user.c.id,
                               sa_user.c.email,
                               sa_user.c.password,
                               sa_user.c.name,
                               sa_user.c.image
                               ]) \
                .select_from(sa_user) \
                .where(sa_user.c.id == user_id)
            users = list(map(lambda x: dict(x), await conn.execute(query)))
            return users[0] if len(users) == 1 else None

    @staticmethod
    async def create_user(data: dict) -> int:
        if 'roles' not in data:
            raise CustomHTTPException(irc['ACCESS_DENIED'], 401)
        roles = data['roles']
        del data['roles']
        async with config['db'].acquire() as conn:
            query = sa_user.insert().values(data)
            user = list(map(lambda x: dict(x), await conn.execute(query)))
            if len(user) != 1:
                raise CustomHTTPException(irc['INTERNAL_SERVER_ERROR'], 500)
            new_user_id = user[0]['id']

            for role in roles:
                found_role = await Role.get_role_by_name(role)
                if not found_role:
                    raise CustomHTTPException(irc['ROLE_NOT_FOUND'], 404)

                await UserGroup.add_role_to_user(new_user_id, found_role['id'])
        return new_user_id

    @classmethod
    async def get_users_without_self(cls, id: int) -> list:
        async with config['db'].acquire() as conn:
            query = sa.select([sa_user.c.id,
                               sa_user.c.email,
                               sa_user.c.password,
                               sa_user.c.name,
                               sa_user.c.image
                               ]) \
                .select_from(sa_user) \
                .where(sa_user.c.id != id) \
                .order_by(sa_user.c.name)
            return list(map(lambda x: dict(x), await conn.execute(query)))

    @classmethod
    async def get_users_by_id_list(cls, ids: list) -> list:
        async with config['db'].acquire() as conn:
            query = sa.select([sa_user.c.id,
                               sa_user.c.email,
                               sa_user.c.name,
                               sa_user.c.image
                               ]) \
                .select_from(sa_user) \
                .where(sa_user.c.id.in_(ids))
            return list(map(lambda x: dict(x), await conn.execute(query)))


sa_user = User.__table__
