from sqlalchemy import (
    Column,
    Integer,
    String,
    Numeric,
    Text,
    Date,
    CheckConstraint,
    ForeignKeyConstraint,
)
from app.core.database import Base


class Investimento(Base):
    __tablename__ = "tb_investimentos"
    __comment__ = "Tabela de investimentos do sistema"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(Text, nullable=True)
    tipo = Column(String(4), nullable=False)
    valor = Column(Numeric, nullable=False)
    data = Column(
        Date, nullable=False, comment="Data em que foi adquirido o investimento"
    )
    id_conta = Column(
        Integer, nullable=False, comment="Conta a qual o investimento está relacionado"
    )

    __table_args__ = (
        CheckConstraint(
            "tipo IN ('A', 'FII', 'C', 'ETF', 'ETFI', 'AI', 'TD', 'RF')",
            "ck_investimentos_tipo",
        ),
        ForeignKeyConstraint(
            ["id_conta"],
            ["tb_contas.id"],
            name="fk_investimento_conta_id",
            ondelete="CASCADE",
            onupdate="CASCADE"
        ),
    )
