import uuid
from abc import ABC, abstractmethod
from typing import Optional

from src.core.interfaces.models import AbstractModel
from src.core.interfaces.repositories import AbstractRepository


class CollectionsAbstractRepository(AbstractRepository, ABC):
    @abstractmethod
    async def get_by_title(self, title: str) -> Optional[AbstractModel]:
        raise NotImplementedError

    @abstractmethod
    async def get(self, id_: int) -> Optional[AbstractModel]:
        raise NotImplementedError

    @abstractmethod
    async def add(self, model: AbstractModel) -> AbstractModel:
        raise NotImplementedError

    @abstractmethod
    async def update(self, id_: uuid.UUID, extra: dict) -> Optional[AbstractModel]:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, id_: uuid.UUID) -> None:
        raise NotImplementedError
