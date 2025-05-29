from typing import Any, Optional
from uuid import UUID

from src.domains.wishlists.interfaces.units_of_work import WishlistsUnitOfWork
from src.domains.wishlists.domain.models import WishlistModelDTO, WishlistModel, WishlistCreateModel


class WishlistService:
    def __init__(self, uow: WishlistsUnitOfWork):
        self._uow: WishlistsUnitOfWork = uow

    async def create_wishlist(self) -> WishlistModel:
        async with self._uow as uow:
            wishlist = await uow.wishlist.add(model=WishlistCreateModel())
        return wishlist

    async def append_item_with_count(self, wishlist_id: UUID, item_id: UUID, count: int = 1) -> Optional[WishlistModel]:
        async with self._uow as uow:
            wishlist = await uow.wishlist.get(id_=wishlist_id)
            updated_wishlist = self._add_or_update_item(wishlist=wishlist, item_id=str(item_id), value=+count)
            result_wishlist = await uow.wishlist.update(id_=wishlist_id, data=updated_wishlist.model_dump())
        return result_wishlist

    async def decrease_item_with_count(self, wishlist_id: UUID, item_id: UUID, count: int = 1) -> Optional[WishlistModel]:
        return await self.append_item_with_count(wishlist_id=wishlist_id, item_id=item_id, count=-count)

    async def append_item(self, wishlist_id: UUID, item_id: UUID) -> Optional[WishlistModel]:
        async with self._uow as uow:
            wishlist = await uow.wishlist.get(id_=wishlist_id)
            if not self._is_item_in_wishlist(wishlist=wishlist.items, item_id=item_id.__str__()):
                wishlist.items.update({f"{item_id}": 1})
                await uow.wishlist.update(id_=wishlist_id, data=wishlist.model_dump())
        return wishlist

    async def remove_item(self, wishlist_id: UUID, item_id: UUID) -> Optional[WishlistModel]:
        async with self._uow as uow:
            wishlist = await uow.wishlist.get(id_=wishlist_id)
            if self._is_item_in_wishlist(wishlist=wishlist.items, item_id=item_id.__str__()):
                print(wishlist)
                wishlist.items.pop(item_id.__str__())
                print(wishlist)
                await uow.wishlist.update(id_=wishlist_id, data=wishlist.model_dump())
        return wishlist

    async def get_wishlist(self, id_: UUID) -> Optional[WishlistModelDTO]:
        async with self._uow as uow:
            wishlist = await uow.wishlist.get(id_=id_)
        return wishlist

    @staticmethod
    def _is_item_in_wishlist(wishlist: dict, item_id: str) -> bool:
        if wishlist.items and wishlist.get(item_id):
            return True
        return False

    def _add_or_update_item(self, wishlist: WishlistModel, item_id: str, value: Any) -> WishlistModel:
        has_item = self._is_item_in_wishlist(wishlist=wishlist.items, item_id=item_id)
        wishlist.items[item_id] = (wishlist.items[item_id] + value) if has_item else value
        return wishlist
