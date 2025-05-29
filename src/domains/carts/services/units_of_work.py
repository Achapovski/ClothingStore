from src.domains.carts.interfaces.units_of_work import CartsUnitOfWork
from src.domains.carts.adapters.repositories import SQLAlchemyCartsRepository
from src.core.database.interfaces.units_of_work import SQLAlchemyAbstractUnitOfWork


class SQLAlchemyCartsUnitOfWork(SQLAlchemyAbstractUnitOfWork, CartsUnitOfWork):
    async def __aenter__(self):
        uow = await super().__aenter__()
        self.carts: SQLAlchemyCartsRepository = SQLAlchemyCartsRepository(session=self.session)
        return uow
