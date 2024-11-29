from database import db

class Fornecedor(db.Model):
    __tablename__ = 'tb_fornecedor'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    contato = db.Column(db.String(50))


    def __init__(self, nome, contato):
        self.nome = nome
        self.contato = contato


    def __repr__(self):
        return f"<Fornecedor {self.nome}>"
    

class Produto(db.Model):
    __tablename__ = 'tb_produto'
    id = db.Column(db.Integer, primary_key=True)
    nm_produto = db.Column(db.String(100))
    preco = db.Column(db.Float(10,2))
    id_fornecedor = db.Column(db.Integer, db.ForeignKey('tb_fornecedor.id'))

    fornecedor = db.relationship('Fornecedor', foreign_keys=id_fornecedor)


    def __init__(self, nm_produto, preco, id_fornecedor):
        self.nm_produto = nm_produto
        self.preco = preco
        self.id_fornecedor = id_fornecedor

    
    def __repr__(self):
        return f"<Produto {self.nm_produto} - {self.fornecedor.nome}>"