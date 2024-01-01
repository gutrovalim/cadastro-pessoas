import json
from unittest.mock import MagicMock
from flask import Flask
from src.controller.pessoa import busca_pessoa
from src.service.pessoa import ServicePessoa
from src.model.pessoa import Pessoa

app = Flask(__name__)


def test_busca_pessoa_existente_na_base():
    '''Teste que valida a execucao com sucesso ao busca uma pessoa'''
    service = ServicePessoa()
    service.BuscaPessoa = MagicMock()
    service.BuscaPessoa.return_value = Pessoa("teste",
                                              "795661544",
                                              "teste",
                                              40)

    with app.test_request_context("/api/pessoa/busca",
                                  json={"id_pessoa": "teste"}):
        resposta = busca_pessoa(service)

    result = json.loads(resposta.data)

    assert result["id_pessoa"] == "teste"


def test_busca_pessoa_nao_existente_na_base():
    '''Teste que valida a execucao com sucesso ao busca uma pessoa'''
    service = ServicePessoa()
    service.BuscaPessoa = MagicMock()
    service.BuscaPessoa.return_value = None

    with app.test_request_context("/api/pessoa/busca",
                                  json={"id_pessoa": "teste"}):
        resposta = busca_pessoa(service)

    result = json.loads(resposta.data)

    assert result == "Pessoa nao encontrada. ID teste"
