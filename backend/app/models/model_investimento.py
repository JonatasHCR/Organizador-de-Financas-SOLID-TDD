from datetime import date


class ModelInvestimento:
    def __init__(
        self,
        id: int,
        nome: str,
        descricao: str,
        tipo_investimento: str,
        valor: float,
        data_investimento: date,
    ):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.tipo_investimento = tipo_investimento
        self.valor = valor
        self.data_investimento = data_investimento
