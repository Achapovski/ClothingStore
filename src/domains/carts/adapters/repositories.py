from uuid import uuid4, UUID
from typing import Optional

from sqlalchemy import insert, Result, select, update

from src.domains.carts.domain.models import CartModel, CartCreateModel
from src.domains.carts.interfaces.repositories import CartsAbstractRepository
from src.core.database.interfaces.repositories import SQLAlchemyAbstractRepository
from src.domains.carts.adapters.models import Cart


class SQLAlchemyCartsRepository(SQLAlchemyAbstractRepository, CartsAbstractRepository):
    async def add(self, model: CartCreateModel) -> Optional[CartModel]:
        result: Result = await self.session.execute(
            insert(Cart).values(id=uuid4(), **model.model_dump()).returning(Cart)
        )
        return self._get_domain_model_or_none(data=result, model=CartModel)

    async def get(self, id_: UUID) -> Optional[CartModel]:
        result: Result = await self.session.execute(
            select(Cart).where(Cart.id == id_)
        )
        return self._get_domain_model_or_none(data=result, model=CartModel)

    async def update(self, id_: UUID, data: dict) -> Optional[CartModel]:
        result: Result = await self.session.execute(
            update(Cart).where(Cart.id == id_).values(
                **data
            ).returning(Cart)
        )
        return self._get_domain_model_or_none(data=result, model=CartModel)

    async def delete(self, id_: UUID) -> None:
        pass
