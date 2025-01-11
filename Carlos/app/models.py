from .database import db

class Produtos(db.Model):
    id_produto = db.Column(db.Integer, primary_key=True)
    nm_produto = db.Column(db.String(100), nullable=False)
    img_url = db.Column(db.String, nullable=False)
    vl_item = db.Column(db.String(200))

    def __repr__(self):
        return f'<Produtos {self.nome}>'

class Usuarios(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(10), nullable=False, unique=True)
    nome_usuario = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(80),nullable=False)
    senha = db.Column(db.String(8), nullable=False)
    endereco = db.Column(db.String, nullable=False)
    cnpj = db.Column(db.String(8), nullable=False)

    def __repr__(self):
        return f'<Usuarios {self.usuario}>'