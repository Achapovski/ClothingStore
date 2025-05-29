from uuid import UUID
from typing import Annotated

from fastapi import APIRouter, Depends, status

from src.domains.products.entrypoints.dependencies import get_product_service
from src.domains.products.domain.models import ProductModel, ProductModelDTO, ProductCreateModelDTO, \
    ProductUpdateModelDTO
from src.domains.products.services.service import ProductDomainService

router = APIRouter(prefix="/products", tags=["Products"])


@router.post(
    path="/",
    response_model=ProductModelDTO,
    status_code=status.HTTP_201_CREATED
)
async def create_product(
        product: ProductCreateModelDTO,
        product_service: Annotated[ProductDomainService, Depends(get_product_service)]
) -> ProductModelDTO:
    product = await product_service.create_product(product=product)
    return ProductModelDTO(**product.model_dump())


@router.get(
    path="/{product_id}",
    response_model=ProductModelDTO,
    status_code=status.HTTP_200_OK
)
async def get_product(
        product_id: UUID,
        product_service: Annotated[ProductDomainService, Depends(get_product_service)]
) -> ProductModelDTO:
    product = await product_service.get_product(id_=product_id)
    return ProductModelDTO(**product.model_dump())


@router.patch(
    path="/{product_id}",
    response_model=ProductUpdateModelDTO,
    status_code=status.HTTP_200_OK
)
async def update_user(
        product_id: UUID,
        product: ProductUpdateModelDTO,
        product_service: Annotated[ProductDomainService, Depends(get_product_service)]
) -> ProductModelDTO:
    product = await product_service.update_product(id_=product_id, product=ProductModel(**product.model_dump()))
    return ProductModelDTO(**product.model_dump())


@router.delete(
    path="/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_product(
        product_id: UUID,
        product_service: Annotated[ProductDomainService, Depends(get_product_service)]
) -> None:
    await product_service.delete_product(id_=product_id)
