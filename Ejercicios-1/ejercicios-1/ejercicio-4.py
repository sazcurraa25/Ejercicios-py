countOfNumbers= 0
numberToKnow=(int(input("Ingresa el numero a adivinar: ")))
while True:
    tryToKnowNumber=(int(input("Ingresa un número: ")))
    if numberToKnow>tryToKnowNumber:
        print("El número secreto es más chico. Intente nuevamente")
        countOfNumbers=countOfNumbers+1
    elif numberToKnow<tryToKnowNumber:
        print("El número secreto es más grande. Intente nuevamente")
        countOfNumbers=countOfNumbers+1
    elif numberToKnow==tryToKnowNumber:
        print("Acertó al número secreto")
        print("Uso", countOfNumbers, "intentos para adivinar")
        break