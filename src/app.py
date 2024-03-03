from fastapi import FastAPI
from src.controller.pessoa import PessoaRouter
from src.service.pessoa import ServicePessoa
from src.service.pessoa import ConectaPessoa

app = FastAPI()

# Database
conecta_pessoa = ConectaPessoa()

# Service
service_pessoa = ServicePessoa(conecta_pessoa)

# Controller
pessoa_router = PessoaRouter(service_pessoa)

app.include_router(
    pessoa_router.define_routes(),
    prefix="/api/pessoa",
    tags=["pessoa"]
)
