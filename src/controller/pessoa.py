from flask import Blueprint
import json

pessoa = Blueprint('pessoa', __name__)


@pessoa.route("/api/pessoa/cadastra", methods=['POST'])
def cadastra_pessoa():
    return (json.dumps({'success': "Pessoa cadastrada com sucesso"}),
            200,
            {'ContentType': 'application/json'})


@pessoa.route("/api/pessoa/atualiza", methods=['PUT'])
def atualiza_pessoa():
    return (json.dumps({'success': "Cadastro da pessoa"
                        " atualizado com sucesso"}),
            200,
            {'ContentType': 'application/json'})
