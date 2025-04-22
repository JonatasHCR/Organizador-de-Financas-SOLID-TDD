from os import getenv
from datetime import date
from sys import path

from psycopg2 import connect
from dotenv import load_dotenv

PROJECT_ROOT = getenv("PROJECT_ROOT")
path.insert(0, PROJECT_ROOT)

from app.repository.repository_ativo import RepositoryAtivo
from app.models.model_ativo import ModelAtivo

load_dotenv()


class TestRepositoryAtivo:
    def test_criacao_tabela(self):
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

    def test_inserir_dado_na_tabela(self):
        try:
            repository = RepositoryAtivo()

            id_teste = 1
            nome_teste = "ativo"
            descricao_teste = "teste"
            valor_teste = 50.0
            data_teste = date.today()
            fixo_teste = "N"
            tipo_renumeracao_teste = "M"

            modelo_teste = ModelAtivo(
                id=id_teste,
                nome=nome_teste,
                descricao=descricao_teste,
                valor=valor_teste,
                data=data_teste,
                fixo=fixo_teste,
                tipo_remuneracao=tipo_renumeracao_teste,
            )

            repository.inserir(modelo_teste)

            conenection = connect(
                host=getenv("HOST"),
                database=getenv("DATABASE"),
                user=getenv("USER"),
                password=getenv("PASSWORD"),
            )
            cursor = conenection.cursor()

            query = """SELECT * FROM ativos"""

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
