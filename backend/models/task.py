from sqlalchemy import select, ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column
from typing import Self

from .db_session import Base


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id = mapped_column(ForeignKey("products.id"))

    @classmethod
    async def get_task(cls, task_id: int, session: AsyncSession) -> Self:
        """
        Get task  by id

        :param task_id: id of task
        :param session: database session
        :return: Task
        """

        _ = await session.execute(select(cls).where(cls.id == task_id))
        return _.scalar()

    async def save(self, session: AsyncSession):
        session.add(self)
        await session.commit()
