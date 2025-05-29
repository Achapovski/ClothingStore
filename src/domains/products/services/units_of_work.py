from src.core.database.interfaces.units_of_work import SQLAlchemyAbstractUnitOfWork
from src.domains.products.adapters.repositories import SQLAlchemyProductsRepository
from src.domains.products.interfaces.units_of_work import ProductUnitOfWork


class SQLAlchemyProductsUnitOfWork(SQLAlchemyAbstractUnitOfWork, ProductUnitOfWork):
    async def __aenter__(self):
        uow = await super().__aenter__()
        self.products: SQLAlchemyProductsRepository = SQLAlchemyProductsRepository(session=self.session)
        return uow
