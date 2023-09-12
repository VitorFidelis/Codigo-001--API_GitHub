# Consumindo a API do Github em Python
import requests
import json


class RepositoriosGitHub():
    def __init__(self, usuario):
        self.usuario = usuario

    def requisicao_api(sef):
        retorno = requests.get(
            f"https://api.github.com/users/{sef.usuario}/repos")
        if retorno.status_code == 200:
            return retorno.json()
        else:
            raise Exception('Não doi possivel retornar esse repositório')
        
    def show_repositorio(self):
        dados_api = self.requisicao_api()
        if type(dados_api) is not int:
            for i in range(len(dados_api)):
                print(dados_api[i]['name'])
        else:
            print(dados_api)

repositorios_list = RepositoriosGitHub('username do repositório')
repositorios_list.show_repositorio()
