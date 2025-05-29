import uuid
from typing import Optional
from uuid import uuid4

from sqlalchemy import Result, select, delete, insert, update

from src.domains.collections.interfaces.repositories import CollectionsAbstractRepository
from src.domains.collections.domain.models import CollectionModel
from src.core.database.interfaces.repositories import SQLAlchemyAbstractRepository
from src.domains.collections.adapters.models import Collection


class CollectionsRepository(SQLAlchemyAbstractRepository, CollectionsAbstractRepository):
    async def add(self, model: CollectionModel) -> Optional[CollectionModel]:
        result: Result = await self.session.execute(
            insert(Collection).values(id=uuid4(), **model.model_dump()).returning(Collection)
        )
        return self._get_domain_model_or_none(data=result, model=CollectionModel)

    async def get(self, id_: uuid.UUID) -> Optional[CollectionModel]:
        result: Result = await self.session.execute(
            select(Collection).where(Collection.id == id_)
        )
        return self._get_domain_model_or_none(data=result, model=CollectionModel)

    async def get_by_title(self, title: str) -> Optional[CollectionModel]:
        result: Result = await self.session.execute(
            select(Collection).where(Collection.title == title)
        )
        return self._get_domain_model_or_none(data=result, model=CollectionModel)

    async def delete(self, id_: uuid.UUID) -> bool:
        result: Result = await self.session.execute(
            delete(Collection).where(Collection.id == id_).returning(Collection.id)
        )
        return True if result.scalar_one_or_none() else False

    async def update(self, id_: uuid.UUID, data: dict) -> Optional[CollectionModel]:
        result: Result = await self.session.execute(
            update(Collection).where(Collection.id == id_).values(**data).returning(Collection)
        )
        return self._get_domain_model_or_none(data=result, model=CollectionModel)
