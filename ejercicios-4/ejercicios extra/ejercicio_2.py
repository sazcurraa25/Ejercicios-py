importantWorks = []
midWorks=[]
optionalWorks=[]
counter=0
while(counter<1000):
    defineWork=(input("Indica la tarea: "))
    for work in defineWork:
        if work == "urgente":
            importantWorks.append(defineWork)
        if work == "importante":
            midWorks.append(defineWork)
        if work == "opcional":
            optionalWorks.append(defineWork)
    continueOption=(input("Desea continuar? si/no: "))
    if continueOption == "si":
        print(defineWork)
    if continueOption == "no":
        break
print("Las tareas importantes son ", importantWorks)
print("las tareas medianamente importantes son: ", midWorks)
print("las tareas opcionales son ", optionalWorks)