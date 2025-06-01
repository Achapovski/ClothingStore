import uuid
from enum import Enum
from datetime import datetime
from decimal import Decimal
from typing import ForwardRef

from sqlalchemy import VARCHAR, UUID, TEXT, DECIMAL, TIMESTAMP, ForeignKey, func, Enum as DBEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database.metadata import Base


class StatusEnum(Enum):
    bronze = "Bronze"
    silver = "Silver"
    gold = "Gold"
    diamond = "Diamond"


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, unique=True, index=True, nullable=False)
    username: Mapped[str] = mapped_column(VARCHAR(25), nullable=False)
    login: Mapped[str] = mapped_column(VARCHAR(25), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    email: Mapped[str] = mapped_column(VARCHAR(45), nullable=True, unique=True)
    phone_number: Mapped[str] = mapped_column(VARCHAR(20), nullable=True, unique=True)
    location: Mapped[str] = mapped_column(TEXT, nullable=True)
    personal_discount: Mapped[Decimal] = mapped_column(DECIMAL(3, 1), default=Decimal("0.0"))
    status: Mapped[Enum] = mapped_column(DBEnum(StatusEnum), default=StatusEnum.bronze)
    total_costs: Mapped[Decimal] = mapped_column(DECIMAL(8, 2), default=Decimal("0.0"))
    cart_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("carts.id"), unique=True, nullable=True)
    wishlist_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("wishlists.id"), nullable=True, unique=True)
    signup_date: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())

    wishlist: Mapped[ForwardRef("Wishlist")] = relationship(
        "Wishlist", back_populates="user", uselist=False, lazy="noload"
    )
    cart: Mapped[ForwardRef("Cart")] = relationship("Cart", back_populates="user", uselist=False, lazy="noload")
    order_history: Mapped[list[ForwardRef("OrderHistory")]] = relationship(
        "OrderHistory", back_populates="user", uselist=True, lazy="noload"
    )
