import uuid
from typing import Optional
from uuid import uuid4, UUID

from sqlalchemy import Result, select, insert, update, delete
from sqlalchemy.orm import joinedload

from src.core.database.interfaces.repositories import SQLAlchemyAbstractRepository
from src.core.interfaces.models import AbstractModel
from src.domains.products.adapters.models import Product
from src.domains.products.domain.models import ProductModel, ProductModelRel
from src.domains.products.interfaces.repositories import ProductsAbstractRepository


class SQLAlchemyProductsRepository(SQLAlchemyAbstractRepository, ProductsAbstractRepository):
    async def add(self, model: ProductModel) -> Optional[ProductModel]:
        result: Result = await self.session.execute(
            insert(Product).values(id=uuid4(), **model.model_dump()).returning(Product)
        )
        return self._get_domain_model_or_none(data=result, model=ProductModel)

    async def get(self, id_: uuid.UUID) -> Optional[ProductModel]:
        result: Result = await self.session.execute(
            select(Product).where(Product.id == id_)
        )
        return self._get_domain_model_or_none(data=result, model=ProductModel)

    async def get_by_title(self, title: str) -> list[ProductModel]:
        result: Result = await self.session.execute(
            select(Product).where(Product.title == title)
        )
        if data := result.scalars().all():
            return [ProductModel.model_validate(obj=obj, from_attributes=True) for obj in data]
        return []

    async def get_by_category(self, category: str) -> list[AbstractModel]:
        result: Result = await self.session.execute(
            select(Product).where(Product.category == category)
        )
        if data := result.scalars().all():
            return [ProductModel.model_validate(obj=obj, from_attributes=True) for obj in data]
        return []

    async def get_by_color(self, color: str) -> list[AbstractModel]:
        result: Result = await self.session.execute(
            select(Product).where(Product.color == color)
        )
        if data := result.scalars().all():
            return [ProductModel.model_validate(obj=obj, from_attributes=True) for obj in data]
        return []

    async def get_by_collection(self, collection: str) -> list[AbstractModel]:
        result: Result = await self.session.execute(
            select(Product).where(Product.collection == collection)
        )
        if data := result.scalars().all():
            return [ProductModel.model_validate(obj=obj, from_attributes=True) for obj in data]
        return []

    async def get_by_material(self, material: str) -> list[AbstractModel]:
        result: Result = await self.session.execute(
            select(Product).where(Product.material == material)
        )
        if data := result.scalars().all():
            return [ProductModel.model_validate(obj=obj, from_attributes=True) for obj in data]
        return []

    async def get_from_ids(self, ids: list[UUID]) -> list[ProductModelRel]:
        result: Result = await self.session.execute(
            select(Product).where(Product.id.in_(ids)).options(joinedload(Product.category))
        )
        if data := result.scalars().all():
            return [ProductModelRel.model_validate(obj=obj, from_attributes=True) for obj in data]
        return []

    async def get_list(self) -> list[ProductModel]:
        result: Result = await self.session.execute(
            select(Product).where(Product.is_active is True)
        )
        if data := result.scalars().all():
            return [ProductModel.model_validate(obj=obj, from_attributes=True) for obj in data]
        return []

    async def update(self, id_: uuid.UUID, data: dict) -> Optional[AbstractModel]:
        result: Result = await self.session.execute(
            update(Product).where(Product.id == id_).values(**data).returning(Product)
        )
        return self._get_domain_model_or_none(data=result, model=ProductModel)

    async def delete(self, id_: uuid.UUID) -> bool:
        result: Result = await self.session.execute(
            delete(Product).where(Product.id == id_).returning(Product.id)
        )
        return True if result.scalar_one_or_none() else False
