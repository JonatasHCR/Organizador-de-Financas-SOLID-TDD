from os import getenv
from datetime import date
from sys import path

from psycopg2 import connect
from dotenv import load_dotenv

from app.repository.repository_investimento import RepositoryInvestimento
from app.models.model_investimento import ModelInvestimento
import config.config

load_dotenv()

PROJECT_ROOT = getenv("PROJECT_ROOT")
path.insert(0, PROJECT_ROOT)


class TestRepositoryInvestimento:
    def test_criacao_tabela(self):
        try:
            repository = RepositoryInvestimento()
            repository.database = getenv("DATABASE_TESTE")
            repository.criar_tabela()

            conenection = connect(
                host=getenv("HOST"),
                database=getenv("DATABASE_TESTE"),
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
            repository.database = getenv("DATABASE_TESTE")

            id_teste = 1
            nome_teste = "investimento"
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
                database=getenv("DATABASE_TESTE"),
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

    def test_modificar_dado_na_tabela(self):
        try:
            repository = RepositoryInvestimento()
            repository.database = getenv("DATABASE_TESTE")

            id_teste = 1
            nome_teste = "investimento_alterado"
            descricao_teste = "teste_alterado"
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

            repository.modificar(modelo_teste)

            conenection = connect(
                host=getenv("HOST"),
                database=getenv("DATABASE_TESTE"),
                user=getenv("USER"),
                password=getenv("PASSWORD"),
            )
            cursor = conenection.cursor()

            query = """SELECT * FROM investimentos WHERE id = %s"""

            cursor.execute(query, (str(modelo_teste.id)))
            existe = cursor.fetchone()
            if existe:
                assert existe[1] == nome_teste
                assert existe[2] == descricao_teste
            else:
                assert False

        except Exception as error:
            print("Tipo do erro:", type(error).__name__)
            print("Mensagem:", str(error))
            assert False
        finally:
            cursor.close()
