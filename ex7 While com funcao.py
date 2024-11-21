            def menu():
    print('Escolha uma opção abaixo:')
    print('a - aceitar')
    print('r - recusar')
    print('s - sair')


# MAIN
menu()
opcao = input('opcão escolhida: ')

while True:
    if opcao=='a':
        print("ACEITOU")
    elif opcao == 'r':
        print("RECUSOU")
    elif opcao == 's':
        break
    else:
        print('OPCAO INVALIDA')

    menu()
    opcao = input('opcão escolhida: ')

print('FIM')