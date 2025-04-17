from datetime import date


class ModelPassivo:
    def __init__(
        self,
        id: int,
        nome: str,
        descricao: str,
        valor: float,
        data: date,
        fixo: str,
        vencimento: date,
        plano: str,
    ):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.data = data
        self.fixo = fixo
        self.vencimento = vencimento
        self.plano = plano
