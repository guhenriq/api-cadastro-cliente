import datetime

from sqlalchemy import Column, String, Date, DateTime
from src.infra.config import Base


class Clients(Base):
    """ Clients Entity """

    __tablename__ = "clients"

    cpf = Column(String(11), primary_key=True, unique=True)
    name = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    email = Column(String(100), nullable=True)
    postalcode = Column(String(50), nullable=True)
    address = Column(String(100), nullable=True)
    district = Column(String(100), nullable=True)
    city = Column(String(50), nullable=True)
    state = Column(String(50), nullable=True)
    phone = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.now)
    updated_at = Column(DateTime(timezone=True), default=datetime.datetime.now, onupdate=datetime.datetime.now)

    def __repr__(self) -> str:
        return f"Client: [cpf={self.cpf}, name={self.name}, lastname={self.lastname}]"