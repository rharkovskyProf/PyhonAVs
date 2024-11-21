def menu():
    print('Escolha uma opção abaixo:')
    print('a - aceitar')
    print('r - recusar')
    print('s - sair')
    op = input('opcão escolhida: ')
    return  op


# MAIN
opcao = menu()
while True:
    if opcao == 'a':
        print("ACEITOU")
    elif opcao == 'r':
        print("RECUSOU")
    elif opcao == 's':
        break
    else:
        print('OPCAO INVALIDA')

    opcao=menu()

print('FIM')