from src.core.database.interfaces.units_of_work import SQLAlchemyAbstractUnitOfWork
from src.domains.wishlists.adapters.repositories import SQLAlchemyWishlistsRepository
from src.domains.wishlists.interfaces.units_of_work import WishlistsUnitOfWork


class SQLAlchemyWishlistsUnitOfWork(SQLAlchemyAbstractUnitOfWork, WishlistsUnitOfWork):
    async def __aenter__(self):
        uow = await super().__aenter__()
        self.wishlist: SQLAlchemyWishlistsRepository = SQLAlchemyWishlistsRepository(session=self.session)
        return uow
