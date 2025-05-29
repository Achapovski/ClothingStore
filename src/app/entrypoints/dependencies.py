from typing import Annotated
from fastapi import Depends

from src.app.interfaces.units_of_work import CommonUserUnitOfWork
from src.app.services.units_of_work import SQLAlchemyCommonUnitOfWork
from src.app.services.user_service import UserService


async def get_unit_of_work() -> CommonUserUnitOfWork:
    return SQLAlchemyCommonUnitOfWork(auto_commit=False)


async def get_user_service(
        uow: Annotated[CommonUserUnitOfWork, Depends(get_unit_of_work)],
) -> UserService:
    return UserService(uow=uow)
