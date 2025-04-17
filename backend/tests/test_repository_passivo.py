from os import getenv

from psycopg2 import connect
from dotenv import load_dotenv


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
            print(error)
            assert False
        finally:
            cursor.close()
