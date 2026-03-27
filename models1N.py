from datetime import datetime
from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)


    tasks: Mapped[list["Task"]] = relationship(
        back_populates="user")


class Task(Base):

    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(200),nullable=False)


    user_id : Mapped[int] = mapped_column(
        ForeignKey("user.id"),
        nullable=False
                                          
    )

    created_at: Mapped[datetime] = mapped_column(DateTime, default= datetime.now)

    user: Mapped["User"] = relationship(
        back_populates="tasks"
    )