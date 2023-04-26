from src.infra.config import DBConnectionHandler
from src.infra.entities import Clients


class ClientsRepository:

    @classmethod
    def insert_client(cpf: str, name: str, lastname: str, date_of_birth: str,
                      email: str | None = None, postalcode: str | None = None,
                      address: str | None = None, district: str | None = None,
                      city: str | None = None, state: str | None = None, phone: str | None = None):

        with DBConnectionHandler() as db_connection:

            try:
                new_client = Clients(cpf=cpf, name=name, lastname=lastname, date_of_birth=date_of_birth,
                                     email=email, postalcode=postalcode, address=address, district=district, 
                                     city=city, state=state, phone=phone)
                
                db_connection.session.add(new_client)
                db_connection.session.commit()                
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
