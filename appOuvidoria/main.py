reclamacoes = []
sugestoes = []
elogios = []

while True:

    print("Lista de serviços:\n\n1) Enviar uma reclamação.\n2) Enviar uma sugestão.\n3) Enviar um elogio.\n4) Sair do sistema.\n")
    servico = input("Escolha um serviço: ")

    if not servico.isdigit():
        print("\nServiço inválido. Tente novamente!\n")
        continue

    servico = int(servico)

    if servico == 1:
        # Trabalha com a lista de reclamações:
        while True:
            print("Lista de serviços:\n\n1) Listar as Manifestações.\n2) Criar uma nova Manifestação.\n3) Exibir quantidade de manifestações.\n4) Pesquisar uma manifestação por código.\n5) Sair do serviço.\n")

            opcao = input("Informe sua opção: ")

            if not opcao.isdigit():
                print("\nServiço inválido. Tente novamente!\n")
                continue

            opcao = int(opcao)

            if opcao == 1:
                print("Listar as Manifestações")
            elif opcao == 2:
                print("Criar uma nova Manifestação")
            elif opcao == 3:
                print("Exibir quantidade de manifestações")
            elif opcao == 4:
                print("Pesquisar uma manifestação por código")
            elif opcao == 5:
                break
            else:
                print("Opção inválida. Tente novamente!")

    elif servico == 2:

        # Trabalha com a lista de sugestões:
        while True:
            print("Lista de serviços:\n\n1) Listar as Manifestações.\n2) Criar uma nova Manifestação.\n3) Exibir quantidade de manifestações.\n4) Pesquisar uma manifestação por código.\n5) Sair do serviço.\n")

            opcao = int(input("Informe sua opção: "))

            if opcao == 1:
                print("Listar as Manifestações")
            elif opcao == 2:
                print("Criar uma nova Manifestação")
            elif opcao == 3:
                print("Exibir quantidade de manifestações")
            elif opcao == 4:
                print("Pesquisar uma manifestação por código")
            elif opcao == 5:
                break
            else:
                print("Opção inválida. Tente novamente!")

    elif servico == 3:

        # Trabalha com a lista de elogios:
        while True:
            print("Lista de serviços:\n\n1) Listar as Manifestações.\n2) Criar uma nova Manifestação.\n3) Exibir quantidade de manifestações.\n4) Pesquisar uma manifestação por código.\n5) Sair do serviço.\n")

            opcao = int(input("Informe sua opção: "))

            if opcao == 1:
                print("Listar as Manifestações")
            elif opcao == 2:
                print("Criar uma nova Manifestação")
            elif opcao == 3:
                print("Exibir quantidade de manifestações")
            elif opcao == 4:
                print("Pesquisar uma manifestação por código")
            elif opcao == 5:
                break
            else:
                print("Opção inválida. Tente novamente!")

    elif servico == 4:
        break
    else:
        print("\nServiço inválido. Tente novamente!\n")
print("Obrigado pelo seu feedback!")