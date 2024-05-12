from sqlalchemy import select, JSON
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column
from typing import Self

from .db_session import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    surname: Mapped[str]
    email: Mapped[str]
    phone: Mapped[str]
    cookies: Mapped[dict] = mapped_column(JSON)

    @classmethod
    async def get_user(cls, user_id: int, session: AsyncSession) -> Self:
        """
        Get user by id

        :param user_id: id of user
        :param session: database session
        :return: User
        """

        _ = await session.execute(select(cls).where(cls.id == user_id))
        return _.scalar()

    async def save(self, session: AsyncSession):
        session.add(self)
        await session.commit()
