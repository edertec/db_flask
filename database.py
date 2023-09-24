from flask_sqlalchemy import SQLAlchemy

# Inicializa o objeto SQLAlchemy
db = SQLAlchemy()

def init_db(app):
    """
    Inicializa o banco de dados.
    """
    # Configura o SQLAlchemy para usar com o Flask
    db.init_app(app)

    # Cria as tabelas no banco de dados
    with app.app_context():
        db.create_all()
