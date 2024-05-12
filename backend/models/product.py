from sqlalchemy import select, ARRAY, VARCHAR
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column
from typing import Self

from .db_session import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    link: Mapped[str]
    query: Mapped[list[str]] = mapped_column(ARRAY(VARCHAR), default=None)

    @classmethod
    async def get_product(cls, product_id: int, session: AsyncSession) -> Self:
        """
        Get product by id

        :param product_id: id of product
        :param session: database session
        :return: Product
        """

        _ = await session.execute(select(cls).where(cls.id == product_id))
        return _.scalar()

    async def save(self, session: AsyncSession):
        session.add(self)
        await session.commit()
