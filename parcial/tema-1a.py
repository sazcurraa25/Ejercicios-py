# Creamos listas vacías para guardar la información de las prendas
nombres = []
precios = []
cantidades = []

# Función para cargar una prenda al inventario
def cargar_prenda(nombre, precio, cantidad):
    # Guardamos los datos en listas paralelas
    nombres.append(nombre)
    precios.append(precio)
    cantidades.append(cantidad)

# Función para mostrar todas las prendas cargadas
def imprimir_mercaderia():
    print("El inventario de ropa es:")
    # Recorremos las listas en paralelo con zip
    for n, p, c in zip(nombres, precios, cantidades):
        print(f"{n} - precio {p} - unidades {c}")

# Función para calcular la valuación total del inventario
def calcular_valuacion_de_mercaderia():
    total = 0
    # Multiplicamos precio * cantidad para cada prenda y lo sumamos
    for p, c in zip(precios, cantidades):
        total += p * c
    print(f"La valuación total de la mercadería que tiene es {total}")


# ---------------- EJEMPLO DE USO ----------------
cargar_prenda("pantalón azul", 3000, 5)
cargar_prenda("remera roja", 2000, 3)
cargar_prenda("remera amarilla", 2000, 3)

imprimir_mercaderia()
calcular_valuacion_de_mercaderia()

#ejercicio 2 

lista_articulos = ["lapicera", "cartuchera", "regla", "tijera", "cuaderno"] 
lista_precios = [100, 2000, 500, 700, 500]
carrito=[]

def comprar(articulos):
    carrito.append(articulos)

def borrar(articulos):
    if articulos in carrito:
        carrito.remove(articulos)

def mostrar(carrito):
    print(",".join(carrito))

def calcular_costo(carrito):
    total = 0
    for articulo in carrito:
        if articulo in lista_articulos:
            i = lista_articulos.index(articulo)
            total += lista_precios[i]
    print(f"El gasto total es {total}")

comprar("lapicera")
comprar("cartuchera")
comprar("cuaderno")
mostrar(carrito)            # lapicera, cartuchera, cuaderno

borrar("cartuchera")
mostrar(carrito)            # lapicera, cuaderno

calcular_costo(carrito)

#ejercicio 3 

