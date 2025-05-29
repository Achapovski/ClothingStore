from src.domains.collections.adapters.repositories import CollectionsRepository
from src.core.database.interfaces.units_of_work import SQLAlchemyAbstractUnitOfWork
from src.domains.collections.interfaces.units_of_work import CollectionsUnitOfWork


class SQLAlchemyCollectionsUnitOfWork(SQLAlchemyAbstractUnitOfWork, CollectionsUnitOfWork):
    async def __aenter__(self):
        uow = await super().__aenter__()
        self.collections: CollectionsRepository = CollectionsRepository(session=self.session)
        return uow
