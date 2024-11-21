i =0
while True:
    if i == 100:
        break

    resto = i%2
    if resto==0:
        print(f'o numero {i} é par')
    else:
        print(f'o numero {i} é impar')
    i = i+1