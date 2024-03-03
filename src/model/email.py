from dataclasses import dataclass


@dataclass
class Telefone:
    '''Classe que define os atributos de um Email'''
    id_email: str
    id_pessoa: str
    email: str
