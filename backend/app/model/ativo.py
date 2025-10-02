from sqlalchemy import (
    CheckConstraint,
    ForeignKeyConstraint,
)
from app.model.base import ModelBase


class Ativo(ModelBase):
    __tablename__ = "tb_ativos"
    __comment__ = "Tabela de ativos do sistema"

    __table_args__ = (
        CheckConstraint(
            "frequencia IN ('Q', 'M', 'S')", "ck_ativos_frequencia_QSM"
        ),
        ForeignKeyConstraint(
            ["conta_id"],
            ["tb_contas.id"],
            name="fk_ativo_conta_id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
    )
