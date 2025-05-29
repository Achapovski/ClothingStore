from typing import Optional

from core.database.interfaces.repositories import SQLAlchemyAbstractRepository
from core.interfaces.models import AbstractModel
from src.domains.histories.interfaces.repositories import OrdersHistoriesAbstractRepository


class OrdersHistoryRepository(SQLAlchemyAbstractRepository, OrdersHistoriesAbstractRepository):
    def get_history(self, user_id: int) -> list[AbstractModel]:
        pass

    def get(self, id_: int) -> Optional[AbstractModel]:
        pass

    def add(self, model: AbstractModel) -> AbstractModel:
        pass

    def update(self) -> Optional[AbstractModel]:
        pass

    def delete(self) -> None:
        pass
