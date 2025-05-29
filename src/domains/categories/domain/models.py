from uuid import UUID

from pydantic import BaseModel, Field

from src.core.interfaces.models import AbstractModel
from src.domains.products.domain.models import ProductModel


class CategoryModel(BaseModel, AbstractModel):
    id: UUID
    title: str = Field(min_length=3, max_length=15)


class CategoryCreateModelDTO(CategoryModel):
    pass


class CategoryModelDTO(CategoryModel):
    id: UUID


class CategoryModelDTORel(CategoryModelDTO):
    products: list["ProductModel"]
