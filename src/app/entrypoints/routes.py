from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from src.app.entrypoints.dependencies import get_user_service, get_auth_service
from src.app.services.user_service import UserService
from src.core.security.config import base_auth_config
from src.domains.carts.domain.models import CartModelDTO, CartModel
from src.domains.products.domain.models import ProductModelItemDTO, ProductModelViewDTO
from src.domains.users.domain.models import UserRegisterModelDTO, UserProfileDTO
from src.domains.users.entrypoints.dependencies import get_domain_user_service
from src.domains.users.services.service import UserDomainService
from src.domains.wishlists.domain.models import WishlistModelDTO, WishlistItemModelDTO
from src.infrastrucure.auth.service import AuthService

router = APIRouter(prefix="/users", tags=["Users"])


@router.get(
    path="/",
    response_model=UserProfileDTO,
    status_code=status.HTTP_200_OK
)
async def get_user(
        user_service: Annotated[UserDomainService, Depends(get_domain_user_service)],
        auth_service: Annotated[AuthService, Depends(get_auth_service)],
        token: Annotated[str, Depends(base_auth_config.oauth2_password)],
) -> UserProfileDTO:
    jwt_data = await auth_service.get_jwt_data(token=token)
    if jwt_data:
        user = await user_service.get_user(id_=jwt_data.user_id)
        return UserProfileDTO(**user.model_dump())
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@router.post(
    path="/",
    response_model=UserProfileDTO,
    status_code=status.HTTP_201_CREATED
)
async def create_user(
        user: UserRegisterModelDTO,
        user_service: Annotated[UserService, Depends(get_user_service)]
) -> UserProfileDTO:
    user = await user_service.create_user(user=user)
    return user_service.as_model(from_=user, to_=UserProfileDTO)


@router.get(
    path="/cart",
    response_model=CartModelDTO,
    status_code=status.HTTP_200_OK
)
async def get_user_cart(
        user_service: Annotated[UserService, Depends(get_user_service)],
        auth_service: Annotated[AuthService, Depends(get_auth_service)],
        token: Annotated[str, Depends(base_auth_config.oauth2_password)],
) -> CartModelDTO:
    jwt_data = await auth_service.get_jwt_data(token=token)
    if jwt_data:
        user_cart = await user_service.get_user_cart(user_id=jwt_data.user_id)
        return CartModelDTO(items=user_cart)
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@router.post(
    path="/cart/items",
    response_model=ProductModelViewDTO,
    status_code=status.HTTP_201_CREATED
)
async def add_product_to_cart(
        product: ProductModelItemDTO,
        user_service: Annotated[UserService, Depends(get_user_service)],
        auth_service: Annotated[AuthService, Depends(get_auth_service)],
        token: Annotated[str, Depends(base_auth_config.oauth2_password)],
) -> ProductModelViewDTO:
    jwt_data = await auth_service.get_jwt_data(token=token)
    if jwt_data:
        product = await user_service.add_product_to_cart(user_id=jwt_data.user_id, item=product)
        return ProductModelViewDTO(**product.model_dump())
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@router.patch(
    path="/cart/items",
    response_model=CartModel,
    status_code=status.HTTP_200_OK
)
async def decrease_product_amount_in_cart(
        product: ProductModelItemDTO,
        user_service: Annotated[UserService, Depends(get_user_service)],
        auth_service: Annotated[AuthService, Depends(get_auth_service)],
        token: Annotated[str, Depends(base_auth_config.oauth2_password)],
) -> CartModel:
    # TODO: Вернуть продукт
    jwt_data = await auth_service.get_jwt_data(token=token)
    if jwt_data:
        return await user_service.decrease_product_amount_in_cart(user_id=jwt_data.user_id, item=product)


@router.get(
    path="/wishlist",
    response_model=WishlistModelDTO,
    status_code=status.HTTP_200_OK
)
async def get_user_wishlist(
        user_service: Annotated[UserService, Depends(get_user_service)],
        auth_service: Annotated[AuthService, Depends(get_auth_service)],
        token: Annotated[str, Depends(base_auth_config.oauth2_password)],
) -> WishlistModelDTO:
    jwt_data = await auth_service.get_jwt_data(token=token)
    if jwt_data:
        wishlist = await user_service.get_user_wishlist(user_id=jwt_data.user_id)
        return WishlistModelDTO(**wishlist.model_dump())
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@router.post(
    path="/wishlist/items",
    response_model=ProductModelViewDTO,
    status_code=status.HTTP_201_CREATED
)
async def add_product_to_wishlist(
        product: WishlistItemModelDTO,
        user_service: Annotated[UserService, Depends(get_user_service)],
        auth_service: Annotated[AuthService, Depends(get_auth_service)],
        token: Annotated[str, Depends(base_auth_config.oauth2_password)],
) -> ProductModelViewDTO:
    jwt_data = await auth_service.get_jwt_data(token=token)
    if jwt_data:
        product = await user_service.add_product_to_wishlist(user_id=jwt_data.user_id, item=product)
        return ProductModelViewDTO(**product.model_dump())
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@router.delete(
    path="/wishlist/items/{item_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def remove_product_from_wishlist(
        item_id: UUID,
        user_service: Annotated[UserService, Depends(get_user_service)],
        auth_service: Annotated[AuthService, Depends(get_auth_service)],
        token: Annotated[str, Depends(base_auth_config.oauth2_password)]
):
    jwt_data = await auth_service.get_jwt_data(token=token)
    if jwt_data:
        await user_service.remove_product_from_wishlist(user_id=jwt_data.user_id, item_id=item_id)
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@router.post(
    path="/login",
    tags=["auth"]
)
async def login_user(
        auth_service: Annotated[AuthService, Depends(get_auth_service)],
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
):
    jwt_token = await auth_service.login(user_login=form_data.username, password=form_data.password)
    return {"access_token": jwt_token, "token_type": "bearer"}
