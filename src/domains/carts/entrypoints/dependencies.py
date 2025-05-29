from typing import Annotated

from fastapi import Depends

from src.domains.carts.services.units_of_work import SQLAlchemyCartsUnitOfWork
from src.domains.carts.services.service import CartDomainService


async def get_carts_unit_of_work() -> SQLAlchemyCartsUnitOfWork:
    return SQLAlchemyCartsUnitOfWork()


async def get_cart_domain_service(
        uow: Annotated[SQLAlchemyCartsUnitOfWork, Depends(get_carts_unit_of_work)]
) -> CartDomainService:
    return CartDomainService(uow=uow)
