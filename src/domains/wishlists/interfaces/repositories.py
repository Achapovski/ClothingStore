from uuid import UUID
from abc import ABC, abstractmethod
from typing import Optional

from src.core.interfaces.repositories import AbstractRepository
from src.domains.wishlists.domain.models import WishlistModel, WishlistModelDTO, WishlistCreateModel


class WishlistsAbstractRepository(AbstractRepository, ABC):
    @abstractmethod
    async def add(self, model: WishlistCreateModel) -> WishlistModel:
        raise NotImplementedError

    @abstractmethod
    async def get(self, id_: UUID) -> Optional[WishlistModel]:
        raise NotImplementedError

    @abstractmethod
    async def update(self, id_: UUID, data: dict) -> Optional[WishlistModel]:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, id_: UUID) -> bool:
        raise NotImplementedError
