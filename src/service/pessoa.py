from src.model.pessoa import Pessoa
from src.database.pessoa import ConectaPessoa


class ServicePessoa():
    '''Classe que define as funcionalidades de cadastro de uma pessoa'''

    def __init__(self,  conecta_pessoa: ConectaPessoa):
        self.conecta_pessoa = conecta_pessoa

    def BuscaPessoa(self, id_pessoa) -> Pessoa:
        '''Servico que busca pessoa pelo Id'''
        return self.conecta_pessoa.BuscaPessoa(id_pessoa)
