#validação de dados 
nome = 'o'
tamanho_nome = 3
idade= 151
salario = float (0)
sexo = 'o'
estado_civil = 'o'

while tamanho_nome >= len(nome):
   nome = input('digite seu nome:')
while idade >150:
   idade = int (input('digite sua idade:'))
while salario == 0:
   salario = float (input('digite o seu salario:'))
while (sexo != 'f' and sexo !='m'):
   sexo = input ('digite seu sexo: (f ou m)')
while (estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd'):
    estado_civil = input('digite seu estado civil atual (s, c, v, d):')
print (f'nome: {nome}')
print (f'idade: {idade}')
print (f'salario: {salario:.2f}')
print (f'estado civil: {estado_civil}')
texto = input('digite um texto: ')
print (f'largura do texto: {(len(texto))}')