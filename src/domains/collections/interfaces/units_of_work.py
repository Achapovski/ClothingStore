from abc import ABC

from src.core.interfaces.units_of_work import AbstractUnitOfWork
from src.domains.collections.adapters.repositories import CollectionsRepository


class CollectionsUnitOfWork(AbstractUnitOfWork, ABC):
    collections: CollectionsRepository
