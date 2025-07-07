from sqlalchemy import (
    Column,
    Integer,
    String,
    Numeric,
    Text,
    Date,
    CheckConstraint,
    ForeignKey,
)
from app.core.database import Base


class Passivo(Base):
    __tablename__ = "tb_passivos"
    __comment__ = "Tabela de passivos do sistema"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(Text, nullable=True)
    valor = Column(Numeric, nullable=False)
    referente = Column(String, nullable=False, comment="ex: Se ele é boleto, saúde, empréstimo")
    data = Column(Date, nullable=False, comment="Data que teve o passivo")
    fixo = Column(
        String(1),
        nullable=False,
        comment="O passivo é acontecido de maneira constante(S) ou foi avulso(N)",
    )
    vencimento = Column(Date, nullable=True)
    plano = Column(
        String(1),
        nullable=True,
        comment="Caso seja fixo se ele é D(Diário), M(Mensal), S(Semanal)",
    )
    id_conta = Column(
        Integer, nullable=False, comment="Conta a qual o passivo está relacionado"
    )

    __table_args__ = (
        CheckConstraint("fixo IN ('S', 'N')", "ck_passivos_fixo_SN"),
        CheckConstraint("plano IN ('D', 'M', 'S')", "ck_passivos_plano_DMS"),
        ForeignKey(
            "id_conta",
            "tb_contas.id",
            name="fk_passivo_conta_id",
            ondelete=True,
            onupdate=True,
        ),
    )
