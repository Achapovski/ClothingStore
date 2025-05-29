import uuid
from typing import Optional

from src.domains.collections.domain.models import CollectionModel
from src.domains.collections.interfaces.units_of_work import CollectionsUnitOfWork


class CollectionDomainService:
    def __init__(self, uow: CollectionsUnitOfWork):
        self._uow: CollectionsUnitOfWork = uow

    async def create_collection(self, collection: CollectionModel) -> Optional[CollectionModel]:
        async with self._uow as uow:
            collection = await uow.collections.add(model=collection)
        return collection

    async def get_collection(self, id_: uuid.UUID) -> Optional[CollectionModel]:
        async with self._uow as uow:
            collection = await uow.collections.get(id_=id_)
        return collection

    async def get_collection_by_title(self, title: str) -> Optional[CollectionModel]:
        async with self._uow as uow:
            collection = await uow.collections.get_by_title(title=title)
        return collection

    async def update_collection(self, id_: uuid.UUID, data: CollectionModel) -> Optional[CollectionModel]:
        async with self._uow as uow:
            collection = await uow.collections.update(id_=id_, data=data.model_dump())
        return collection

    async def delete_collection(self, id_: uuid.UUID) -> bool:
        async with self._uow as uow:
            result = await uow.collections.delete(id_=id_)
        return result
