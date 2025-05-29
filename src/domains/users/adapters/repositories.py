from uuid import UUID, uuid4
from typing import Optional

from pydantic import EmailStr
from sqlalchemy import Result, insert, select, delete, update
from sqlalchemy.orm import joinedload

from src.core.database.interfaces.repositories import SQLAlchemyAbstractRepository
from src.domains.users.domain.models import UserModel, UserCreateModel, UserRelationshipModel
from src.domains.users.adapters.models import User
from src.domains.users.interfaces.repositories import UsersAbstractRepository


class SQLAlchemyUsersRepository(SQLAlchemyAbstractRepository, UsersAbstractRepository):
    async def add(self, model: UserCreateModel) -> Optional[UserModel]:
        result: Result = await self.session.execute(
            insert(User).values(id=uuid4(), **model.model_dump()).returning(User)
        )
        return self._get_domain_model_or_none(data=result, model=UserModel)

    async def get(self, id_: UUID) -> Optional[UserModel]:
        result: Result = await self.session.execute(
            select(User).where(User.id == id_)
        )
        return self._get_domain_model_or_none(data=result, model=UserModel)

    async def get_by_email(self, email: EmailStr) -> Optional[UserModel]:
        result: Result = await self.session.execute(
            select(User).where(User.email == email)
        )
        return self._get_domain_model_or_none(data=result, model=UserModel)

    async def get_full(self, id_: UUID) -> Optional[UserRelationshipModel]:
        result: Result = await self.session.execute(
            select(User).where(User.id == id_).options(joinedload(User.wishlist), joinedload(User.cart))
        )
        return self._get_domain_model_or_none(data=result, model=UserRelationshipModel)

    async def update(self, id_: UUID, data: dict) -> Optional[UserModel]:
        result: Result = await self.session.execute(
            update(User).where(User.id == id_).values(**data).returning(User)
        )
        return self._get_domain_model_or_none(data=result, model=UserModel)

    async def delete(self, id_: UUID) -> bool:
        result: Result = await self.session.execute(
            delete(User).where(User.id == id_).returning(User.id)
        )
        return True if result.scalar_one_or_none() else False
