from sqlalchemy import (
    CheckConstraint,
    ForeignKeyConstraint,
)
from app.model.base import ModelBase


class Passivo(ModelBase):
    __tablename__ = "tb_passivos"
    __comment__ = "Tabela de passivos do sistema"

    __table_args__ = (
        CheckConstraint("frequencia IN ('D', 'M', 'S')", "ck_passivos_plano_DMS"),
        ForeignKeyConstraint(
            ["conta_id"],
            ["tb_contas.id"],
            name="fk_passivo_conta_id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
    )
