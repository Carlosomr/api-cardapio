from flask import current_app as app
from flask import jsonify, request, session
from flask_cors import CORS, cross_origin
from .models import Produtos, Usuarios
from .database import db
import bcrypt

CORS(app)  # Habilita CORS para toda a aplicação

@app.route('/', methods=['GET'])
def get_login():
    login = Usuarios.query.all()
    return jsonify([
        {
            "id_usuario": user.id_usuario,
            "usuario": user.usuario,
            "nome_usuario": user.nome_usuario,
            "email": user.email,
            "senha": user.senha,
            "endereco": user.endereco,
            "cnpj": user.cnpj
        } for user in login
    ])

@app.route('/cadastro', methods=['POST'])
@cross_origin()  # Adiciona @cross_origin() para permitir CORS nesta rota específica
def add_usuarios():
    data = request.get_json()
    
    # Verifica se o usuário já existe
    usuario_existente = Usuarios.query.filter_by(usuario=data['usuario']).first()
    if usuario_existente:
        return jsonify({"error": "Usuário já existe"}), 400

    # Extraia a senha do JSON enviado na solicitação
    senha = data.get('senha')
    
    if not senha:
        return jsonify({"error": "Senha é obrigatória"}), 400
    
    # Gerar o hash da senha
    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
    senha_hash_str = senha_hash.decode('utf-8')  # Converte o hash para string

    add_user = Usuarios(
        usuario=data['usuario'],
        nome_usuario=data['nome_usuario'],
        email=data['email'],
        senha=senha_hash_str,  # Armazena o hash da senha como string
        endereco=data['endereco'],  # Novo campo
        cnpj=data['cnpj']  # Novo campo
    )
    db.session.add(add_user)
    db.session.commit()
    return jsonify({
        "id_usuario": add_user.id_usuario,
        "usuario": add_user.usuario,
        "nome_usuario": add_user.nome_usuario,
        "email": add_user.email,
        "senha": add_user.senha,
        "endereco": add_user.endereco,  # Novo campo
        "cnpj": add_user.cnpj  # Novo campo
    }), 201

@app.route('/login', methods=['POST'])
@cross_origin()  # Adiciona @cross_origin() para permitir CORS nesta rota específica
def login():
    data = request.get_json()
    usuario = data.get('usuario')
    senha = data.get('senha')

    user = Usuarios.query.filter_by(usuario=usuario).first()

    if user and bcrypt.checkpw(senha.encode('utf-8'), user.senha.encode('utf-8')):
        session['user_id'] = user.id_usuario  # Armazena o ID do usuário na sessão
        return jsonify({"message": "Login bem-sucedido!"}), 200
    else:
        return jsonify({"message": "Usuário ou senha inválidos!"}), 401

@app.route('/itens', methods=['GET'])
@cross_origin()  # Adiciona @cross_origin() para permitir CORS nesta rota específica
def get_produtos():
    produtos = Produtos.query.all()
    return jsonify([{"id_produto": prod.id_produto, "nm_produto": prod.nm_produto, "img_url": prod.img_url, "vl_item": prod.vl_item} for prod in produtos])

@app.route('/cadastrar/itens', methods=['POST'])
@cross_origin()  # Adiciona @cross_origin() para permitir CORS nesta rota específica
def add_itens():
    data = request.get_json()
    novo_produto = Produtos(
        nm_produto=data['nm_produto'],
        img_url=data['img_url'],
        vl_item=data.get('vl_item')
    )
    db.session.add(novo_produto)
    db.session.commit()
    return jsonify({"id_produto": novo_produto.id_produto, "nm_produto": novo_produto.nm_produto, "img_url": novo_produto.img_url, "vl_item": novo_produto.vl_item}), 201

@app.route('/cadastrar/itens/<int:id_produto>', methods=['GET'])
@cross_origin()  # Adiciona @cross_origin() para permitir CORS nesta rota específica
def get_produtos_id(id_produto):
    produto = Produtos.query.get_or_404(id_produto)
    return jsonify({"id_produto": produto.id_produto, "nm_produto": produto.nm_produto, "img_url": produto.img_url, "vl_item": produto.vl_item})
