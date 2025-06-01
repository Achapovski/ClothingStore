import uuid
from datetime import datetime
from decimal import Decimal
from typing import ForwardRef

from sqlalchemy import VARCHAR, UUID, TEXT, DECIMAL, TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database.metadata import Base

Product = ForwardRef("Product")


class Collection(Base):
    __tablename__ = "collections"

    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, unique=True, index=True, nullable=False)
    title: Mapped[str] = mapped_column(VARCHAR(45), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(TEXT, nullable=True)
    created_date: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), default=func.now())
    discount: Mapped[Decimal] = mapped_column(DECIMAL(3, 1), default=Decimal("0.0"))

    products: Mapped[list["Product"]] = relationship(
        "Product", back_populates="collection", uselist=True, lazy="noload"
    )
