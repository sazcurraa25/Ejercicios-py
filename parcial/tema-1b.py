tituloLibro=[]
generoLibro=[]
puntuacionLibro=[]
def agregar_libro(titulo, genero):
    tituloLibro.append(titulo)
    generoLibro.append(genero)
    puntuacionLibro.append([])
def votar_libro(titulo, puntuacion):
    if titulo in tituloLibro:
        i = tituloLibro.index(titulo)
        puntuacionLibro[i].append(puntuacion)
def recomendar_por_genero(genero):
    mejor_promedio = -1
    mejor_titulo = None
    print(f"Recomendaciones para genero: {genero}")
    for i in range(len(tituloLibro)):
        if generoLibro[i] == genero:
            if len(puntuacionLibro[i])>0:
                promedio = sum(puntuacionLibro[i])/len(puntuacionLibro[i])
                if promedio > mejor_promedio:
                    mejor_promedio = promedio
                    mejor_titulo = tituloLibro[i]
    if mejor_titulo:
            print(f"El libro recomendado es {mejor_titulo} con {mejor_promedio:.2f}") 
    else:
            print(f"No hay libros con votos en el genero {genero}")

agregar_libro("El Principito", "Literatura infantil")
agregar_libro("Cien años de soledad", "Novela")
agregar_libro("Crónicas marcianas", "Novela")

votar_libro("El Principito",10)
votar_libro("El Principito",9)
votar_libro("El Principito",8)
votar_libro("Cien años de soledad",9)
votar_libro("Cien años de soledad",8)
votar_libro("Crónicas marcianas",8)

recomendar_por_genero("Novela")
recomendar_por_genero("Literatura infantil") 











# Lista de letras originales
i = ["a", "e", "i", "o", "u"]

# Lista de letras encriptadas (en el mismo orden)
ii = ["v", "w", "x", "y", "z"]

# Función para encriptar con listas paralelas
def encriptar(palabra):
    resultado = ""
    for letra in palabra:
        if letra in i:  # si la letra está en la lista i
            indice = i.index(letra)   # buscamos su posición
            resultado += ii[indice]   # usamos la misma posición en ii
        else:
            resultado += letra  # si no está, se deja igual
    return resultado


# ---------------- EJEMPLO ----------------
print(encriptar("casa"))   # cvsv
print(encriptar("fino"))   # fxny
print(encriptar("peru"))


productos = [
     [],  # nombres
     [],  # cantidades
     []   # precios
]

def cargar_venta(producto, cantidad, precio):
    if producto in productos[0]:
        # si el producto ya existe, reemplazo sus valores
        i = productos[0].index(producto)
        productos[1][i] = cantidad
        productos[2][i] = precio
    else:
        # si no existe, lo agrego
        productos[0].append(producto)
        productos[1].append(cantidad)
        productos[2].append(precio)

def imprimir_ventas():
    print("Ventas registradas (últimos valores):")
    for i in range(len(productos[0])):
        print(f"{productos[0][i]} - Cantidad: {productos[1][i]} - Precio por tonelada: ${productos[2][i]}")


# ------------------ EJEMPLO ------------------
cargar_venta("Soja", 500, 320) 
cargar_venta("Trigo", 1000, 1000) 
cargar_venta("Trigo", 300, 250) 
cargar_venta("Cebada", 400, 220) 
cargar_venta("Soja", 1000, 1000) 
cargar_venta("Soja", 200, 340) 

imprimir_ventas()
