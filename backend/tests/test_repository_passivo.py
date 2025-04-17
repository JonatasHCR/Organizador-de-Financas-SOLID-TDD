from os import getenv

from psycopg2 import connect
from dotenv import load_dotenv

from app.repository.repository_passivo import RepositoryPassivo

load_dotenv()


class TestRepositoryAtivo:
    def test_criacao_tabela_ativos(self):
        try:
            repository = RepositoryPassivo()

            conenection = connect(
                host=getenv("HOST"),
                database=getenv("DATABASE"),
                user=getenv("USER"),
                password=getenv("PASSWORD"),
            )
            cursor = conenection.cursor()

            query = """
            SELECT 1 
            FROM information_schema.tables
            WHERE table_schema = 'public'
            AND table_name = 'passivos';
            """

            cursor.execute(query)
            existe = cursor.fetchone()
            if existe:
                assert True
            else:
                assert False

        except Exception as error:
            print("Tipo do erro:", type(error).__name__)
            print("Mensagem:", str(error))
            assert False
        finally:
            cursor.close()
