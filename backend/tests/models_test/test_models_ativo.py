from sys import path
from os import getenv
from datetime import date

from dotenv import load_dotenv
from pytest import mark

load_dotenv()

PROJECT_ROOT = getenv("PROJECT_ROOT")
path.insert(0, PROJECT_ROOT)

from backend.app.models.ativo import ModelAtivo
import config.config


@mark.models
class TestModelsAtivo:
    def test_model_ativo(self):
        id_teste = 1
        nome_teste = "ativo"
        descricao_teste = "teste"
        valor_teste = 50.0
        data_teste = date.today()
        fixo_teste = "N"
        tipo_renumeracao_teste = "M"
        try:
            modelo_teste = ModelAtivo(
                id=id_teste,
                nome=nome_teste,
                descricao=descricao_teste,
                valor=valor_teste,
                data=data_teste,
                fixo=fixo_teste,
                tipo_remuneracao=tipo_renumeracao_teste,
            )
            assert len(modelo_teste.to_list()) == 7
        except Exception as error:
            print("Tipo do erro:", type(error).__name__)
            print("Mensagem:", str(error))
            assert False
