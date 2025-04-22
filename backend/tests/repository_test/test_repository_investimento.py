from os import getenv
from datetime import date
from sys import path

from psycopg2 import connect
from dotenv import load_dotenv

PROJECT_ROOT = getenv("PROJECT_ROOT")
path.insert(0, PROJECT_ROOT)

from app.repository.repository_investimento import RepositoryInvestimento
from app.models.model_investimento import ModelInvestimento

load_dotenv()


class TestRepositoryInvestimento:
    def test_criacao_tabela(self):
        try:
            repository = RepositoryInvestimento()

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
            AND table_name = 'investimentos';
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

    def test_inserir_dado_na_tabela(self):
        try:
            repository = RepositoryInvestimento()

            id_teste = 1
            nome_teste = "despesa"
            descricao_teste = "teste"
            tipo_investimento_teste = "A"
            valor_teste = 50.0
            data_teste = date.today()

            modelo_teste = ModelInvestimento(
                id=id_teste,
                nome=nome_teste,
                descricao=descricao_teste,
                tipo=tipo_investimento_teste,
                valor=valor_teste,
                data=data_teste,
            )

            repository.inserir(modelo_teste)

            conenection = connect(
                host=getenv("HOST"),
                database=getenv("DATABASE"),
                user=getenv("USER"),
                password=getenv("PASSWORD"),
            )
            cursor = conenection.cursor()

            query = """SELECT * FROM investimentos"""

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
