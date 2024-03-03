import mysql.connector
from src.model.pessoa import Pessoa


class ConectaPessoa():
    '''Classe de conexao com o banco de dados para uma pessoa'''

    def __init__(self) -> None:
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dbadmin"
            )

        self.mycursor = self.mydb.cursor(dictionary=True)

    def BuscaPessoa(self, id_pessoa) -> Pessoa:
        '''Metodo que busca a pessoa no banco de dados'''

        self.mycursor.execute("SELECT * FROM cadastro_pessoa.pessoa"
                              f" WHERE ID_PES = '{id_pessoa}'")
        linhas = self.mycursor.fetchall()

        if not linhas:
            return None

        for linha in linhas:
            pessoa = Pessoa(linha["ID_PES"],
                            linha["NOM_PES"],
                            linha["NUM_DOCM_PES"],
                            linha["NUM_IDAE_PES"])

        return pessoa
