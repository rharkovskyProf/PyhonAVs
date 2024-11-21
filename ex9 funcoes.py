def menu():
    print('Escolha uma opção abaixo:')
    print('1 - somar')
    print('2 - subtrair')
    print('3 - mutiplicar')
    print('4 - dividir')
    print('s - sair')
    op = input('opcão escolhida: ')
    return  op
def soma():
    res = numero1 + numero2
    return res
def subtrai():
    res = numero1 - numero2
    return res
def multiplica():
    res = numero1 * numero2
    return res
def divide():
    res = numero1 / numero2
    return res

# MAIN
while True:
    opcao = menu()
    if opcao == 's':
        break

    numero1 = int(input('entre com 1o numero: '))
    numero2 = int(input('entre com 2o numero: '))
    if opcao == '1':
        resultado = soma()
    elif opcao == '2':
            resultado = subtrai()
    elif opcao == '3':
        resultado = multiplica()
    elif opcao == '4':
        resultado = divide()
    else:
        print('OPCAO INVALIDA')

    print(f'resultado = {resultado}')


print('FIM')