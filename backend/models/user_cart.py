from sqlalchemy import select, ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column
from typing import Self

from .db_session import Base


class UserCart(Base):
    __tablename__ = "users_carts"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id = mapped_column(ForeignKey("users.id"))
    product_id = mapped_column(ForeignKey("products.id"))

    @classmethod
    async def get_user_cart(cls, cart_id: int, session: AsyncSession) -> Self:
        """
        Get user cart by id

        :param cart_id: id of user cart
        :param session: database session
        :return: UserCart
        """

        _ = await session.execute(select(cls).where(cls.id == cart_id))
        return _.scalar()

    async def save(self, session: AsyncSession):
        session.add(self)
        await session.commit()
