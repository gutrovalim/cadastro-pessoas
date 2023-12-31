from dataclasses import dataclass


@dataclass
class Endereco:
    '''Classe que define um Endereco'''
    id_endereco: str
    id_pessoa: str
    nome_logradouro: str
    numero_logradouro: int
    complemento_logradouro: str
    nome_bairro: str
    nome_cidade: str
    nome_pais: str
    codigo_postal: str
