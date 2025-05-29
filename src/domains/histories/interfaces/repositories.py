from abc import ABC, abstractmethod
from typing import Optional

from core.interfaces.models import AbstractModel
from core.interfaces.repositories import AbstractRepository


class OrdersHistoriesAbstractRepository(AbstractRepository, ABC):
    @abstractmethod
    async def get_history(self, user_id: int) -> list[AbstractModel]:
        raise NotImplementedError

    @abstractmethod
    async def add(self, model: AbstractModel) -> AbstractModel:
        raise NotImplementedError

    @abstractmethod
    async def get(self, id_: int) -> Optional[AbstractModel]:
        raise NotImplementedError

    @abstractmethod
    async def update(self) -> Optional[AbstractModel]:
        raise NotImplementedError

    @abstractmethod
    async def delete(self) -> None:
        raise NotImplementedError
