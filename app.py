from flask import Flask, render_template, request, flash, redirect, Blueprint
app = Flask(__name__)
app.config['SECRET_KEY'] = 'f77a90697fc48d53e3b05a15bd8c214697f139351362b3febaa190ccd4a3d4e2'

conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/lalau_db"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from database import db
from flask_migrate import Migrate
from models import Fornecedor, Produto

db.init_app(app)
migrate = Migrate(app, db)

from modules.fornecedores.fornecedores import bp_fornecedores
app.register_blueprint(bp_fornecedores, url_prefix='/fornecedores')

from modules.produtos.produtos import bp_produtos
app.register_blueprint(bp_produtos, url_prefix='/produtos')

@app.route("/")
def index():
    return render_template("index.html")