from typing import Optional
from uuid import UUID

from src.domains.products.domain.models import ProductModel
from src.domains.products.interfaces.units_of_work import ProductUnitOfWork


class ProductDomainService:
    def __init__(self, uow: ProductUnitOfWork):
        self._uow: ProductUnitOfWork = uow

    async def create_product(self, product: ProductModel) -> Optional[ProductModel]:
        async with self._uow as uow:
            product = await uow.products.add(model=product)
            return product

    async def update_product(self, id_: UUID, product: ProductModel) -> Optional[ProductModel]:
        async with self._uow as uow:
            product = await uow.products.update(id_=id_, data=product.model_dump())
            return product

    async def get_product(self, id_: UUID) -> Optional[ProductModel]:
        async with self._uow as uow:
            product = await uow.products.get(id_=id_)
            return product
        
    async def get_product_from_ids(self, ids: list[UUID]) -> Optional[list[ProductModel]]:
        async with self._uow as uow: 
            products = await uow.products.get_from_ids(ids=ids)
            return products

    async def delete_product(self, id_: UUID) -> bool:
        async with self._uow as uow:
            result = await uow.products.delete(id_=id_)
            return result
