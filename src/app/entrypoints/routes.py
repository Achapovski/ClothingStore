from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, status

from src.app.entrypoints.dependencies import get_user_service
from src.app.services.user_service import UserService
from src.domains.carts.domain.models import CartModelDTO, CartModel
from src.domains.products.domain.models import ProductModelItemDTO, ProductModelViewDTO
from src.domains.users.domain.models import UserRegisterModelDTO, UserProfileDTO
from src.domains.wishlists.domain.models import WishlistModelDTO, WishlistItemModelDTO

router = APIRouter(prefix="/users", tags=["Users"])


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
    path="/{user_id}/cart",
    response_model=CartModelDTO,
    status_code=status.HTTP_200_OK
)
async def get_user_cart(
        user_id: UUID,
        user_service: Annotated[UserService, Depends(get_user_service)]
) -> CartModelDTO:
    user_cart = await user_service.get_user_cart(user_id=user_id)
    return CartModelDTO(items=user_cart)


@router.post(
    path="/{user_id}/cart/items",
    response_model=ProductModelViewDTO,
    status_code=status.HTTP_201_CREATED
)
async def add_product_to_cart(
        user_id: UUID,
        product: ProductModelItemDTO,
        user_service: Annotated[UserService, Depends(get_user_service)]
) -> ProductModelViewDTO:
    product = await user_service.add_product_to_cart(user_id=user_id, item=product)
    return ProductModelViewDTO(**product.model_dump())


@router.patch(
    path="/{user_id}/cart/items",
    response_model=CartModel,
    status_code=status.HTTP_200_OK
)
async def decrease_product_amount_in_cart(
        user_id: UUID,
        product: ProductModelItemDTO,
        user_service: Annotated[UserService, Depends(get_user_service)]
) -> CartModel:
    # TODO: Вернуть продукт
    return await user_service.decrease_product_amount_in_cart(user_id=user_id, item=product)


@router.get(
    path="/{user_id}/wishlist",
    response_model=WishlistModelDTO,
    status_code=status.HTTP_200_OK
)
async def get_user_wishlist(
        user_id: UUID,
        user_service: Annotated[UserService, Depends(get_user_service)]
) -> WishlistModelDTO:
    wishlist = await user_service.get_user_wishlist(user_id=user_id)
    return WishlistModelDTO(**wishlist.model_dump())


@router.post(
    path="/{user_id}/wishlist/items",
    response_model=ProductModelViewDTO,
    status_code=status.HTTP_201_CREATED
)
async def add_product_to_wishlist(
        user_id: UUID,
        product: WishlistItemModelDTO,
        user_service: Annotated[UserService, Depends(get_user_service)]
) -> ProductModelViewDTO:
    product = await user_service.add_product_to_wishlist(user_id=user_id, item=product)
    return ProductModelViewDTO(**product.model_dump())


@router.delete(
    path="/{user_id}/wishlist/items/{item_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def remove_product_from_wishlist(
        user_id: UUID,
        item_id: UUID,
        user_service: Annotated[UserService, Depends(get_user_service)],
):
    await user_service.remove_product_from_wishlist(user_id=user_id, item_id=item_id)
