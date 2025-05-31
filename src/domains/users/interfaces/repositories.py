from uuid import UUID
from abc import ABC, abstractmethod
from typing import Optional

from pydantic import EmailStr

from src.core.interfaces.repositories import AbstractRepository
from src.domains.users.domain.models import UserModel, UserCreateModel, UserRelationshipModel


class UsersAbstractRepository(AbstractRepository, ABC):
    @abstractmethod
    async def get(self, id_: UUID) -> Optional[UserModel]:
        raise NotImplementedError

    @abstractmethod
    async def get_by_email(self, email: EmailStr) -> Optional[UserModel]:
        raise NotImplementedError

    @abstractmethod
    async def get_by_login(self, login: str) -> Optional[UserModel]:
        raise NotImplementedError

    @abstractmethod
    async def get_full(self, id_: UUID) -> UserRelationshipModel:
        raise NotImplementedError

    @abstractmethod
    async def add(self, model: UserCreateModel) -> UserModel:
        raise NotImplementedError

    @abstractmethod
    async def update(self, id_: UUID, data: dict) -> Optional[UserModel]:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, id_: UUID) -> bool:
        raise NotImplementedError
