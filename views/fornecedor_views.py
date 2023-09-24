from flask import Blueprint, request, render_template, redirect, url_for, flash
from models.fornecedor import Fornecedor
from database import db

fornecedor_blueprint = Blueprint('fornecedor', __name__, template_folder='templates')

# Listar todos os fornecedores
@fornecedor_blueprint.route('/fornecedores/listar', methods=['GET'])
def listar_fornecedores():
    fornecedores = Fornecedor.query.all()
    return render_template('fornecedor/listar.html', fornecedores=fornecedores)

# Cadastrar novo fornecedor
@fornecedor_blueprint.route('/fornecedores/cadastrar', methods=['GET', 'POST'])
def cadastrar_fornecedor():
    if request.method == 'POST':
        fornecedor = Fornecedor(
            fornecedor=request.form['fornecedor'],
            telefone=request.form['telefone'],
            endereco=request.form['endereco'],
            situacao=bool(request.form.get('situacao')),
            email=request.form['email']
        )
        db.session.add(fornecedor)
        db.session.commit()
        flash('Fornecedor cadastrado com sucesso!', 'success')
        return redirect(url_for('fornecedor.listar_fornecedores'))
    return render_template('fornecedor/cadastrar.html')

# Atualizar fornecedor
@fornecedor_blueprint.route('/fornecedores/editar/<int:codigo>', methods=['GET', 'POST'])
def editar_fornecedor(codigo):
    fornecedor = Fornecedor.query.get(codigo)
    if request.method == 'POST':
        fornecedor.fornecedor = request.form['fornecedor']
        fornecedor.telefone = request.form['telefone']
        fornecedor.endereco = request.form['endereco']
        fornecedor.situacao = bool(request.form.get('situacao'))
        fornecedor.email = request.form['email']
        db.commit()
        flash('Fornecedor atualizado com sucesso!', 'success')
        return redirect(url_for('fornecedor.listar_fornecedores'))
    return render_template('fornecedor/editar.html', fornecedor=fornecedor)

# Excluir fornecedor
@fornecedor_blueprint.route('/fornecedores/excluir/<int:codigo>', methods=['GET'])
def excluir_fornecedor(codigo):
    fornecedor = Fornecedor.query.get(codigo)
    db.delete(fornecedor)
    db.commit()
    flash('Fornecedor excluído com sucesso!', 'success')
    return redirect(url_for('fornecedor.listar_fornecedores'))
