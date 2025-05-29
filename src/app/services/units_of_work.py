from sqlalchemy.ext.asyncio import async_sessionmaker

from src.domains.carts.services.units_of_work import SQLAlchemyCartsUnitOfWork
from src.app.interfaces.units_of_work import CommonUserUnitOfWork
from src.core.database.interfaces.units_of_work import SQLAlchemyAbstractUnitOfWork
from src.core.database.connection import async_sessionmaker as default_sessionmaker
from src.domains.products.services.units_of_work import SQLAlchemyProductsUnitOfWork
from src.domains.users.services.units_of_work import SQLAlchemyUsersUnitOfWork
from src.domains.wishlists.services.units_of_work import SQLAlchemyWishlistsUnitOfWork


class SQLAlchemyCommonUnitOfWork(SQLAlchemyAbstractUnitOfWork, CommonUserUnitOfWork):
    def __init__(self, session_maker: async_sessionmaker = default_sessionmaker, auto_commit: bool = False) -> None:
        super().__init__(session_maker=session_maker, auto_commit=auto_commit)
        self.session = self._session_maker()

        self.users = SQLAlchemyUsersUnitOfWork(
            auto_commit=self._auto_commit, auto_close=self._auto_commit, session=self.session
        )
        self.carts = SQLAlchemyCartsUnitOfWork(
            auto_commit=self._auto_commit, auto_close=self._auto_commit, session=self.session
        )
        self.wishlists = SQLAlchemyWishlistsUnitOfWork(
            auto_commit=self._auto_commit, auto_close=self._auto_commit, session=self.session
        )
        self.products = SQLAlchemyProductsUnitOfWork(
            auto_commit=self._auto_commit, auto_close=self._auto_commit, session=self.session
        )

    async def __aenter__(self):
        uow = await super().__aenter__()
        await self.session.close()
        return uow
