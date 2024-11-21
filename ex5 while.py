print('Escolha uma opção abaixo:')
print('a - aceitar')
print('r - recusar')
print('s - sair')
opcao = input('opcão escolhida: ')

while (opcao != 's'):
    if opcao=='a':
        print("ACEITOU")
    elif opcao == 'r':
        print("RECUSOU")
    else:
        print('OPCAO INVALIDA')

    print('Escolha uma opção abaixo:')
    print('a - aceitar')
    print('r - recusar')
    print('s - sair')
    opcao = input('opcão escolhida: ')

print('FIM')