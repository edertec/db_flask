from flask import Flask, render_template
from database import db, init_db  # Importa db e init_db de database.py
import config

# Criação da instância da aplicação Flask
app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = config.Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.Config.SQLALCHEMY_TRACK_MODIFICATIONS
app.secret_key = config.Config.SECRET_KEY

# Inicializa o banco de dados
init_db(app)

# Importação e registro dos blueprints
from views.fornecedor_views import fornecedor_blueprint
from views.produto_views import produto_blueprint


app.register_blueprint(fornecedor_blueprint, url_prefix='/fornecedor')
app.register_blueprint(produto_blueprint, url_prefix='/produto')

# Rota principal (pode ser removida ou modificada conforme necessário)
@app.route('/')
def index():
    return render_template('base.html')

# Execução da aplicação
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(debug=True)
