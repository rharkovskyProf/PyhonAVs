while True:
    print('Escolha uma opção abaixo:')
    print('a - aceitar')
    print('r - recusar')
    print('s - sair')
    opcao = input('opcão escolhida: ')

    if opcao =='a':
        print("ACEITOU")
    elif opcao == 'r':
        print("RECUSOU")
    elif opcao == 's':
        break
    else:
        print('OPCAO INVALIDA')


print('FIM')