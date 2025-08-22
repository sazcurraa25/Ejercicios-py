def numberOfDNI (number):
    if (len(number)==8 or len(number)==7) and number.isnumeric():
        return "true"
    else:
        return "false"
dni = numberOfDNI(input("Ingrese su DNI: "))
print(dni)

