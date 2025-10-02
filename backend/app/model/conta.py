from sqlalchemy import (
    Column,
    Integer,
    String,
)
from app.core.database import Base


class Conta(Base):
    __tablename__ = "tb_contas"
    __comment__ = "Tabela de contas do sistema"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    referencia = Column(String, nullable=False)
