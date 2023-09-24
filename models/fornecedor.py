from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from database import db 

Base = declarative_base()

class Fornecedor(db.Model):
    __tablename__ = 'fornecedores'

    codigo = Column(Integer, primary_key=True, autoincrement=True)
    fornecedor = Column(String(100), nullable=False)
    telefone = Column(String(15), nullable=True)
    endereco = Column(String(200), nullable=True)
    situacao = Column(Boolean, default=True)
    email = Column(String(100), nullable=True)

    def __init__(self, fornecedor, telefone, endereco, situacao, email):
        self.fornecedor = fornecedor
        self.telefone = telefone
        self.endereco = endereco
        self.situacao = situacao
        self.email = email

    def __repr__(self):
        return f"<Fornecedor(codigo='{self.codigo}', fornecedor='{self.fornecedor}', telefone='{self.telefone}', endereco='{self.endereco}', situacao='{self.situacao}', email='{self.email}')>"
