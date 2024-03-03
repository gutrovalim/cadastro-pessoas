# Micro serviço de cadastro de pessoas

Este Micro Serviço tem como objetivo Cadastrar uma Pessoa em um banco de dados. É possível armazenar dados de Email, Telefone, Endereço e Dados pessoais da pessoa.



## Arquitetura

![Arquitetura](https://github.com/gutrovalim/cadastro-pessoas/blob/develop/docs/desenho_arquitetura.png)

## Documentação da API

#### Retorna uma pessoa

```http
  GET /api/pessoa/busca
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `id_pessoa` | `string` | **Obrigatório**. A pessoa a ser buscada no banco de dados |

#### Retornos

#### HTTP 200
```
{
	"id_pessoa": "ac5f301ad681ee1c268e6bec9063c0620619f24c3a68160e6e0a3d43d4a4d2be",
	"nome_pessoa": "42972210808",
	"numero_documento_pessoa": "Gustavo Trovalim",
	"numero_idade_pessoa": 29
}
```

#### HTTP 404
```
"Pessoa nao encontrada. ID ac5f301ad681ee1c268e6bec9063c0620619f24c3a68160e6e0a3d43d4a4d2be"
```
