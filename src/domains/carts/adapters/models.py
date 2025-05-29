import uuid

from sqlalchemy import JSON, UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database.metadata import Base


class Cart(Base):
    __tablename__ = "carts"

    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, index=True)
    items: Mapped[dict] = mapped_column(JSON, default=dict())

    user: Mapped["User"] = relationship("User", back_populates="cart", uselist=False, lazy="selectin")
