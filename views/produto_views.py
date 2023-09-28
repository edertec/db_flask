from flask import Blueprint, request, render_template, redirect, url_for, flash
from models.produto import Produto
from database import db

produto_blueprint = Blueprint('produto', __name__, template_folder='templates')

# Listar todos os produtos
@produto_blueprint.route('/produtos/listar', methods=['GET'])
def listar_produtos():
    produtos = Produto.query.all()
    return render_template('produto/listar.html', produtos=produtos)

# Cadastrar novo produto
@produto_blueprint.route('/produtos/cadastrar', methods=['GET', 'POST'])
def cadastrar_produto():
    if request.method == 'POST':
        produto = Produto(
            produto=request.form['produto'],
            preco=float(request.form['preco']),
            unidade=request.form['unidade'],
            situacao=bool(request.form.get('situacao')),
            descricao=request.form['descricao'],
            fabricante=request.form['fabricante']
        )
        db.session.add(produto)
        db.session.commit()
        flash('Produto cadastrado com sucesso!', 'success')
        return redirect(url_for('produto.listar_produtos'))
    return render_template('produto/cadastrar.html')

# Atualizar produto
@produto_blueprint.route('/produtos/editar/<int:codigo>', methods=['GET', 'POST'])
def editar_produto(codigo):
    if request.method == 'GET':
        return carregar_tela(codigo)  
    if request.method == 'POST':
        produto = Produto.query.get(codigo)
        produto.produto = request.form['produto']
        produto.preco = float(request.form['preco'])
        produto.unidade = request.form['unidade']
        produto.situacao = bool(request.form.get('situacao'))
        produto.descricao = request.form['descricao']
        produto.fabricante = request.form['fabricante']
        db.session.commit()
        flash('Produto atualizado com sucesso!', 'success')
        return redirect(url_for('produto.listar_produtos'))

# Excluir produto
@produto_blueprint.route('/produtos/excluir/<int:codigo>', methods=['GET'])
def excluir_produto(codigo):
    produto = Produto.query.get(codigo)
    db.session.delete(produto)
    db.session.commit()
    flash('Produto excluído com sucesso!', 'success')
    return redirect(url_for('produto.listar_produtos'))

def carregar_tela(codigo):
    produto = Produto.query.get(codigo)
    form_data = {
        'produto': produto.produto,
        'preco': produto.preco,
        'unidade': produto.unidade,
        'situacao': produto.situacao,
        'descricao': produto.descricao,
        'fabricante': produto.fabricante
    }
    return render_template('produto/cadastrar.html', form_data=form_data)

