from os import getenv
from datetime import date
from sys import path

from psycopg2 import connect
from dotenv import load_dotenv
from pytest import mark

load_dotenv()

PROJECT_ROOT = getenv("PROJECT_ROOT")
path.insert(0, PROJECT_ROOT)

from backend.app.repository.passivo import RepositoryPassivo
from backend.app.model.passivo import ModelPassivo
import config.config


@mark.repository
class TestRepositoryPassivo:
    def test_criacao_tabela(self):
        try:
            repository = RepositoryPassivo()
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

    def test_inserir_dado_na_tabela(self):
        try:
            repository = RepositoryPassivo()
            repository.database = getenv("DATABASE_TESTE")

            id_teste = 1
            nome_teste = "passivo"
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
                database=getenv("DATABASE_TESTE"),
                user=getenv("USER"),
                password=getenv("PASSWORD"),
            )
            cursor = conenection.cursor()

            query = """SELECT * FROM passivos"""

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
            repository = RepositoryPassivo()
            repository.database = getenv("DATABASE_TESTE")

            id_teste = 1
            nome_teste = "passivo_alterado"
            descricao_teste = "teste_alterado"
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

            repository.modificar(modelo_teste)

            conenection = connect(
                host=getenv("HOST"),
                database=getenv("DATABASE_TESTE"),
                user=getenv("USER"),
                password=getenv("PASSWORD"),
            )
            cursor = conenection.cursor()

            query = """SELECT * FROM passivos WHERE id = %s"""

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

    def test_mostrar_dados_na_tabela(self):
        try:
            repository = RepositoryPassivo()
            repository.database = getenv("DATABASE_TESTE")

            existe = repository.mostrar()

            assert len(existe) > 0
            assert isinstance(existe[0], ModelPassivo)

        except Exception as error:
            print("Tipo do erro:", type(error).__name__)
            print("Mensagem:", str(error))
            assert False

    def test_deletar_dado_na_tabela(self):
        try:
            repository = RepositoryPassivo()
            repository.database = getenv("DATABASE_TESTE")

            id_teste = 1
            nome_teste = "passivo_excluído"
            descricao_teste = "teste_excluído"
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

            repository.deletar(modelo_teste)

            conenection = connect(
                host=getenv("HOST"),
                database=getenv("DATABASE_TESTE"),
                user=getenv("USER"),
                password=getenv("PASSWORD"),
            )
            cursor = conenection.cursor()

            query = """SELECT * FROM passivos WHERE id = %s"""

            cursor.execute(query, (str(modelo_teste.id)))
            existe = cursor.fetchone()
            if existe:
                assert False
            else:
                assert True

            query = """DROP TABLE IF EXISTS passivos"""
            cursor.execute(query)
            conenection.commit()

        except Exception as error:
            print("Tipo do erro:", type(error).__name__)
            print("Mensagem:", str(error))
            assert False
        finally:
            cursor.close()
