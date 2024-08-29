#menor V, maior V e soma
lista_numero = []
numero_inicial = int(input("adicione o primeiro numero da lista:"))
lista_numero.append (numero_inicial)
adicionar_numero = 's'
while adicionar_numero == 's':
    numero_adicional = int(input("digite outro numero a lista:"))
    lista_numero.append (numero_adicional)
    adicionar_numero = input ("deseja adicionar outro numero?[s ou n]")[:1]
lista_numero.sort()
print (f'o menor numero é {lista_numero [0]} e o maior numero é {lista_numero [-1]}')