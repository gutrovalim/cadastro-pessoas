import json
from flask import Blueprint, request, Response
from dataclasses import asdict
from src.service.pessoa import ServicePessoa

pessoa = Blueprint('pessoa', __name__)


@pessoa.route("/api/pessoa/busca", methods=['GET'])
def busca_pessoa(service=ServicePessoa):
    '''Controlle para realizar as chamadas realizadas a pessoa'''

    data = request.get_json()
    id_pessoa = data["id_pessoa"]

    pessoa_retorno = service.BuscaPessoa(id_pessoa)

    if not pessoa_retorno:
        return Response(
            response=json.dumps(f"Pessoa não encontrada. ID {id_pessoa}"),
            status=404,
            mimetype='application/json'
        )

    return Response(
        response=json.dumps(asdict(pessoa_retorno)),
        status=200,
        mimetype='application/json'
    )
