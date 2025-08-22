sumOfNumbers= 0 
while True: 
    number= int(input("Ingrese un número: "))
    answer = input("Deseas agregar otro número? (si/no): ").lower()
    if number % 2 == 0:
        sumOfNumbers += number
    if answer == "no":
        break
    elif answer != "si":
        print("Lo introducido no corresponde con lo que se pide")
print("La suma de los numeros pares es", sumOfNumbers)

