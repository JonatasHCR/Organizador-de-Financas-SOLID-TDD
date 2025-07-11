from sqlalchemy import Column, Integer, String, Text
from app.core.database import Database


class Conta(Database.Base):
    __tablename__ = "tb_contas"
    __comment__ = "Tabela de contas do sistema"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False, unique=True)
    descricao = Column(Text, nullable=True)
