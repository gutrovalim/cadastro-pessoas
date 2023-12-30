from flask import Blueprint
import json

email = Blueprint('email', __name__)


@email.route("/api/email/cadastra", methods=['POST'])
def cadastra_email():
    return (json.dumps({'success': "Email cadastrado com sucesso"}),
            200,
            {'ContentType': 'application/json'})


@email.route("/api/email/atualiza", methods=['PUT'])
def atualiza_email():
    return (json.dumps({'success': "Email atualizado com sucesso"}),
            200,
            {'ContentType': 'application/json'})
