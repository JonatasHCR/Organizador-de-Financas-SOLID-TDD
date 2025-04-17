from os import getenv
from datetime import date

from psycopg2 import connect
from dotenv import load_dotenv

from app.repository.repository_passivo import RepositoryPassivo
from app.models.model_passivo import ModelPassivo

load_dotenv()


class TestRepositoryPassivo:
    def test_criacao_tabela(self):
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

    def test_inserir_dado_na_tabela():
        try:
            repository = RepositoryPassivo()

            id_teste = 1
            nome_teste = "despesa"
            descricao_teste = "teste"
            valor_teste = 50.0
            data_teste = date.today()
            fixo_teste = "N"
            vencimento_teste = date.today()
            plano_pagamento_teste = "M"

            modelo_teste = ModelPassivo(
                id=id_teste,
                nome=nome_teste,
                descricao=descricao_teste,
                valor=valor_teste,
                data=data_teste,
                fixo=fixo_teste,
                vencimento=vencimento_teste,
                plano=plano_pagamento_teste,
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
