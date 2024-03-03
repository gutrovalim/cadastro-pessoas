import json
from fastapi import APIRouter, Response
from dataclasses import asdict
from src.service.pessoa import ServicePessoa


class PessoaRouter:
    def __init__(self, service_pessoa: ServicePessoa):
        self.router = APIRouter()
        self.service_pessoa = service_pessoa

        self.define_routes()

    def define_routes(self):
        @self.router.get("/busca")
        async def busca_pessoa(id_pessoa: str):
            '''Controller para realizar as chamadas realizadas a pessoa'''
            pessoa_retorno = self.service_pessoa.BuscaPessoa(id_pessoa)

            if not pessoa_retorno:
                return Response(
                    content=json.dumps(
                        f"Pessoa nao encontrada. ID {id_pessoa}"
                        ),
                    status_code=404,
                    media_type='application/json'
                )

            return Response(
                content=json.dumps(asdict(pessoa_retorno)),
                status_code=200,
                media_type='application/json'
            )

        return self.router
