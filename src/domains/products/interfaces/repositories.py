from uuid import UUID
from abc import ABC, abstractmethod
from typing import Optional

from src.core.interfaces.repositories import AbstractRepository
from src.domains.products.domain.models import ProductModel


class ProductsAbstractRepository(AbstractRepository, ABC):
    @abstractmethod
    async def get_by_title(self, title: str) -> Optional[ProductModel]:
        raise NotImplementedError

    @abstractmethod
    async def get_by_collection(self, collection: str) -> list[ProductModel]:
        raise NotImplementedError

    @abstractmethod
    async def get_by_material(self, material: str) -> list[ProductModel]:
        raise NotImplementedError

    @abstractmethod
    async def get_by_color(self, color: str) -> list[ProductModel]:
        raise NotImplementedError

    @abstractmethod
    async def get_by_category(self, category: str) -> list[ProductModel]:
        raise NotImplementedError

    @abstractmethod
    async def get_from_ids(self, ids: list[UUID]) -> list[ProductModel]:
        raise NotImplementedError

    @abstractmethod
    async def get(self, id_: UUID) -> Optional[ProductModel]:
        raise NotImplementedError

    @abstractmethod
    async def add(self, model: ProductModel) -> ProductModel:
        raise NotImplementedError

    @abstractmethod
    async def update(self, id_: UUID, data: dict) -> Optional[ProductModel]:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, id_: UUID) -> bool:
        raise NotImplementedError
