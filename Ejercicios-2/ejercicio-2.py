numberOfParticipants=0
nonSatisfactory=[]
lessSatisfactory=[]
mediumSatisfactory=[]
goodSatisfactory=[]
excellentSatisfactory=[]
lista=[0,0,0,0,0]
while (numberOfParticipants < 15):
    getQualification=int(input("Exprese su satisfacción del 1 al 5: "))
    if getQualification == 1:
        nonSatisfactory.append(getQualification)
    elif getQualification == 2:
        lessSatisfactory.append(getQualification)
    elif getQualification == 3:
        mediumSatisfactory.append(getQualification)
    elif getQualification == 4: 
        goodSatisfactory.append(getQualification)
    elif getQualification == 5:
        excellentSatisfactory.append(getQualification)
        lista[4]=lista[4]+1
    else:
        print("El numero ingresado no es correcto, intente de nuevo")
        continue
    numberOfParticipants +=1

print("Nada Satisfecho:",((len(nonSatisfactory)/15)*100), "%")
print("Poco satisfecho:",((len(lessSatisfactory)/15)*100), "%")
print("Medianamente satisfecho:",((len(mediumSatisfactory)/15)*100), "%")
print("Satisfecho:",((len(goodSatisfactory)/15)*100), "%")
print("Muy satisfecho:",((len(excellentSatisfactory)/15)*100),"%")
