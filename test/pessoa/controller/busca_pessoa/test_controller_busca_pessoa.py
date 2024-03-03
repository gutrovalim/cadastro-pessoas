
from fastapi import FastAPI
from fastapi.testclient import TestClient
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

    assert response.status_code == 200

    expected_data = {
        "id_pessoa": "1",
        "nome_pessoa": "John Doe",
        "numero_documento_pessoa": "123",
        "numero_idade_pessoa": 30
    }
    assert response.json() == expected_data


def test_busca_pessoa_404(mock_service_pessoa_404):
    router = PessoaRouter(mock_service_pessoa_404)
    client = client_test(router)
    response = client.get("/api/pessoa/busca", params={"id_pessoa": "2"})

    assert response.status_code == 404
