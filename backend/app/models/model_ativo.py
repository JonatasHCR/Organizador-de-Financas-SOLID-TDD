from datetime import date


class ModelAtivo:
    def __init__(
        self,
        id: int,
        nome: str,
        descricao: str,
        valor: float,
        data: date,
        fixo: str,
        tipo_remuneracao: str,
    ):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.data = data
        self.fixo = fixo
        self.tipo_remuneracao = tipo_remuneracao
