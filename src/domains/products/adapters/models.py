import uuid
from decimal import Decimal
from typing import ForwardRef

from sqlalchemy import VARCHAR, UUID, TEXT, DECIMAL, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database.metadata import Base

OrderHistory = ForwardRef("OrderHistory")
Collection = ForwardRef("Collection")
Category = ForwardRef("Category")


class Product(Base):
    __tablename__ = "products"

    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, index=True, nullable=False, unique=True)
    title: Mapped[str] = mapped_column(VARCHAR(35), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(TEXT, nullable=True)
    type: Mapped[str] = mapped_column(VARCHAR(20), nullable=False)
    color: Mapped[str] = mapped_column(VARCHAR(20), nullable=False)
    price: Mapped[Decimal] = mapped_column(DECIMAL(4, 2), nullable=False)
    material: Mapped[str] = mapped_column(VARCHAR(25), nullable=False)
    discount: Mapped[Decimal] = mapped_column(DECIMAL(3, 1), default=Decimal("0.0"))
    image_url: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    category_title: Mapped[uuid.UUID] = mapped_column(ForeignKey("categories.title"), nullable=False)
    collection_title: Mapped[str] = mapped_column(ForeignKey("collections.title"), nullable=False, unique=False)

    order_history: Mapped[list["OrderHistory"]] = relationship("OrderHistory", back_populates="product", lazy="noload")
    collection: Mapped["Collection"] = relationship("Collection", back_populates="products", lazy="noload")
    category: Mapped["Category"] = relationship("Category", back_populates="products", lazy="noload")
