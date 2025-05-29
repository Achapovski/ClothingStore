from uuid import UUID
from typing import Annotated

from fastapi import APIRouter, Depends, status

from src.domains.collections.domain.models import CollectionModel, CollectionModelDTO
from src.domains.collections.services.service import CollectionDomainService

from src.domains.collections.entrypoints.dependencies import get_collection_domain_service

router = APIRouter(prefix="/collections", tags=["Collections"])


@router.post(
    path="/",
    response_model=CollectionModelDTO,
    status_code=status.HTTP_201_CREATED
)
async def create_collection(
        collection: CollectionModelDTO,
        collection_service: Annotated[CollectionDomainService, Depends(get_collection_domain_service)]
) -> CollectionModelDTO:
    collection = await collection_service.create_collection(collection=CollectionModel(**collection.model_dump()))
    return CollectionModelDTO(**collection.model_dump())


@router.get(
    path="/{collection_id}",
    response_model=CollectionModelDTO,
    status_code=status.HTTP_200_OK
)
async def get_collection(
        collection_id: UUID,
        collection_service: Annotated[CollectionDomainService, Depends(get_collection_domain_service)]
) -> CollectionModelDTO:
    collection = await collection_service.get_collection(id_=collection_id)
    return CollectionModelDTO(**collection.model_dump())


@router.delete(
    path="/{collection_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_collection(
        collection_id: UUID,
        collection_service: Annotated[CollectionDomainService, Depends(get_collection_domain_service)]
) -> None:
    await collection_service.delete_collection(id_=collection_id)


@router.patch(
    path="/{collection_id}",
    response_model=CollectionModelDTO,
    status_code=status.HTTP_200_OK
)
async def update_collection(
        collection_id: UUID,
        collection: CollectionModel,
        collection_service: Annotated[CollectionDomainService, Depends(get_collection_domain_service)]
) -> CollectionModelDTO:
    collection = await collection_service.update_collection(id_=collection_id, data=collection)
    return CollectionModelDTO(**collection.model_dump())
