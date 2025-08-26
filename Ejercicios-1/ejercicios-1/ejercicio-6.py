import random
#Numero del usuario

#Numero que pone el pelotudo que lo maneja al programa
# 3719

numero = '3719'


#Restricciones
#
# Intentos : 8
# Comparar dos cadenas iguales. Iguales significa
#       1. Mismo digito en misma posicion, por ejemplo 12 no es igual a 21 porque por más de tener numeros iguales, la posicion varia.
#       2. Que las cadenas tengan la misma longitud. 
#       3. Si la primer comparación falla, no te hace falta seguir comparando.
# 
# #


cadenaOriginal = str(random.randint(1000, 9999)) # Te importa una cadena random de 4 caracteres siempre. 
print(cadenaOriginal)
cadenaUsuario = str(input("Ingrese el numero a adivinar:"))  #1234
numeroAcertado=1
intentosPermitidos=1
if(len(cadenaOriginal)!=len(cadenaUsuario)):
    print("No se pueden comparar dos cadenas de distinto tamaño")
else:
    while (intentosPermitidos<8):
        numeroAcertado=0
        for Digito in range(0,len(cadenaOriginal)):
            # iterar digito por digito la cadena, si es 1234, vos vas a tener en Digito, los valores: 1, 2, 3 y 4.
            if(cadenaOriginal[Digito]==cadenaUsuario[Digito]):
                print(cadenaOriginal[Digito]+"-"+cadenaUsuario[Digito])
                numeroAcertado+=1
                print(numeroAcertado)
        if(numeroAcertado==len(cadenaOriginal)):
            print("Ganaste mamotreto!!")
            break
        else:
            print("ERROR. No es el numero, pero adivinaste:" + str(numeroAcertado) + " numeros")
            intentosPermitidos+=1
            cadenaUsuario=str(input("Ingrese el numero a adivinar:"))
            

    
    