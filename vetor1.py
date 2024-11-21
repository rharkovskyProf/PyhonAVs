# Faça um programa que lê 10 números inteiros e imprima os valores origianis, em ordem reversa,
numeros = [0]*10
print(f'Original: {numeros}')
for i in range(10):
    numeros[i] = int(input(f'entre com um numero na posicao {i}: '))

print(f'ordem original {numeros}')
print(f'5o elemento {numeros[5]}')

# tamanho, soma e media
print(f'tamanho: {len(numeros)}')
print(f'Soma: {sum(numeros)}')
print(f'Media: {sum(numeros)/len(numeros)}')

# ordenar
print(f'ordenado: {sorted(numeros)}')

# inverter
numeros.reverse()
print(f'ordem reversa {numeros}')
