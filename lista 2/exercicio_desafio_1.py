#Serie de Fibonacci

a, b = 0,1 

contador = 0 

while contador < 16:
    
    print(a)
    
    a, b = b, a + b

    contador += 1