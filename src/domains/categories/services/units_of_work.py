from src.domains.categories.adapters.repositories import SQLAlchemyCategoriesRepository
from src.domains.categories.interfaces.units_of_work import CategoriesUnitOfWork
from src.core.database.interfaces.units_of_work import SQLAlchemyAbstractUnitOfWork


class SQLAlchemyCategoriesUnitOfWork(SQLAlchemyAbstractUnitOfWork, CategoriesUnitOfWork):
    async def __aenter__(self):
        uow = await super().__aenter__()
        self.categories: SQLAlchemyCategoriesRepository = SQLAlchemyCategoriesRepository(session=self.session)
        return uow
