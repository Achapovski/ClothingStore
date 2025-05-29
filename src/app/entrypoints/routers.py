from fastapi import APIRouter

from src.app.entrypoints.routes import router as app_router
from src.domains.carts.domain.models import CartModel
from src.domains.categories.domain.models import CategoryModelDTORel, CategoryModel
from src.domains.products.domain.models import ProductModelRel, ProductModel
from src.domains.users.domain.models import UserModel, UserRelationshipModel
from src.domains.users.entrypoints.routes import router as users_router
from src.domains.collections.entrypoints.routes import router as collections_router
from src.domains.products.entrypoints.routes import router as products_router
from src.domains.categories.entrypoints.routes import router as category_router
from src.domains.histories.adapters.models import OrderHistory
from src.domains.wishlists.adapters.models import Wishlist
from src.domains.wishlists.domain.models import WishlistModelDTORel, WishlistModel

UserModel.model_rebuild()
CategoryModel.model_rebuild()
ProductModel.model_rebuild()
WishlistModel.model_rebuild()
ProductModelRel.model_rebuild()
CategoryModel.model_rebuild()
WishlistModelDTORel.model_rebuild()
CategoryModelDTORel.model_rebuild()
CartModel.model_rebuild()
UserRelationshipModel.model_rebuild()
ProductModelRel.model_rebuild()

routers = [
    users_router,
    collections_router,
    products_router,
    category_router,
    app_router,
]


def get_app_router():
    router = APIRouter()

    for router_ in routers:
        router.include_router(router_)

    return router
