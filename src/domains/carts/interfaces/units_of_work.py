from abc import ABC

from src.core.interfaces.units_of_work import AbstractUnitOfWork
from src.domains.carts.interfaces.repositories import CartsAbstractRepository


class CartsUnitOfWork(AbstractUnitOfWork, ABC):
    carts: CartsAbstractRepository
