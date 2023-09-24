import os

class Config(object):
    # Configuração geral
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.urandom(24)

    # Configuração do banco de dados
    SQLALCHEMY_DATABASE_URI = 'sqlite:///CETEC.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    pass
