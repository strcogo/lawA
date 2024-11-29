from flask import Blueprint, render_template, request, redirect, flash
from models import Fornecedor
from database import db

bp_fornecedores = Blueprint('fornecedores', __name__, template_folder="templates")

@bp_fornecedores.route("/")
def index():
    p = Fornecedor.query.all()
    return render_template("fornecedores.html", dados=p)


@bp_fornecedores.route("/add")
def add():
    return render_template("fornecedores_add.html")


@bp_fornecedores.route("/save", methods=['POST'])
def save():
    nome = request.form.get("nome")
    contato = request.form.get("contato")
    if nome and contato:
        db_fornecedor = Fornecedor(nome, contato)
        db.session.add(db_fornecedor)
        db.session.commit()
        flash("Fornecedor cadastrado!")
        return redirect("/fornecedores")
    else:
        flash("Preencha todos os campos!")
        return redirect("/fornecedores/add")
    

@bp_fornecedores.route("/remove/<int:id>")
def remove(id):
    p = Fornecedor.query.get(id)
    try:
        db.session.delete(p)
        db.session.commit()
        flash("Fornecedor removido!")
    except:
        flash("Fornecedor Inválido!")
    return redirect("/fornecedores")


@bp_fornecedores.route("/edit/<int:id>")
def edit(id):
    p = Fornecedor.query.get(id)
    return render_template("fornecedores_edit.html", dados=p)


@bp_fornecedores.route("/edit-save", methods=['POST'])
def edit_save():
    nome = request.form.get("nome")
    contato = request.form.get("contato")
    id = request.form.get("id")
    if nome and contato and id:
        p = Fornecedor.query.get(id)
        p.nome = nome
        p.contato = contato
        db.session.commit()
        flash("Dados atualizados!")
    else:
        flash("Preencha todos os campos!")
    return redirect("/fornecedores")