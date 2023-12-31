import json
from flask import Blueprint, request
from dataclasses import asdict
from service.pessoa import ServicePessoa

pessoa = Blueprint('pessoa', __name__)


@pessoa.route("/api/pessoa/busca", methods=['GET'])
def busca_pessoa():
    '''Controlle para realizar as chamadas realizadas a pessoa'''

    data = request.get_json()
    id_pessoa = data["id_pessoa"]

    service = ServicePessoa()
    pessoa = service.BuscaPessoa(id_pessoa)

    if not pessoa:
        return (json.dumps(f"Pessoa não encontrada. ID {id_pessoa}"),
                404,
                {'ContentType': 'application/json'})

    return (json.dumps(asdict(pessoa)),
            200,
            {'ContentType': 'application/json'})
