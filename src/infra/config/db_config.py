from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker
from typing import Type


class DBConnectionHandler:
    """ Sqalchemy database connection """

    def __init__(self) -> None:
        self.__connection_string = "sqlite:///database.db"
        self.session = None

    def get_engine(self) -> Type[Engine]:
        """ Return connection engine """
        engine = create_engine(self.__connection_string)
        return engine
    
    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        