from abc import ABC

from src.core.interfaces.units_of_work import AbstractUnitOfWork
from src.domains.categories.adapters.repositories import SQLAlchemyCategoriesRepository


class CategoriesUnitOfWork(AbstractUnitOfWork, ABC):
    categories: SQLAlchemyCategoriesRepository
