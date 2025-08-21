sumOfNumbers= 0 
while True: 
    number= int(input("Ingrese un número: "))
    if number % 2 == 0:
        sumOfNumbers +=0
    answer = input("Deseas agregar otro número? (si/no): ").lower
    if answer == "no":
        break
print("La suma de los numeros pares es", sumOfNumbers)

#linea de codigo nueva 