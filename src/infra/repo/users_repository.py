from src.infra.config import DBConnectionHandler
from src.infra.entities import Users

class UsersRepository:

    @classmethod
    def insert_user(cls, username: str, password: str):
        """ Insert new user """
        
        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(username=username, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

