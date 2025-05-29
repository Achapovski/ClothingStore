import uuid
from abc import abstractmethod, ABC
from typing import Optional
from uuid import UUID

from src.core.interfaces.models import AbstractModel
from src.core.interfaces.repositories import AbstractRepository


class CategoriesAbstractRepository(AbstractRepository, ABC):
    @abstractmethod
    async def add(self, model: AbstractModel) -> AbstractModel:
        pass

    @abstractmethod
    async def get(self, id_: UUID) -> Optional[AbstractModel]:
        pass

    @abstractmethod
    async def update(self, id_: uuid.UUID, data: dict) -> Optional[AbstractModel]:
        pass

    @abstractmethod
    async def delete(self, id_: uuid.UUID) -> bool:
        pass
