# testar senha

# Criterio 1: senha >= 8 caracteres
def tamanhoValido(txt):
    tamanho = len(txt)
    return   (tamanho>=8)

# Criterio 2: senha nao pode comecar por digito
def naoIniciaDigito(txt):
    if txt[0].isdigit():
        return False
    else:
        return True
# Criterio 3: senha com pelo menos 1 maiusculo
def peloMenos1Maiusc(txt):
    Maisculo = 'QWERTYUIOPASDFGHJKLÇZXCVBNM'
    for i in range(len(txt)):
        if txt[i] in Maisculo:
            return True

    return False

#main

senha = input('Entre com uma senha: ')

if tamanhoValido(senha) & naoIniciaDigito(senha) & peloMenos1Maiusc(senha):
    print('Senha OK')
else:
    print('Senha INVALIDA')

print('FIM')