from datetime import date


class ModelPassivo:
    def __init__(
        self,
        id: int,
        nome: str,
        descricao: str,
        valor: float,
        data_pagamento: date,
        fixo: str,
        vencimento: date,
        plano_pagamento: str,
    ):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.data_pagamento = data_pagamento
        self.fixo = fixo
        self.vencimento = vencimento
        self.plano_pagamento = plano_pagamento
