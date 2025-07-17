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


class Ativo(Base):
    __tablename__ = "tb_ativos"
    __comment__ = "Tabela de ativos do sistema"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    referencia = Column(
        String, nullable=False, comment="ex: Se ele é salario, freelancer, empréstimo"
    )
    descricao = Column(Text, nullable=True)
    valor = Column(Numeric, nullable=False)
    data_adquirido = Column(
        Date, nullable=False, comment="Data em que foi adquirido o ativo"
    )
    eh_fixo = Column(
        Boolean,
        nullable=False,
        comment="O ativo é recebido de maneira constante?",
    )
    tipo_remuneracao = Column(
        String(1),
        nullable=True,
        comment="Caso seja fixo se ele é Q(Quizena), M(Mensal), S(Semanal)",
    )
    data_finalizado = Column(Date, nullable=True)
    conta_id = Column(
        Integer, nullable=False, comment="Conta a qual o ativo está relacionado"
    )

    __table_args__ = (
        CheckConstraint(
            "tipo_remuneracao IN ('Q', 'M', 'S')", "ck_ativos_tipo_remuneracao_QSM"
        ),
        ForeignKeyConstraint(
            ["conta_id"],
            ["tb_contas.id"],
            name="fk_ativo_conta_id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
    )
