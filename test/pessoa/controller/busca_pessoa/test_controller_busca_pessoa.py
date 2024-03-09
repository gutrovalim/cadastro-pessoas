
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from src.model.pessoa import Pessoa
from src.controller.pessoa import PessoaRouter


def client_test(router):
    app = FastAPI()
    app.include_router(router.router,
                       prefix="/api/pessoa",
                       tags=["pessoa"])

    return TestClient(app)


def test_busca_pessoa_200(mock_service_pessoa_200):
    router = PessoaRouter(mock_service_pessoa_200)
    client = client_test(router)
    response = client.get("/api/pessoa/busca", params={"id_pessoa": "1"})

    expected_data = Pessoa(id_pessoa="1",
                           nome_pessoa="John Doe",
                           numero_documento_pessoa="123",
                           numero_idade_pessoa=30)

    expected_response = JSONResponse(content=jsonable_encoder(expected_data),
                                     status_code=status.HTTP_200_OK)

    assert response.status_code == 200
    assert response.content == expected_response.body


def test_busca_pessoa_404(mock_service_pessoa_404):
    router = PessoaRouter(mock_service_pessoa_404)
    client = client_test(router)
    response = client.get("/api/pessoa/busca", params={"id_pessoa": "2"})

    assert response.status_code == 404
