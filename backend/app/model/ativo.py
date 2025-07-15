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


class Ativo(Base):
    __tablename__ = "tb_ativos"
    __comment__ = "Tabela de ativos do sistema"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(Text, nullable=True)
    valor = Column(Numeric, nullable=False)
    referente = Column(
        String, nullable=False, comment="ex: Se ele é salario, freelancer, empréstimo"
    )
    data = Column(Date, nullable=False, comment="Data em que foi adquirido o ativo")
    fixo = Column(
        String(1),
        nullable=False,
        comment="O ativo é recebido de maneira constante(S) ou foi avulso(N)",
    )
    tipo_remuneracao = Column(
        String(1),
        nullable=True,
        comment="Caso seja fixo se ele é Q(Quizena), M(Mensal), S(Semanal)",
    )
    finalizado = Column(Date, nullable=True)
    id_conta = Column(
        Integer, nullable=False, comment="Conta a qual o ativo está relacionado"
    )

    __table_args__ = (
        CheckConstraint("fixo IN ('S', 'N')", "ck_ativos_fixo_SN"),
        CheckConstraint(
            "tipo_remuneracao IN ('Q', 'M', 'S')", "ck_ativos_tipo_remuneracao_QSM"
        ),
        ForeignKeyConstraint(
            ["id_conta"],
            ["tb_contas.id"],
            name="fk_ativo_conta_id",
            ondelete="CASCADE",
            onupdate="CASCADE"
        ),
    )
