# Dicionário para armazenar os contatos
contatos = {}


def adicionar_contato():
    nome = input("digite o nome do contato: ")
    if nome in contatos:
        print("este contato já existe!")
    else:
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        favorito = input("Este contato é favorito? (s/n): ").lower() == 's'
        contatos[nome] = {
            "telefone": telefone,
            "email": email,
            "favorito": favorito
        }
        print("Contato adicionado com sucesso!")


def visualizar_contatos(is_favorite):
    if contatos == {}:
        print("nao existem contatos em sua lista")
    if (is_favorite == False):
        for nome, info in contatos.items():
            favorito = "s" if info["favorito"] else "n"
            print(
                f"nome: {nome}, telefone: {info['telefone']}, email: {info['email']}, favorito: {favorito}")
    else:
        print("Contatos Favoritos:")
        for nome, info in contatos.items():
            if info["favorito"]:
                print(
                    f"Nome: {nome}, Telefone: {info['telefone']}, Email: {info['email']}")


def editar_contato():
    nome = input("digite o nome do contato que deseja editar: ")
    if nome in contatos:
        telefone = input("digite o novo telefone do contato: ")
        email = input("digite o novo email do contato: ")
        favorito = input(
            "Este contato é favorito? (s/n): ").lower() == 's'
        contatos[nome] = {
            "telefone": telefone,
            "email": email,
            "favorito": favorito
        }
    else:
        print("contato nao encontrado!")


def marcar_desmarcar_favorito():
    nome = input(
        "digite o nome do contato para marcar/desmarcar como favorito: ")
    if nome in contatos:
        contatos[nome]["favorito"] = not contatos[nome]["favorito"]
        print("contato atualizado.")
    else:
        print("contato não encontrado!")


def apagar_contato():
    nome = input("digite o nome do contato que deseja apagar: ")
    if nome in contatos:
        del contatos[nome]
        print("contato apagado.")
    else:
        print("contato não encontrado!")


def popular_lista():
    global contatos
    if (contatos != {}):
        print("lista ja contem usuarios")
    else:
        contatos = {
            "Alice": {
                "telefone": "1234-5678",
                "email": "alice@dd.com",
                "favorito": True
            },
            "Bob": {
                "telefone": "8765-4321",
                "email": "bob@dd.com",
                "favorito": False
            },
            "Raul": {
                "telefone": "4445-2233",
                "email": "ral@dd.com",
                "favorito": False
            }
        }
        print("lista de contatos populada com sucesso.")


def menu():
    while True:
        print("\nmenu:")
        print("1. adicionar contato")
        print("2. visualizar contatos")
        print("3. editar contato")
        print("4. marcar/Desmarcar como favorito")
        print("5. ver contatos favoritos")
        print("6. apagar contato")
        print("7. sair")
        print("8. popular lista de contato")

        opcao = input("escolha uma opção: ")

        if opcao == '1':
            adicionar_contato()
        elif opcao == '2':
            visualizar_contatos(False)
        elif opcao == '3':
            editar_contato()
        elif opcao == '4':
            marcar_desmarcar_favorito()
        elif opcao == '5':
            visualizar_contatos(True)
        elif opcao == '6':
            apagar_contato()
        elif opcao == '8':
            popular_lista()
        elif opcao == '7':
            print("saindo do programa...")
            break
        else:
            print("opcao inválida!")


menu()
