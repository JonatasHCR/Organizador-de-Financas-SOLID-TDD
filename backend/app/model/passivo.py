from sqlalchemy import (
    Column,
    Integer,
    String,
    Numeric,
    Text,
    Date,
    CheckConstraint,
    ForeignKeyConstraint,
    Boolean,
)
from app.core.database import Base


class Passivo(Base):
    __tablename__ = "tb_passivos"
    __comment__ = "Tabela de passivos do sistema"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    referencia = Column(
        String, nullable=False, comment="ex: Se ele é foi de Saúde, Conta, Empréstimo"
    )
    descricao = Column(Text, nullable=True)
    valor = Column(Numeric, nullable=False)
    data = Column(Date, nullable=False, comment="Data que teve o passivo")
    eh_fixo = Column(
        Boolean,
        nullable=False,
        comment="O passivo é acontecido de maneira constante?",
    )
    frequencia = Column(
        String(1),
        nullable=True,
        comment="Caso seja fixo se ele é D(Diário), M(Mensal), S(Semanal)",
    )
    vencimento = Column(Date, nullable=True)
    conta_id = Column(
        Integer, nullable=False, comment="Conta a qual o passivo está relacionado"
    )

    __table_args__ = (
        CheckConstraint("plano IN ('D', 'M', 'S')", "ck_passivos_plano_DMS"),
        ForeignKeyConstraint(
            ["conta_id"],
            ["tb_contas.id"],
            name="fk_passivo_conta_id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
    )
