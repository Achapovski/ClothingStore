import uuid
from enum import unique
from typing import ForwardRef

from sqlalchemy import VARCHAR, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database.metadata import Base

Product = ForwardRef("Product")


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, unique=True, index=True)
    title: Mapped[str] = mapped_column(VARCHAR(35), nullable=False, unique=True)

    products: Mapped[list["Product"]] = relationship("Product", back_populates="category", lazy="noload", uselist=True)
