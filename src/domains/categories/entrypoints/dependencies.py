from typing import Annotated

from fastapi import Depends

from src.domains.categories.services.service import CategoryService
from src.domains.categories.services.units_of_work import SQLAlchemyCategoriesUnitOfWork


async def get_categories_unit_of_work() -> SQLAlchemyCategoriesUnitOfWork:
    return SQLAlchemyCategoriesUnitOfWork()


async def get_category_domain_service(
        uow: Annotated[SQLAlchemyCategoriesUnitOfWork, Depends(get_categories_unit_of_work)]
) -> CategoryService:
    return CategoryService(uow=uow)
