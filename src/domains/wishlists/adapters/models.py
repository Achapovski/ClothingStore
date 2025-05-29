import uuid

from sqlalchemy import UUID, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database.metadata import Base


class Wishlist(Base):
    __tablename__ = "wishlists"

    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, index=True)
    items: Mapped[dict] = mapped_column(JSON, default=dict())

    user: Mapped["User"] = relationship("User", back_populates="wishlist", uselist=False, lazy="selectin")
