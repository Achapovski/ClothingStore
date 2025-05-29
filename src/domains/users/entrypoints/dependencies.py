from typing import Annotated

from fastapi import Depends

from src.domains.users.services.units_of_work import SQLAlchemyUsersUnitOfWork
from src.domains.users.services.service import UserDomainService


async def get_users_unit_of_work() -> SQLAlchemyUsersUnitOfWork:
    return SQLAlchemyUsersUnitOfWork()


async def get_domain_user_service(
        uow: Annotated[SQLAlchemyUsersUnitOfWork, Depends(get_users_unit_of_work)]
) -> UserDomainService:
    return UserDomainService(uow=uow)
