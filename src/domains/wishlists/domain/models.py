import json
from typing import Union, ForwardRef
from uuid import UUID

from pydantic import BaseModel, Field, field_serializer, field_validator

from src.core.interfaces.models import AbstractModel
from src.domains.products.domain.models import ProductModel, ProductModelItemDTO


class WishlistModel(BaseModel, AbstractModel):
    id: UUID
    items: Union[dict[UUID | str, int], dict] = Field(
        default_factory=dict, examples=[{"686fc140-855c-441e-874f-55faf409565c": 1}]
    )

    @field_serializer("items")
    def uuid_serializer(self, value: UUID):
        return str(value)

    @field_validator("items", mode="before")
    def items_validator(cls, data: Union[dict[UUID, int], dict]):
        # TODO: Можно подумать о вынесении json десериализатора в AbstractModel
        if isinstance(data, str):
            data = json.loads(data.replace("'", "\""))

        for key, value in data.items():
            UUID(str(key), version=4)
            if 0 <= value < 100:
                continue
            raise ValueError("The value cannot be less than 0 or more than 99")
        return data


class WishlistCreateModel(BaseModel):
    items: Union[dict[UUID | str, int], dict] = Field(
        default_factory=dict, examples=[{"686fc140-855c-441e-874f-55faf409565c": 1}]
    )


class WishlistItemsModel(BaseModel):
    items: list[ProductModel]


class WishlistItemModelDTO(BaseModel):
    item_id: UUID


class WishlistModelDTO(BaseModel):
    items: list[ProductModel] | list


class WishlistModelDTORel(WishlistModelDTO):
    # user: ForwardRef("UserModel")
    pass
