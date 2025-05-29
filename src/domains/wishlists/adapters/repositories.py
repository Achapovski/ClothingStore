from typing import Optional
from uuid import UUID, uuid4

from sqlalchemy import Result, insert, select, update

from src.core.database.interfaces.repositories import SQLAlchemyAbstractRepository
from src.domains.wishlists.adapters.models import Wishlist
from src.domains.wishlists.domain.models import WishlistModel
from src.domains.wishlists.interfaces.repositories import WishlistsAbstractRepository


class SQLAlchemyWishlistsRepository(SQLAlchemyAbstractRepository, WishlistsAbstractRepository):
    async def add(self, model: WishlistModel) -> Optional[WishlistModel]:
        result: Result = await self.session.execute(
            insert(Wishlist).values(id=uuid4(), **model.model_dump()).returning(Wishlist)
        )
        return self._get_domain_model_or_none(data=result, model=WishlistModel)

    async def get(self, id_: UUID) -> Optional[WishlistModel]:
        result: Result = await self.session.execute(
            select(Wishlist).where(Wishlist.id == id_)
        )
        return self._get_domain_model_or_none(data=result, model=WishlistModel)

    async def update(self, id_: UUID, data: dict) -> Optional[WishlistModel]:
        result: Result = await self.session.execute(
            update(Wishlist).where(Wishlist.id == id_).values(
                **data
            ).returning(Wishlist)
        )
        return self._get_domain_model_or_none(data=result, model=WishlistModel)

    async def delete(self, id_: UUID) -> bool:
        pass
