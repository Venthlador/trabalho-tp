import os
import json

nome_arquivo = 'animes.json'

def lerArquivo() -> list:
    arq = open(nome_arquivo, 'r', encoding='utf-8')
    data = arq.read()
 
    return json.loads(data)


def salvarArquivo(animes: list):
    arq = open(nome_arquivo, 'w+', encoding='utf-8')
    data = json.dumps(animes, indent=4)
    arq.write(data)
    arq.close()

def cadastrarAnime() -> dict:
    anime = {}
    anime['nome'] = str(input('Nome do Anime: '))
    anime['episodios'] = str(input('Numero de Episodios: '))
    anime['genero'] = str(input('Genero: '))
    anime['data_de_lancamento'] = int(input('Data de Lancamento: '))
    anime['autor'] = str(input('Autor: '))
    anime["classificacao"] = str(input('Classificacao: '))
    anime['id'] = int(input('ID: '))
    
    animes = lerArquivo()
    animes.append(anime)
    salvarArquivo(animes)

def menu():
    
    print(10 * '-=-')
    print('1 - Cadastrar anime')
    print('2 - Listar animes')
    print('3 - Encontrar Anime')
    print('4 - alterar Anime')
    print('5 - deletar anime')
    print('6 - Sair')
    print(10 * '-=-')
    return int(input('Escolha uma opção: '))


def mostrarAnimes():
    
    print(10 * '-=-')
    animes = lerArquivo()
    for anime in animes:
        print(f'Nome: {anime["nome"]}')
        print(f'Episodios: {anime["episodios"]}')
        print(f'Genero: {anime["genero"]}')
        print(f'Data de Lancamento: {anime["data_de_lancamento"]}')
        print(f'Autor: {anime["autor"]}')
        print(f'Classificacao: {anime["classificacao"]}')
        print(f'ID: {anime["id"]}')
        print(10 * '-=-')
    input('Pressione ENTER para continuar...')

def encontrarAnime():

    animes = lerArquivo()
    pede_id = int(input("Insira o id do anime que deseja pesquisar: "))
    for anime in animes:
        if anime["id"] == pede_id:
            print(10 * '-=-')
            print(f'Nome: {anime["nome"]}')
            print(f'Episodios: {anime["episodios"]}')
            print(f'Genero: {anime["genero"]}')
            print(f'Data de Lancamento: {anime["data_de_lancamento"]}')
            print(f'Autor: {anime["autor"]}')
            print(f'Classificacao: {anime["classificacao"]}')
            print(f'ID: {anime["id"]}')
            print(10 * '-=-')
            input('Pressione ENTER para continuar...')

def deletarAnime():
    animes = lerArquivo()
    pede_id = int(input("Ensira o ID: "))
    for anime in animes:
        if anime["id"] == pede_id:
            index_anime = animes.index(anime)
            animes.pop(index_anime)
            print ("Anime deletado")

    salvarArquivo(animes)

# Index é o valor a ser pesquisado na lista.

def alterarAnime():
    animes = lerArquivo()
    pede_id = int(input("Insira o id do anime que deseja alterar: "))
    for anime in animes:
        if anime["id"] == pede_id:
            alterar_anime = input("Deseja Alterar o nome?: ").upper()
            if alterar_anime == "S":
                anime["nome"] = input("Nome do anime: ")
            
            alterar_anime = input("Deseja alterar o numero de episodios? ").upper()
            if alterar_anime == "S":
                anime["episodios"] = input("Numero de episodios: ")
            
            alterar_anime = input("Deseja alterar o genero do anime?: ").upper()
            if alterar_anime == "S":
                anime["genero"] = input("Genero do anime: ")
            
            alterar_anime = input("Deseja alterar o ano de lancamento? ").upper()
            if alterar_anime == "S":
                anime["data_de_lancamento"] = input("Ano de lancamento: ")
            
            alterar_anime = input("Deseja alterar a classificacao?: ").upper()
            if alterar_anime == "S":
                anime["classificacao"] = input("Classificacao do anime: ")
            
            alterar_anime = input("Deseja Alterar o ID?: ").upper()
            if alterar_anime == "S":
                anime["id"] = input("ID: ")
            
    salvarArquivo(animes)