countOfNumbers= 0
while True:
    numberToKnow=(int(input("Ingresa el numero a adivinar: ")))
    tryToKnowNumber=(int(input("Ingresa un número: ")))
    tryOtherNumber=(int(input("Ingresa otro número: ")))
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
    elif numberToKnow != int():
        print("El valor entregado no es valido, intente nuevamente")
    elif tryOtherNumber != int():
        print("El valor entregado no es valido, intente nuevamente")
    elif tryToKnowNumber != int():
        print("El valor entregado no es valido, intente nuevamente")