import uuid
from datetime import datetime

from sqlalchemy import TIMESTAMP, ForeignKey, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database.metadata import Base


class OrderHistory(Base):
    __tablename__ = "orders_history"

    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, index=True)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), unique=True)
    product_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("products.id"), unique=True)
    purchase_date: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="order_history", lazy="noload")
    product: Mapped["Product"] = relationship("Product", back_populates="order_history", lazy="noload")
