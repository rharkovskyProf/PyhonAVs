# Faça um programa que leia um texto aleatório, com no mínimo 20 caracteres quaisquer,
# e forneça seu tamanho, versão Maiuscula e Minuscula, quantidade de vogais, quantidade de digitos,
# Quantiade de caracteres especiais
# Substituir a palavra "Piton" por "Python"

texto = input ('Entre com um texto (até 20 caracteres): ')
tamanho = len(texto)
print(f'O tamanho é {tamanho}')
print(f'Versão Maiuscula: {texto.upper()}')
print(f'Versão Maiuscula: {texto.lower()}')

contadorVogais = 0
for i in range(tamanho):
    if texto[i].lower() in ('a','e','i','o','u'):
        contadorVogais = contadorVogais +1

contadorDigitos = 0
for i in range(tamanho):
    if texto[i].isdigit():
        contadorDigitos = contadorDigitos +1

contadorEspecial = 0
for i in range(tamanho):
    if texto[i] in ('!','@','#','$','%', '*', '(', ')'):
        contadorEspecial = contadorEspecial +1

# fora do loop "for"
print(f'Existem {contadorVogais} vogais no texto')
print(f'Existem {contadorDigitos} digitos no texto')
print(f'Existem {contadorEspecial} caracteres especiais no texto')

#corrigindo a palavra "Piton"
print(f'original: {texto}')
print(f'Acertado: {texto.replace("Piton", "Python")}')