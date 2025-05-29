from src.core.database.interfaces.units_of_work import SQLAlchemyAbstractUnitOfWork
from src.domains.users.adapters.repositories import SQLAlchemyUsersRepository
from src.domains.users.interfaces.units_of_work import UsersUnitOfWork


class SQLAlchemyUsersUnitOfWork(SQLAlchemyAbstractUnitOfWork, UsersUnitOfWork):
    async def __aenter__(self):
        uow = await super().__aenter__()
        self.users: SQLAlchemyUsersRepository = SQLAlchemyUsersRepository(session=self.session)
        return uow
