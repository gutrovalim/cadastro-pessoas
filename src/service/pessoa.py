from model.pessoa import Pessoa
from database.pessoa import ConectaPessoa


class ServicePessoa():
    '''Classe que define as funcionalidades de cadastro de uma pessoa'''

    def BuscaPessoa(self, id_pessoa) -> Pessoa:
        '''Servico que busca pessoa pelo Id'''
        database = ConectaPessoa()

        return database.BuscaPessoa(id_pessoa)
