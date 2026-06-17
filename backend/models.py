from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime

from database import Base

class Usuario(Base):
    __tablename__= "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha_hash = Column(String, nullable=False)
    tipo = Column(String, default="usuario")
    ativo = Column(Boolean, default=True)
    data_criacao = Column(DateTime, default=datetime.utcnow)