from typing import Optional
from uuid import UUID

from src.domains.categories.interfaces.units_of_work import CategoriesUnitOfWork
from src.domains.categories.domain.models import CategoryModel, CategoryModelDTO, CategoryModelDTORel


class CategoryService:
    def __init__(self, uow: CategoriesUnitOfWork):
        self._uow: CategoriesUnitOfWork = uow

    async def create_category(self, model: CategoryModel) -> Optional[CategoryModelDTO]:
        async with self._uow as uow:
            category = await uow.categories.add(model=model)
            return category

    async def get_category(self, id_: UUID) -> Optional[CategoryModelDTO]:
        async with self._uow as uow:
            category = await uow.categories.get(id_=id_)
            return category

    async def get_category_by_title(self, title: str) -> Optional[CategoryModel]:
        async with self._uow as uow:
            category = await uow.categories.get_by_title(title=title)
        return category

    async def get_category_products(self, title: str) -> Optional[CategoryModelDTORel]:
        async with self._uow as uow:
            category_products = await uow.categories.get_category_products(title=title)
            return category_products

    async def update_category(self, id_: UUID, model: CategoryModel) -> Optional[CategoryModelDTO]:
        async with self._uow as uow:
            category = await uow.categories.update(id_=id_, data=model.model_dump())
            return category

    async def delete_category(self, id_: UUID) -> bool:
        async with self._uow as uow:
            result = await uow.categories.delete(id_=id_)
            return result
