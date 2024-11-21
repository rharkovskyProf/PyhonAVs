# --TEXTOS E TEXTOS—
# Escreva um código que leia um texto e o imprima, até que o texto lido seja igual a “Sair”,
#  em qualquer grafia (por ex: SAIR, sair, SAir, saIR, etc...).

while True:
    texto = input('Entre com Texto: ')
    if texto.upper()=='SAIR':
        break
    print(texto)

print('FIM DO PROGRAMA')