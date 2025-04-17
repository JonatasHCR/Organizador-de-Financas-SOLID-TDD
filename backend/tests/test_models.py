from datetime import date


class TestModels:
    def test_model_ativo(self):
        id_teste = 1
        nome_teste = "salario"
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
                data_recebimento=data_teste,
                fixo=fixo_teste,
                tipo_remuneracao=tipo_renumeracao_teste,
            )
            assert True
        except Exception as e:
            print(e)
            assert False
