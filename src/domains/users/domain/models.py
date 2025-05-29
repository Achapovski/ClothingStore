from datetime import datetime
from decimal import Decimal
from uuid import UUID
from typing import ForwardRef

from pydantic import Field, EmailStr, BaseModel, SecretStr, field_serializer

from src.core.interfaces.models import AbstractModel
from src.domains.products.domain.models import ProductModel

# from src.domains.wishlists.domain.models import WishlistModelDTO, WishlistModel

CartModel = ForwardRef("CartModel")
WishlistModel = ForwardRef("WishlistModel")


class UserModel(BaseModel, AbstractModel):
    id: UUID
    login: str
    username: str
    password: SecretStr
    email: EmailStr
    phone_number: str | None
    personal_discount: Decimal
    status: str
    signup_date: datetime
    location: str | None
    cart_id: UUID
    wishlist_id: UUID


class UserUpdateModel(BaseModel, AbstractModel):
    login: str | None = None
    username: str | None = None
    email: EmailStr | None = None
    location: str | None = None
    phone_number: str | None = None


class UserRelationshipModel(BaseModel, AbstractModel):
    id: UUID
    username: str
    cart: CartModel
    wishlist: WishlistModel


class UserRegisterModelDTO(BaseModel):
    login: str = Field(default="Anonymous")
    username: str
    password: SecretStr
    email: EmailStr

    @field_serializer("password")
    def password_serializer(self, value: SecretStr):
        return value.get_secret_value()


class UserCreateModel(UserRegisterModelDTO):
    cart_id: UUID
    wishlist_id: UUID


class UserLoginModelDTO(BaseModel):
    login: str
    password: SecretStr


class UserProfileDTO(BaseModel):
    id: UUID
    username: str
    login: str
    email: str
    phone_number: str | None
    location: str | None
    personal_discount: Decimal
    status: str
    signup_date: datetime


class UserCartDTO(BaseModel):
    items: list[ProductModel]


class UserUpdateDTO(UserUpdateModel):
    pass


class UserWishlistDTO(UserCartDTO):
    pass


# class UserModelDTO(BaseModel):
#     id: UUID
#     login: str
#     email: EmailStr
#     cart: list[ProductModel] = Field()
#     wishlist: list[ProductModel] = Field()


class UserModelRel(UserModel):
    cart: UserCartDTO
    wishlist: UserWishlistDTO
