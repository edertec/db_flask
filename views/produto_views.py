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
    produto = Produto.query.get(codigo)
    if request.method == 'POST':
        produto.produto = request.form['produto']
        produto.preco = float(request.form['preco'])
        produto.unidade = request.form['unidade']
        produto.situacao = bool(request.form.get('situacao'))
        produto.descricao = request.form['descricao']
        produto.fabricante = request.form['fabricante']
        db.commit()
        flash('Produto atualizado com sucesso!', 'success')
        return redirect(url_for('produto.listar_produtos'))
    return render_template('produto/editar.html', produto=produto)

# Excluir produto
@produto_blueprint.route('/produtos/excluir/<int:codigo>', methods=['GET'])
def excluir_produto(codigo):
    produto = Produto.query.get(codigo)
    db.delete(produto)
    db.commit()
    flash('Produto excluído com sucesso!', 'success')
    return redirect(url_for('produto.listar_produtos'))

