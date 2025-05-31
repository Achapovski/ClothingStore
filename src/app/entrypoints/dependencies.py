from typing import Annotated
from fastapi import Depends

from src.app.interfaces.units_of_work import CommonUserUnitOfWork
from src.app.services.units_of_work import SQLAlchemyCommonUnitOfWork
from src.app.services.user_service import UserService
from src.core.security.config import jwt_config, base_auth_config
from src.domains.users.entrypoints.dependencies import get_domain_user_service
from src.domains.users.services.service import UserDomainService
from src.infrastrucure.auth.service import AuthService


async def get_unit_of_work() -> CommonUserUnitOfWork:
    return SQLAlchemyCommonUnitOfWork(auto_commit=False)


async def get_user_service(
        uow: Annotated[CommonUserUnitOfWork, Depends(get_unit_of_work)],
) -> UserService:
    return UserService(uow=uow)


async def get_auth_service(
        user_service: Annotated[UserDomainService, Depends(get_domain_user_service)]
) -> AuthService:
    return AuthService(user_service=user_service, jwt_config=jwt_config, auth_config=base_auth_config)
