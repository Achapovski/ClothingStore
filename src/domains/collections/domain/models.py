from uuid import UUID, uuid4

from pydantic import BaseModel, Field

from src.core.interfaces.models import AbstractModel


class CollectionModel(BaseModel, AbstractModel):
    title: str = Field(min_length=3, max_length=30)
    description: str = Field(default=str())


class CollectionModelDTO(BaseModel):
    title: str = Field(min_length=3, max_length=30)
    description: str = Field(default=str())
