numberToKnow=(int(input("Ingresa el numero a adivinar: ")))
tryToKnowNumber=(int(input("Ingresa un número: ")))
countOfNumbers= 0
while(numberToKnow, tryToKnowNumber):
    tryOtherNumber=(int(input("Ingresa otro número: ")))
    countOfNumbers=countOfNumbers+1
    if(numberToKnow>tryToKnowNumber):
        print("El número secreto es más chico. Intente nuevamente")
    if(numberToKnow<tryToKnowNumber):
        print("El número secreto es más grande. Intente nuevamente")
    if(numberToKnow==tryToKnowNumber):
        print("Acertó al número secreto")
        print("Uso", countOfNumbers, "intentos para adivinar")
        break