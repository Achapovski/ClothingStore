from abc import ABC

from src.domains.carts.interfaces.units_of_work import CartsUnitOfWork
from src.core.interfaces.units_of_work import AbstractUnitOfWork
from src.domains.products.interfaces.units_of_work import ProductUnitOfWork
from src.domains.users.interfaces.units_of_work import UsersUnitOfWork
from src.domains.wishlists.interfaces.units_of_work import WishlistsUnitOfWork


class CommonUserUnitOfWork(AbstractUnitOfWork, ABC):
    users: UsersUnitOfWork
    carts: CartsUnitOfWork
    wishlists: WishlistsUnitOfWork
    products: ProductUnitOfWork
