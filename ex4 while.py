frase = input('Entre com uma frase: ')
tamanho = len(frase)
digitos=''
alfa=''
i = 0
while (i <tamanho):
    letra = frase[i]
    print(f'a letra número {i} é {letra}')
    if letra.isdigit():
        digitos = digitos + letra
    else:
        alfa =alfa + letra

    i = i +1

print(f'Na frase {frase}os digitos da frase são {digitos} e as letras são {alfa}')
print('FIM')