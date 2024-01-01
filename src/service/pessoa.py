from src.model.pessoa import Pessoa
from src.database.pessoa import ConectaPessoa


class ServicePessoa():
    '''Classe que define as funcionalidades de cadastro de uma pessoa'''

    def BuscaPessoa(id_pessoa, conecta=ConectaPessoa) -> Pessoa:
        '''Servico que busca pessoa pelo Id'''
        return conecta.BuscaPessoa(id_pessoa)
