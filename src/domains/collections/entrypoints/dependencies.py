from typing import Annotated

from fastapi import Depends

from src.domains.collections.services.units_of_work import SQLAlchemyCollectionsUnitOfWork
from src.domains.collections.services.service import CollectionDomainService
from src.core.database.interfaces.units_of_work import SQLAlchemyAbstractUnitOfWork


async def get_unit_of_work() -> SQLAlchemyAbstractUnitOfWork:
    return SQLAlchemyCollectionsUnitOfWork()


async def get_collection_domain_service(
        uow: Annotated[SQLAlchemyCollectionsUnitOfWork, Depends(get_unit_of_work)]
) -> CollectionDomainService:
    return CollectionDomainService(uow=uow)
