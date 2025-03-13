listaReclamacoes = []
listaSugestoes = []
listaElogios = []

while True:

    print("\n============================")
    print("  LISTA DE MANIFESTAÇÕES  ")
    print("============================\n")
    print("1) Enviar uma reclamação")
    print("2) Enviar uma sugestão")
    print("3) Enviar um elogio")
    print("4) Sair do sistema\n")

    servico = input("Escolha um serviço: ")

    if not servico.isdigit():
        print("\n⚠️ Serviço inválido. Tente novamente!\n")
        continue

    servico = int(servico)

    if servico == 1:
        while True:
            print("\n============================")
            print("       RECLAMAÇÕES         ")
            print("============================\n")
            print("1) Listar as reclamações")
            print("2) Criar uma nova reclamação")
            print("3) Exibir quantidade de reclamações")
            print("4) Pesquisar uma reclamação por código")
            print("5) Sair do serviço\n")

            opcao = input("Informe sua opção: ")

            if not opcao.isdigit():
                print("\n⚠️ Opção inválida. Tente novamente!\n")
                continue

            opcao = int(opcao)

            if opcao == 1:
                if len(listaReclamacoes) < 1:
                    print("\n❌ Não há reclamações cadastradas.\n")
                else:
                    print("\nLista de reclamações:")
                    for num in range(len(listaReclamacoes)):
                        print(f"Reclamação {num+1}) {listaReclamacoes[num]}")
                    print()

            elif opcao == 2:
                novaManifestacao = input("\nDescreva sua nova reclamação: ")

                if len(novaManifestacao) < 1:
                    print("\n⚠️ Informe uma reclamação válida!\n")
                else:
                    listaReclamacoes.append(novaManifestacao)
                    print(f"\n✅ Reclamação cadastrada com sucesso! O seu código é {len(listaReclamacoes)}\n")

            elif opcao == 3:
                print(f"\n📊 Total de reclamações cadastradas: {len(listaReclamacoes)}\n")

            elif opcao == 4:
                codigoManifestacao = input("\nInforme o código da reclamação: ")

                if not codigoManifestacao.isdigit():
                    print("\n⚠️ Informe um código válido!\n")
                    continue

                codigoManifestacao = int(codigoManifestacao)

                if 1 <= codigoManifestacao <= len(listaReclamacoes):
                    print(f"\n🔎 Reclamação {codigoManifestacao}: {listaReclamacoes[codigoManifestacao-1]}\n")
                else:
                    print("\n❌ Reclamação não encontrada.\n")

            elif opcao == 5:
                break
            else:
                print("\n⚠️ Opção inválida. Tente novamente!\n")

    elif servico == 2:
        while True:
            print("\n============================")
            print("        SUGESTÕES         ")
            print("============================\n")
            print("1) Listar as sugestões")
            print("2) Criar uma nova sugestão")
            print("3) Exibir quantidade de sugestões")
            print("4) Pesquisar uma sugestão por código")
            print("5) Sair do serviço\n")

            opcao = input("Informe sua opção: ")

            if not opcao.isdigit():
                print("\n⚠️ Opção inválida. Tente novamente!\n")
                continue

            opcao = int(opcao)

            if opcao == 1:
                if len(listaSugestoes) < 1:
                    print("\n❌ Não há sugestões cadastradas.\n")
                else:
                    print("\nLista de sugestões:")
                    for num in range(len(listaSugestoes)):
                        print(f"Sugestão {num+1}) {listaSugestoes[num]}")
                    print()

            elif opcao == 2:
                novaManifestacao = input("\nDescreva sua nova sugestão: ")

                if len(novaManifestacao) < 1:
                    print("\n⚠️ Informe uma sugestão válida!\n")
                else:
                    listaSugestoes.append(novaManifestacao)
                    print(f"\n✅ Sugestão cadastrada com sucesso! O seu código é {len(listaSugestoes)}\n")

            elif opcao == 3:
                print(f"\n📊 Total de sugestões cadastradas: {len(listaSugestoes)}\n")

            elif opcao == 4:
                codigoManifestacao = input("\nInforme o código da sugestão: ")

                if not codigoManifestacao.isdigit():
                    print("\n⚠️ Informe um código válido!\n")
                    continue

                codigoManifestacao = int(codigoManifestacao)

                if 1 <= codigoManifestacao <= len(listaSugestoes):
                    print(f"\n🔎 Sugestão {codigoManifestacao}: {listaSugestoes[codigoManifestacao-1]}\n")
                else:
                    print("\n❌ Sugestão não encontrada.\n")

            elif opcao == 5:
                break
            else:
                print("\n⚠️ Opção inválida. Tente novamente!\n")

    elif servico == 3:
        while True:
            print("\n============================")
            print("         ELOGIOS          ")
            print("============================\n")
            print("1) Listar os elogios")
            print("2) Criar um novo elogio")
            print("3) Exibir quantidade de elogios")
            print("4) Pesquisar um elogio por código")
            print("5) Sair do serviço\n")

            opcao = input("Informe sua opção: ")

            if not opcao.isdigit():
                print("\n⚠️ Opção inválida. Tente novamente!\n")
                continue

            opcao = int(opcao)

            if opcao == 1:
                if len(listaElogios) < 1:
                    print("\n❌ Não há elogios cadastrados.\n")
                else:
                    print("\nLista de elogios:")
                    for num in range(len(listaElogios)):
                        print(f"Elogio {num+1}) {listaElogios[num]}")
                    print()

            elif opcao == 2:
                novaManifestacao = input("\nDescreva seu novo elogio: ")

                if len(novaManifestacao) < 1:
                    print("\n⚠️ Informe um elogio válido!\n")
                else:
                    listaElogios.append(novaManifestacao)
                    print(f"\n✅ Elogio cadastrado com sucesso! O seu código é {len(listaElogios)}\n")

            elif opcao == 3:
                print(f"\n📊 Total de elogios cadastrados: {len(listaElogios)}\n")

            elif opcao == 4:
                codigoManifestacao = input("\nInforme o código do elogio: ")

                if not codigoManifestacao.isdigit():
                    print("\n⚠️ Informe um código válido!\n")
                    continue

                codigoManifestacao = int(codigoManifestacao)

                if 1 <= codigoManifestacao <= len(listaElogios):
                    print(f"\n🔎 Elogio {codigoManifestacao}: {listaElogios[codigoManifestacao-1]}\n")
                else:
                    print("\n❌ Elogio não encontrado.\n")

            elif opcao == 5:
                break
            else:
                print("\n⚠️ Opção inválida. Tente novamente!\n")

    elif servico == 4:
        print("\n✅ Obrigado pelo seu feedback! Saindo do sistema...\n")
        break
    else:
        print("\n⚠️ Opção inválida. Tente novamente!\n")