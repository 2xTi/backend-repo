from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, DateTime
from sqlalchemy.sql import text, func
from database import Base, engine

class Model_Mensagem(Base):
    __tablename__ = 'teste'
 
    id = Column(Integer, primary_key=True, nullable=False)
    titulo = Column(String, nullable=False)
    conteudo = Column(String, nullable=False)
    publicada = Column(Boolean, server_default=text('true'), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)
    
class Model_MenuNav(Base):
    __tablename__ = 'menus'

    id = Column(Integer, primary_key=True, nullable=False)
    menuNav = Column(String, nullable=False)
    link = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)
