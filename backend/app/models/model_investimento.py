from datetime import date


class ModelInvestimento:
    def __init__(
        self,
        id: int,
        nome: str,
        descricao: str,
        tipo: str,
        valor: float,
        data: date,
    ):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.tipo = tipo
        self.valor = valor
        self.data = data
