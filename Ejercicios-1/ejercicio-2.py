lastNumber=0
biggerNumber=0
while(lastNumber<5):
    insertNumber=(int(input("Ingrese un número: ")))
    lastNumber=lastNumber+1
    if(insertNumber>biggerNumber):
        biggerNumber=insertNumber
        print("el nuevo número más grande es ", biggerNumber)
    else:
        print("El numero mas grande es", biggerNumber)
    print(biggerNumber)