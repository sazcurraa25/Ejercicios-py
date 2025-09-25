importantWorks = []
midWorks=[]
optionalWorks=[]
counter=0
while(counter<1000):
    defineWork=(input("Indica la tarea: "))
    if "Urgente" in defineWork:
        importantWorks.append(defineWork)
    if "Importante" in defineWork:
        midWorks.append(defineWork)
    if "Opcional" in defineWork:
        optionalWorks.append(defineWork)
    continueOption=(input("Queres agregar otra tarea SI/NO: "))
    if continueOption == "si":
        print(defineWork)
    if continueOption == "no":
        break
print("Las tareas importantes son ", importantWorks)
print("las tareas medianamente importantes son: ", midWorks)
print("las tareas opcionales son ", optionalWorks)