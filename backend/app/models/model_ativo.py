from datetime import date


class ModelAtivo:
    def __init__(
        self,
        id: int,
        nome: str,
        descricao: str,
        valor: float,
        data_recebimento: date,
        fixo: str,
        tipo_remuneracao: str,
    ):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.data_recebimento = data_recebimento
        self.fixo = fixo
        self.tipo_remuneracao = tipo_remuneracao
