from decimal import Decimal
from typing import ForwardRef

from pydantic import BaseModel, Field, AnyHttpUrl, field_serializer, field_validator
from uuid import UUID

from src.core.interfaces.models import AbstractModel


# CategoryModel = ForwardRef("CategoryModel")
# CollectionModel = ForwardRef("CollectionModel")


class ProductModel(BaseModel, AbstractModel):
    id: UUID
    title: str = Field(min_length=3, max_length=35)
    description: str = Field(default="")
    type: str = Field(min_length=3, max_length=20)
    color: str = Field(min_length=3, max_length=20)
    price: Decimal = Field(ge=Decimal("1.0"))
    material: str = Field(min_length=2, max_length=25)
    discount: Decimal = Field(default=Decimal("0.0"))
    image_url: AnyHttpUrl | str = Field()
    category_title: str
    collection_title: str

    @staticmethod
    @field_serializer("image_url")
    def serialize_url(value: AnyHttpUrl | str):
        if isinstance(value, str):
            return AnyHttpUrl(value).unicode_string()
        return value.unicode_string()

    @field_validator("image_url")
    def validate_url(cls, value: AnyHttpUrl | str):
        if isinstance(value, str):
            return AnyHttpUrl(value).unicode_string()
        return value.unicode_string()


class ProductModelDTO(ProductModel):
    pass


class ProductUpdateModelDTO(BaseModel):
    class Config:
        exclude = {"id"}


class ProductCreateModelDTO(ProductModel):
    class Config:
        exclude = {"id"}


class ProductModelItemDTO(BaseModel):
    product_id: UUID
    amount: int = Field(default=1)


class ProductModelViewDTO(BaseModel):
    title: str
    type: str
    color: str
    # amount: int
    image_url: AnyHttpUrl
    collection_title: str
    category_title: str


class ProductModelRel(ProductModel):
    # category: "CategoryModel"
    # collection: "CollectionModel"
    pass
