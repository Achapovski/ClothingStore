from abc import ABC

from src.core.interfaces.units_of_work import AbstractUnitOfWork
from src.domains.users.interfaces.repositories import UsersAbstractRepository


class UsersUnitOfWork(AbstractUnitOfWork, ABC):
    users: UsersAbstractRepository
