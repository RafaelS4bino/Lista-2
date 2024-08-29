#numero primo
numero = int(input('digite um numero: '))

if numero == 0 or numero == 1:
    print(f'o numero {numero} não é primo')
elif numero > 1:
    for i in range (2, numero):
        if (numero % i) == 0:
            print(f'o numero {numero} não é primo')
            break
    else:
        print(numero, 'é um numero primo')