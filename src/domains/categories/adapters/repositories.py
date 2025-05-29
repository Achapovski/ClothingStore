from typing import Optional
from uuid import UUID, uuid4

from sqlalchemy import insert, Result, select, update, delete
from sqlalchemy.orm import selectinload

from src.domains.categories.adapters.models import Category
from src.domains.categories.interfaces.repositories import CategoriesAbstractRepository
from src.core.database.interfaces.repositories import SQLAlchemyAbstractRepository
from src.domains.categories.domain.models import CategoryModel, CategoryModelDTO, CategoryModelDTORel


class SQLAlchemyCategoriesRepository(CategoriesAbstractRepository, SQLAlchemyAbstractRepository):
    async def add(self, model: CategoryModel) -> Optional[CategoryModelDTO]:
        result: Result = await self.session.execute(
            insert(Category).values(id=uuid4(), **model.model_dump()).returning(Category)
        )
        return self._get_domain_model_or_none(data=result, model=CategoryModelDTO)

    async def get(self, id_: UUID) -> Optional[CategoryModelDTO]:
        result: Result = await self.session.execute(
            select(Category).where(Category.id == id_)
        )
        return self._get_domain_model_or_none(data=result, model=CategoryModelDTO)

    async def get_by_title(self, title: str) -> Optional[CategoryModel]:
        result: Result = await self.session.execute(
            select(Category).where(Category.title == title)
        )
        return self._get_domain_model_or_none(data=result, model=CategoryModel)

    async def get_category_products(self, title: str) -> CategoryModelDTORel:
        result: Result = await self.session.execute(
            select(Category).where(Category.title == title).options(selectinload(Category.products))
        )
        return self._get_domain_model_or_none(data=result, model=CategoryModelDTORel)

    async def update(self, id_: UUID, data: dict) -> Optional[CategoryModelDTO]:
        result: Result = await self.session.execute(
            update(Category).values(**data).where(Category.id == id_).returning(Category)
        )
        return self._get_domain_model_or_none(data=result, model=CategoryModelDTO)

    async def delete(self, id_: UUID) -> bool:
        result: Result = await self.session.execute(
            delete(Category).where(Category.id == id_)
        )
        return True if result.scalar_one_or_none() else False
