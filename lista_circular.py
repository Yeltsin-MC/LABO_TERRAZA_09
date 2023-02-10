
"""Hacer una lista circular que tengas las funciones de """
        # Eliminar ultimo.
        # Lista Vacía
        # Agregar Inicio
        # Eliminar Inicio
        # Mostrar Lista

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaCircular:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero == None

    def agregar_inicio(self, dato):
        nuevo = Nodo(dato)
        if self.vacia():
            self.primero = nuevo
            self.ultimo = nuevo
            self.ultimo.siguiente = self.primero
        else:
            nuevo.siguiente = self.primero
            self.primero = nuevo
            self.ultimo.siguiente = self.primero

    def eliminar_inicio(self):
        if self.vacia():
            return None
        elif self.primero == self.ultimo:
            self.primero = None
            self.ultimo = None
        else:
            self.primero = self.primero.siguiente
            self.ultimo.siguiente = self.primero

    def eliminar_ultimo(self):
        if self.vacia():
            return None
        elif self.primero == self.ultimo:
            self.primero = None
            self.ultimo = None
        else:
            actual = self.primero
            anterior = None
            while actual.siguiente != self.ultimo:
                anterior = actual
                actual = actual.siguiente
            anterior.siguiente = self.primero
            self.ultimo = anterior

    def mostrar_lista(self):
        if self.vacia():
            return None
        else:
            actual = self.primero
            while actual:
                print(actual.dato)
                actual = actual.siguiente
                if actual == self.primero:
                    break


lista = ListaCircular()
lista.agregar_inicio(1) # agrega a las lista el número 1
lista.agregar_inicio(2) # agrega a las lista el número 2
lista.agregar_inicio(3) # agrega a las lista el número 3
lista.mostrar_lista()

lista.eliminar_ultimo()
lista.mostrar_lista()

lista.eliminar_inicio()
lista.mostrar_lista() #muestra la lista final
