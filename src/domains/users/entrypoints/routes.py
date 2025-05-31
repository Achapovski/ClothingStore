from uuid import UUID
from typing import Annotated

from fastapi import APIRouter, Depends, status

from src.domains.users.entrypoints.dependencies import get_domain_user_service
from src.domains.users.services.service import UserDomainService
from src.domains.users.domain.models import UserModel, UserCreateModel, UserProfileDTO, UserUpdateModel, UserUpdateDTO, \
    UserCartDTO

router = APIRouter(prefix="/users", tags=["Users"])


# TODO: Адаптировать преобразование модели в DTO (Можно попробовать запихнуть это в абстрактную предметную модель)

# @router.get(
#     path="/{user_id}",
#     response_model=UserProfileDTO,
#     status_code=status.HTTP_200_OK
# )
# async def get_user(
#         user_id: UUID,
#         user_service: Annotated[UserDomainService, Depends(get_domain_user_service)]
# ) -> UserProfileDTO:
#     user = await user_service.get_user(id_=user_id)
#     return UserProfileDTO(**user.model_dump())


@router.delete(
    path="/{user_id}",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_user(
        user_id: UUID,
        user_service: Annotated[UserDomainService, Depends(get_domain_user_service)]
):
    await user_service.delete_user(id_=user_id)


@router.patch(
    path="/{user_id}",
    response_model=UserUpdateDTO,
    status_code=status.HTTP_200_OK
)
async def update_user(
        user_id: UUID,
        data: UserUpdateDTO,
        user_service: Annotated[UserDomainService, Depends(get_domain_user_service)]
):
    user = await user_service.update_user(id_=user_id, data=UserUpdateModel(**data.model_dump()))
    return UserUpdateDTO(**user.model_dump())
