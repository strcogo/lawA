from flask import Blueprint, render_template, request, redirect, flash
from models import Produto, Fornecedor
from database import db

bp_produtos = Blueprint('produtos', __name__, template_folder="templates")

@bp_produtos.route("/")
def index():
    p = Produto.query.all()
    return render_template("produtos.html", dados=p)


@bp_produtos.route("/add")
def add():
    p = Produto.query.all()
    f = Fornecedor.query.all()
    return render_template("produtos_add.html", dados=p, fornecedores=f)


@bp_produtos.route("/save", methods=['POST'])
def save():
    nm_produto = request.form.get("nm_produto")
    preco = request.form.get("preco")
    id_fornecedor = request.form.get("id_fornecedor")

    fornecedor = Fornecedor.query.all()

    if nm_produto and preco and id_fornecedor:
        db_produto = Produto(nm_produto, preco, id_fornecedor)
        db.session.add(db_produto)
        db.session.commit()
        flash("Produto cadastrada!")
        return redirect("/produtos")
    else:
        flash("Preencha todos os campos!")
        return redirect("/produtos/add")
    

@bp_produtos.route("/remove/<int:id>")
def remove(id):
    p = Produto.query.get(id)
    try:
        db.session.delete(p)
        db.session.commit()
        flash("Produto removido!")
    except:
        flash("Produto Inválido!")
    return redirect("/produtos")


@bp_produtos.route("/edit/<int:id>")
def edit(id):
    p = Produto.query.get(id)
    f = Fornecedor.query.all()
    return render_template("produtos_edit.html", dados=p, fornecedores=f)


@bp_produtos.route("/edit-save", methods=['POST'])
def edit_save():
    nm_produto = request.form.get("nm_produto")
    preco = request.form.get("preco")
    id_fornecedor = request.form.get("id_fornecedor")
    id = request.form.get("id")
    if nm_produto and preco and id_fornecedor and id:
        p = Produto.query.get(id)
        p.nm_produto = nm_produto
        p.preco = preco
        p.id_fornecedor = id_fornecedor
        db.session.commit()
        flash("Dados atualizados!")
    else:
        flash("Preencha todos os campos!")
    return redirect("/produtos")