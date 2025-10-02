from sqlalchemy import (
    Column,
    Integer,
    String,
    Numeric,
    Text,
    Date,
    Boolean,
)
from app.core.database import Base



class ModelBase(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    referencia = Column(String, nullable=False)
    descricao = Column(Text, nullable=True)
    valor = Column(Numeric, nullable=False)
    data_adquirido = Column(Date, nullable=False)
    fixo = Column(Boolean, nullable=False)
    frequencia = Column(String(1), nullable=True)
    data_finalizado = Column(Date, nullable=True)
    conta_id = Column(Integer, nullable=False)
