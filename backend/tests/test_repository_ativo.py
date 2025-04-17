from os import getenv

from psycopg2 import connect
from dotenv import load_dotenv
import pytest

from app.repository.repository_ativo import RepositoryAtivo
from app.models.model_ativo import ModelAtivo

load_dotenv()


class TestRepositoryAtivo:
    def test_criacao_tabela_ativos(self):
        try:
            repository = RepositoryAtivo()

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
            AND table_name = 'ativos';
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
