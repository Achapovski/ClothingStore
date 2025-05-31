from datetime import datetime
from decimal import Decimal
from uuid import UUID
from typing import ForwardRef

from pydantic import Field, EmailStr, BaseModel

from src.core.interfaces.models import AbstractModel
from src.domains.products.domain.models import ProductModel

CartModel = ForwardRef("CartModel")
WishlistModel = ForwardRef("WishlistModel")


class UserModel(BaseModel, AbstractModel):
    id: UUID
    login: str
    username: str
    password: str
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
    password: str
    email: EmailStr


class UserCreateModel(UserRegisterModelDTO):
    cart_id: UUID
    wishlist_id: UUID


class UserLoginModelDTO(BaseModel):
    login: str
    password: str


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


class UserModelRel(UserModel):
    cart: UserCartDTO
    wishlist: UserWishlistDTO
