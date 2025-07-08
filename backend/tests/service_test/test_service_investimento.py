from os import getenv
from datetime import date
from sys import path

from psycopg2 import connect
from dotenv import load_dotenv
from pytest import mark

load_dotenv()

PROJECT_ROOT = getenv("PROJECT_ROOT")
path.insert(0, PROJECT_ROOT)

from backend.app.repository.investimento import RepositoryInvestimento
from backend.app.models.investimento import ModelInvestimento
import config.config

@mark.service
class TestServiceInvestimento:
    def test_inserindo_dados_filtrados_na_tabela(self):
        try:
            service = ServiceInvestimento()
            service.repository.database = getenv("DATABASE_TESTE")
            service.repository.criar_tabela()

            id_teste = 1
            nome_teste = "     investimento    "
            descricao_teste = "   teste         descrição     não formatada"
            tipo_investimento_teste = "    A    "
            valor_teste = "51,50   "
            data_teste = "23/04/2025    "

            modelo_teste = ModelInvestimento(
                id=id_teste,
                nome=nome_teste,
                descricao=descricao_teste,
                tipo=tipo_investimento_teste,
                valor=valor_teste,
                data=data_teste,
            )

            service.inserir(modelo_teste)

            conenection = connect(
                host=getenv("HOST"),
                database=getenv("DATABASE_TESTE"),
                user=getenv("USER"),
                password=getenv("PASSWORD"),
            )
            cursor = conenection.cursor()

            query = """SELECT * FROM ativos"""

            cursor.execute(query)
            existe = cursor.fetchone()
            if existe:
                assert existe[1] == "investimento"
                assert existe[2] == "teste descrição não formatada"
                assert existe[3] == "A"
                assert existe[4] == 51.50
                assert existe[5] == "2025-04-23"
            else:
                assert False

        except Exception as error:
            print("Tipo do erro:", type(error).__name__)
            print("Mensagem:", str(error))
            assert False
        finally:
            cursor.close()
