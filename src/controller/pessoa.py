from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from src.service.pessoa import ServicePessoa


class PessoaRouter:
    '''Clase que define os endpoints do controller de pessoas'''
    def __init__(self, service_pessoa: ServicePessoa):
        self.router = APIRouter()
        self.service_pessoa = service_pessoa

        self.define_routes()

    def define_routes(self):
        @self.router.get("/busca")
        async def busca_pessoa(id_pessoa: str):
            '''Método que realiza a busca de uma pessoa a partir de um ID'''
            pessoa_retorno = self.service_pessoa.BuscaPessoa(id_pessoa)

            if not pessoa_retorno:
                return JSONResponse(
                    content=jsonable_encoder(f"Pessoa não encontrada. "
                                             f"ID: {id_pessoa}"),
                    status_code=status.HTTP_404_NOT_FOUND)

            return JSONResponse(content=jsonable_encoder(pessoa_retorno),
                                status_code=status.HTTP_200_OK)

        return self.router
