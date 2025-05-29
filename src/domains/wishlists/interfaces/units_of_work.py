from abc import ABC

from src.core.interfaces.units_of_work import AbstractUnitOfWork
from src.domains.wishlists.interfaces.repositories import WishlistsAbstractRepository


class WishlistsUnitOfWork(AbstractUnitOfWork, ABC):
    wishlist: WishlistsAbstractRepository
