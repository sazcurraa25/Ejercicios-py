import functools
# se agrega en una lista diferente para poder agregar cosas ademas de agregarle alguno  de los elementos de las listas
# si alguno de los elementos no cumple con la función se elimina
# filter(func, list)
# def no_negativo(numero):
#     return numero >= 0
# listadoDeStock = [1,2,0,-10]

# listado = filter(validacion_dni, listadoDeDni)
# print(list(listado))

# def validacion_dni(DNI):
#     salida = False
#     if(DNI.isdigit()) and (len(DNI)>=7 and len(DNI)<= 8 ):
#         salida = True
#     return salida

# listadoDeDni = [42660378, 23998338, 8992993]


persona = ["ana", "mariela", "josefina"]
def suma(a,b):
    return a + " "+ b

def mult(a,b):
    return a * b

resultado = functools.reduce(suma, persona)
# resultado2 = functools.reduce(mult, lista)

print(resultado)
# print(resultado2)

# # el .zip combina varias listas en una emparejandolo por indice, donde la lista resultante se concatena toda junta 
# zip(list1, ..., listn)

# list1= [1,2,3,4]
# list2= ['a', 'b', 'c', 'd']

produce = ['manzana', 'naranja', 'pera']
prices = [50, 40, 60] 