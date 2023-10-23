import json

def adicionar_item(banco_de_dados, chave, valor):
    banco_de_dados[chave] = valor
    print("Item adicionado com sucesso!")

def remover_item(banco_de_dados, chave):
    if chave in banco_de_dados:
        del banco_de_dados[chave]
        print("Item removido com sucesso!")
    else:
        print("Item não encontrado!")

def buscar_item(banco_de_dados, chave):
    if chave in banco_de_dados:
        print(f"Resultado da busca: {banco_de_dados[chave]}")
    else:
        print("Item não encontrado!")

def exportar_banco_de_dados(banco_de_dados, nome_arquivo):
    with open(nome_arquivo, 'w') as file:
        json.dump(banco_de_dados, file)
    print(f"Banco de dados exportado para {nome_arquivo} com sucesso!")

def carregar_banco_de_dados(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.decoder.JSONDecodeError:
        return {}

nome_arquivo = "banco_de_dados.json"
banco_de_dados = carregar_banco_de_dados(nome_arquivo)

while True:
    print("\nBanco de Dados Simples no Terminal")
    print("1. Adicionar Item")
    print("2. Remover Item")
    print("3. Buscar Item")
    print("4. Exportar Banco de Dados")
    print("5. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        chave = input("Digite a chave do item: ")
        valor = input("Digite o valor do item: ")
        adicionar_item(banco_de_dados, chave, valor)
    elif escolha == "2":
        chave = input("Digite a chave do item a ser removido: ")
        remover_item(banco_de_dados, chave)
    elif escolha == "3":
        chave = input("Digite a chave do item a ser buscado: ")
        buscar_item(banco_de_dados, chave)
    elif escolha == "4":
        exportar_banco_de_dados(banco_de_dados, nome_arquivo)
    elif escolha == "5":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")