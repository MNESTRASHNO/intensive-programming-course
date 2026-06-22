from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

class Func(Base):
    __tablename__ = "function"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    func_name: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    func: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
