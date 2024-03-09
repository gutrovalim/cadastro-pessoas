import mysql.connector
from src.model.pessoa import Pessoa

QUERY_BUSCA_PESSOA = "SELECT * FROM cadastro_pessoa.pessoa WHERE ID_PES ="


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

        self.mycursor.execute(f"{QUERY_BUSCA_PESSOA}"
                              f" '{id_pessoa}'")
        query_result = self.mycursor.fetchone()

        if not query_result:
            return None

        pessoa = Pessoa(id_pessoa=query_result["ID_PES"],
                        nome_pessoa=query_result["NOM_PES"],
                        numero_documento_pessoa=query_result["NUM_DOCM_PES"],
                        numero_idade_pessoa=query_result["NUM_IDAE_PES"])

        return pessoa
