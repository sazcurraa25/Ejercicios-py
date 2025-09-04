nombre = [ "Maria", "Pedro", "Carlos"] 
apellido = [ "Perez", "Gomez", "Martinez"]
nombre_apellido=[]
for name, surname in zip(nombre, apellido):
    nombre_apellido.append(name + " " + surname)
print(nombre_apellido)