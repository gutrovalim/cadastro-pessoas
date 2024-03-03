import pytest
from unittest.mock import MagicMock
from src.service.pessoa import ServicePessoa
from src.model.pessoa import Pessoa


@pytest.fixture
def mock_service_pessoa_200():
    mock_service = MagicMock(spec=ServicePessoa)
    mock_service.BuscaPessoa.\
        return_value = Pessoa(id_pessoa="1",
                              nome_pessoa="John Doe",
                              numero_documento_pessoa="123",
                              numero_idade_pessoa=30)
    return mock_service


@pytest.fixture
def mock_service_pessoa_404():
    mock_service = MagicMock(spec=ServicePessoa)
    mock_service.BuscaPessoa.return_value = None
    return mock_service
