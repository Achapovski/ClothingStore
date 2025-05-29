from typing import Annotated, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, status

from src.domains.categories.domain.models import CategoryModelDTO, CategoryModelDTORel, \
    CategoryCreateModelDTO
from src.domains.categories.entrypoints.dependencies import get_category_domain_service
from src.domains.categories.services.service import CategoryService

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post(
    path="/",
    response_model=CategoryModelDTO,
    status_code=status.HTTP_201_CREATED
)
async def create_category(
        category: CategoryCreateModelDTO,
        category_service: Annotated[CategoryService, Depends(get_category_domain_service)]
) -> CategoryModelDTO:
    category = await category_service.create_category(model=category)
    return category


# @router.get(
#     path="/{category_title}",
#     response_model=CategoryModelDTO,
#     status_code=status.HTTP_200_OK
# )
async def get_category_by_title(
        category_title: str,
        category_service: Annotated[CategoryService, Depends(get_category_domain_service)]
) -> CategoryModelDTO:
    category = await category_service.get_category_by_title(title=category_title)
    return CategoryModelDTO(**category.model_dump())


@router.get(
    path="/{category_id}",
    response_model=CategoryModelDTO,
    status_code=status.HTTP_200_OK
)
async def get_category(
        category_id: UUID,
        category_service: Annotated[CategoryService, Depends(get_category_domain_service)]
) -> CategoryModelDTO:
    category = await category_service.get_category(id_=category_id)
    return category


@router.get(
    path="{category_title}/products",
    response_model=CategoryModelDTORel,
    status_code=status.HTTP_200_OK
)
async def get_category_products(
        title: str,
        category_service: Annotated[CategoryService, Depends(get_category_domain_service)]
) -> Optional[CategoryModelDTORel]:
    products = await category_service.get_category_products(title=title)
    return products


@router.patch(
    path="/{category_id}",
    response_model=CategoryModelDTO,
    status_code=status.HTTP_200_OK
)
async def update_category(
        category_id: UUID,
        category: CategoryModelDTO,
        category_service: Annotated[CategoryService, Depends(get_category_domain_service)]
) -> CategoryModelDTO:
    category = await category_service.update_category(id_=category_id, model=category)
    return category


@router.delete(
    path="/{category_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_collection(
        category_id: UUID,
        category_service: Annotated[CategoryService, Depends(get_category_domain_service)]
) -> None:
    await category_service.delete_category(id_=category_id)
