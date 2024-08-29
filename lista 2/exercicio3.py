#calculadora de adição 
print("Operaçoes de adição")

while True:
    number_1 = float(input("\nDigite o primeiro valor: "))
    number_2 = float(input("Digite o segundo valor: "))

    resultado = number_1 + number_2 

    print(f"\n{number_1} + {number_2} = {resultado}")

    continuar = input("\nDeseja fazer outra conta? S/N ").lower()

    if continuar != 's':
        print("Fim!")
        break 