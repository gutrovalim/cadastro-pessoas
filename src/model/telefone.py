from dataclasses import dataclass


@dataclass
class Telefone:
    '''Classe que define os atributos de um Telefone'''
    id_telefone: str
    id_pessoa: str
    codigo_ddi: str
    codigo_ddd: str
    numero_telefone: int
    idto_categoria_telefone: str
