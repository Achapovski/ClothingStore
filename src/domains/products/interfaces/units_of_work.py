from abc import ABC

from src.core.interfaces.units_of_work import AbstractUnitOfWork
from src.domains.products.adapters.repositories import SQLAlchemyProductsRepository


class ProductUnitOfWork(AbstractUnitOfWork, ABC):
    products: SQLAlchemyProductsRepository
