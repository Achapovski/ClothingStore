from uuid import UUID
from abc import abstractmethod, ABC
from typing import Optional

from src.domains.carts.domain.models import CartModel, CartCreateModel
from src.core.interfaces.repositories import AbstractRepository


class CartsAbstractRepository(AbstractRepository, ABC):
    @abstractmethod
    async def add(self, model: CartCreateModel) -> CartModel:
        raise NotImplementedError

    @abstractmethod
    async def get(self, id_: UUID) -> Optional[CartModel]:
        raise NotImplementedError

    @abstractmethod
    async def update(self, id_: UUID, data: dict) -> Optional[CartModel]:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, id_: UUID) -> bool:
        raise NotImplementedError
