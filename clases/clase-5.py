# Diseño orientado a objetos
    # las escencia de OOD es desctribir al sistema en terminos de "cajas negreas magicas" (objetos) y sus interfases (metodos)
    # cada componente proporciona un conjunto de servicios a traves de su interfaz
    # los demas componentes son clientes de los servicios
    # solo se necesita entender la interfaz de una servicio; los detalles de la implementacion no son importantes, pueden cambiarse y no deberian afectar al cliente en lo absoluto
    # el componente que porporciona el servicio no debería tener en cuenta como se utiliza el servicio, solo tiene que porporcional el servicio "tal y como se anuncia" a traves de la interfaz
    # separar las "preocupaciones" de implementacion hace posible el diseño de sistemas complejos
# Los objetos
    # un objeto es una pedazo de codigo y datos autocontenidos 
    # un aspecto clave del enfoque de los objetos es dividir el problema en partes más pequeñas y comprensibles (divide and conquer)
    # los objetos tienen limites que nos permiten ignorar los detalles innecesarios. es decir, ocultan detalles y nos permiten enfocarnos en el "resto del programa"
    # clase- una plantilla 
    # metodo - una capacidad definida de una clase
    # atributo - un dato en una clase
    # objeto - una instancia en particular de una clase
# entonces un objeto consiste en : 
    # una coleccion de informacion relacionada (atributos)
class Animal():
    comidas= 0 #<------------- La cantidad de comida que tiene 
    def comer(self):
        self.comidas = self.comidas + 1
        print("He comido ", self.comidas, " veces")
        
perro = Animal()
perro.comer()
perro.comer()
Animal.comer(perro)
print(type(perro))
