from typing import Annotated

from fastapi import Depends

from src.domains.products.interfaces.units_of_work import ProductUnitOfWork
from src.domains.products.services.service import ProductDomainService
from src.domains.products.services.units_of_work import SQLAlchemyProductsUnitOfWork


async def get_product_unit_of_work() -> ProductUnitOfWork:
    return SQLAlchemyProductsUnitOfWork()


async def get_product_service(
        uow: Annotated[ProductUnitOfWork, Depends(get_product_unit_of_work)]
) -> ProductDomainService:
    products_service = ProductDomainService(uow=uow)
    return products_service
