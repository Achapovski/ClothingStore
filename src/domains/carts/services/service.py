from typing import Any, Optional
from uuid import UUID

from src.domains.carts.domain.models import CartModel, CartCreateModel
from src.domains.carts.interfaces.units_of_work import CartsUnitOfWork


class CartDomainService:
    def __init__(self, uow: CartsUnitOfWork):
        self._uow: CartsUnitOfWork = uow

    async def create_cart(self) -> CartModel:
        async with self._uow as uow:
            cart = await uow.carts.add(model=CartCreateModel())
        return cart

    async def append_item(self, cart_id: UUID, item_id: UUID, amount: int = 1) -> Optional[CartModel]:
        async with self._uow as uow:
            cart = await uow.carts.get(id_=cart_id)
            updated_cart = self._add_or_update_item(cart=cart, item_id=str(item_id), value=amount)
            result_cart = await uow.carts.update(id_=cart_id, data=updated_cart.model_dump())
        return result_cart

    async def decrease_item(self, cart_id: UUID, item_id: UUID, amount: int = 1) -> Optional[CartModel]:
        return await self.append_item(cart_id=cart_id, item_id=item_id, amount=-amount)

    async def get_cart(self, id_: UUID) -> Optional[CartModel]:
        async with self._uow as uow:
            cart = await uow.carts.get(id_=id_)
        return cart

    @staticmethod
    def _is_item_in_cart(cart: dict, item_id: str) -> bool:
        if cart.items and cart.get(item_id):
            return True
        return False

    def _add_or_update_item(self, cart: CartModel, item_id: str, value: Any) -> CartModel:
        has_item = self._is_item_in_cart(cart=cart.items, item_id=item_id)
        cart.items[item_id] = (cart.items[item_id] + value) if has_item else value
        return CartModel(**cart.model_dump())
