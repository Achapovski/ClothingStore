from typing import Type, Optional
from uuid import UUID

from pydantic import BaseModel

from src.domains.carts.domain.models import CartItemModel, CartModel
from src.domains.products.domain.models import ProductModelItemDTO, ProductModel
from src.domains.products.services.service import ProductDomainService
from src.domains.carts.services.service import CartDomainService
from src.app.interfaces.units_of_work import CommonUserUnitOfWork
from src.domains.users.services.service import UserDomainService
from src.domains.users.domain.models import UserRegisterModelDTO, UserModel, UserCreateModel
from src.domains.wishlists.domain.models import WishlistItemsModel, WishlistItemModelDTO, WishlistModel
from src.domains.wishlists.services.service import WishlistService


class UserService:
    def __init__(self, uow: CommonUserUnitOfWork):
        self._uow: CommonUserUnitOfWork = uow
        self.user_service: UserDomainService = UserDomainService(uow=self._uow.users)
        self.cart_service: CartDomainService = CartDomainService(uow=self._uow.carts)
        self.wishlist_service: WishlistService = WishlistService(uow=self._uow.wishlists)
        self.product_service: ProductDomainService = ProductDomainService(uow=self._uow.products)

    async def create_user(self, user: UserRegisterModelDTO) -> UserModel:
        async with self._uow as uow:
            cart = await self.cart_service.create_cart()
            wishlist = await self.wishlist_service.create_wishlist()
            user_model = UserCreateModel(**user.model_dump(), cart_id=cart.id, wishlist_id=wishlist.id)
            user = await self.user_service.create_user(user=user_model)
            await uow.commit()
        return user

    async def get_user_cart(self, user_id: UUID) -> list[CartItemModel]:
        async with self._uow:
            user = await self.user_service.get_user_full_data(id_=user_id)
            products = await self.product_service.get_product_from_ids([item for item in user.cart.items])
            cart = [CartItemModel(item=item, amount=user.cart.items[item.id.__str__()]) for item in products]
        return cart

    async def get_user_wishlist(self, user_id: UUID) -> WishlistItemsModel:
        async with self._uow:
            user = await self.user_service.get_user_full_data(id_=user_id)
            products = await self.product_service.get_product_from_ids([item for item in user.wishlist.items])
            wishlist = WishlistItemsModel(items=[item for item in products])
        return wishlist

    async def add_product_to_cart(self, user_id: UUID, item: ProductModelItemDTO) -> Optional[ProductModel]:
        async with self._uow as uow:
            user = await self.user_service.get_user(id_=user_id)
            await self.cart_service.append_item(cart_id=user.cart_id, item_id=item.product_id, amount=item.amount)
            product = await self.product_service.get_product(id_=item.product_id)
            await uow.commit()
        return product

    async def decrease_product_amount_in_cart(self, user_id: UUID, item: ProductModelItemDTO) -> Optional[CartModel]:
        async with self._uow as uow:
            user = await self.user_service.get_user(id_=user_id)
            cart = await self.cart_service.decrease_item(
                cart_id=user.cart_id, item_id=item.product_id, amount=item.amount
            )
            await uow.commit()
        return cart

    async def add_product_to_wishlist(self, user_id: UUID, item: WishlistItemModelDTO) -> Optional[ProductModel]:
        async with self._uow as uow:
            user = await self.user_service.get_user(id_=user_id)
            await self.wishlist_service.append_item(wishlist_id=user.wishlist_id, item_id=item.item_id)
            product = await self.product_service.get_product(id_=item.item_id)
            await uow.commit()
        return product

    async def remove_product_from_wishlist(self, user_id: UUID, item_id: UUID) -> Optional[WishlistModel]:
        async with self._uow as uow:
            user = await self.user_service.get_user(id_=user_id)
            wishlist = await self.wishlist_service.remove_item(wishlist_id=user.wishlist_id, item_id=item_id)
            await uow.commit()
        return wishlist

    @staticmethod
    def as_model[T: Type[BaseModel]](from_: BaseModel, to_: T) -> Type[T]:
        return to_(**from_.model_dump())
