#mesmo desafio só que aceita apenas numeros entre 0 e 1000.
lista_numero = []
loop_lista= 1
while loop_lista > len(lista_numero):
    numero_inicial = int(input("adicione o primeiro numero da lista entre 0 a 1000:"))
    if numero_inicial in range(0,1001):
        lista_numero.append (numero_inicial)
adicionar_numero = 's'
while adicionar_numero == 's':
    numero_adicional = int(input("digite outro numero a lista entre 0 a 1000:"))
    if numero_adicional in range(0,1001):
        lista_numero.append (numero_adicional)
        adicionar_numero = input ("deseja adicionar outro numero?[s ou n]")[:1]
lista_numero.sort()
print (f'o menor numero é {lista_numero [0]} e o maior numero é {lista_numero [-1]}')