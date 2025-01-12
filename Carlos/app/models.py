from .database import db

class Produtos(db.Model):
    id_produto = db.Column(db.Integer, primary_key=True)
    nm_produto = db.Column(db.String(100), nullable=False)
    img_url = db.Column(db.String, nullable=False)
    vl_item = db.Column(db.String(200))

    def __repr__(self):
        return f'<Produtos {self.nm_produto}>'

class Usuarios(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), nullable=False, unique=True)  # Aumentado para 50 caracteres
    nome_usuario = db.Column(db.String(80), nullable=False)          # Aumentado para 80 caracteres
    email = db.Column(db.String(120), nullable=False)                # Aumentado para 120 caracteres
    senha = db.Column(db.String(255), nullable=False)                # Aumentado para 255 caracteres
    endereco = db.Column(db.String(255), nullable=False)             # Aumentado para 255 caracteres
    cnpj = db.Column(db.String(20), nullable=False, unique=True)     # Aumentado para 20 caracteres

    def __repr__(self):
        return f'<Usuarios {self.usuario}>'
