import datetime

from sqlalchemy import Column, String, Integer, DateTime
from src.infra.config import Base

class Users(Base):
    """ Users Entity """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.now)
    updated_at = Column(DateTime(timezone=True), default=datetime.datetime.now, onupdate=datetime.datetime.now)

    def __repr__(self) -> str:
        return f"User: [name={self.username}]"