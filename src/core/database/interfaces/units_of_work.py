from typing import Self

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from src.core.database.connection import async_sessionmaker as default_sessionmaker
from src.core.interfaces.units_of_work import AbstractUnitOfWork


class SQLAlchemyAbstractUnitOfWork(AbstractUnitOfWork):
    def __init__(
            self,
            session_maker: async_sessionmaker = default_sessionmaker,
            auto_commit: bool = True,
            auto_close: bool = True,
            session: AsyncSession = None
    ) -> None:
        super().__init__(auto_commit=auto_commit)
        self.auto_close = auto_close
        self._session_maker: async_sessionmaker = session_maker
        self.session: AsyncSession = session

    async def __aenter__(self) -> Self:
        if not self.session:
            self.session: AsyncSession = self._session_maker()
        return await super().__aenter__()

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await super().__aexit__(exc_type, exc_val, exc_tb)
        if self.auto_close:
            await self.session.close()

    async def commit(self) -> None:
        await self.session.commit()

    async def rollback(self) -> None:
        self.session.expunge_all()
        await self.session.rollback()
