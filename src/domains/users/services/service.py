from uuid import UUID

from pydantic import EmailStr

from src.domains.users.domain.models import UserModel, UserCreateModel, UserUpdateModel, UserRelationshipModel
from src.domains.users.interfaces.units_of_work import UsersUnitOfWork


class UserDomainService:
    def __init__(self, uow: UsersUnitOfWork):
        self._uow: UsersUnitOfWork = uow

    async def create_user(self, user: UserCreateModel) -> UserModel:
        async with self._uow as uow:
            user = await uow.users.add(model=user)
        return user

    async def get_user(self, id_: UUID) -> UserModel:
        async with self._uow as uow:
            user = await uow.users.get(id_=id_)
        return user

    async def get_user_by_email(self, email: EmailStr) -> UserModel:
        async with self._uow as uow:
            user = await uow.users.get_by_email(email=email)
            return user

    async def get_user_full_data(self, id_: UUID) -> UserRelationshipModel:
        async with self._uow as uow:
            user = await uow.users.get_full(id_=id_)
            return user

    async def update_user(self, id_: UUID, data: UserUpdateModel) -> UserModel:
        async with self._uow as uow:
            user = await uow.users.update(id_=id_, data=data.model_dump())
            return user

    async def delete_user(self, id_: UUID) -> bool:
        async with self._uow as uow:
            result: bool = await uow.users.delete(id_=id_)
            return result
