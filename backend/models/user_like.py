from sqlalchemy import select, ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column
from typing import Self

from .db_session import Base


class UserLike(Base):
    __tablename__ = "users_likes"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id = mapped_column(ForeignKey("users.id"))
    product_id = mapped_column(ForeignKey("products.id"))

    @classmethod
    async def get_user_like(cls, like_id: int, session: AsyncSession) -> Self:
        """
        Get user like by id

        :param like_id: id of user like
        :param session: database session
        :return: UserLike
        """

        _ = await session.execute(select(cls).where(cls.id == like_id))
        return _.scalar()

    async def save(self, session: AsyncSession):
        session.add(self)
        await session.commit()
