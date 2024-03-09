from pydantic import BaseModel


class Pessoa(BaseModel):
    '''Classe que define os atributos de uma Pessoa'''
    id_pessoa: str
    nome_pessoa: str
    numero_documento_pessoa: str
    numero_idade_pessoa: int
