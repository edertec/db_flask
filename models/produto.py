from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from database import db

Base = declarative_base()

class Produto(db.Model):
    __tablename__ = 'produtos'

    codigo = Column(Integer, primary_key=True, autoincrement=True)
    produto = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    unidade = Column(String(20), nullable=False)
    situacao = Column(Boolean, default=True)
    descricao = Column(String(300), nullable=True)
    fabricante = Column(String(100), nullable=True)

    def __init__(self, produto, preco, unidade, situacao, descricao, fabricante):
        self.produto = produto
        self.preco = preco
        self.unidade = unidade
        self.situacao = situacao
        self.descricao = descricao
        self.fabricante = fabricante

    def __repr__(self):
        return f"<Produto(codigo='{self.codigo}', produto='{self.produto}', preco='{self.preco}', unidade='{self.unidade}', situacao='{self.situacao}', descricao='{self.descricao}', fabricante='{self.fabricante}')>"
