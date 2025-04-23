#Listas

#Lista enlazada simple
class nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        
    def eliminar(self, valor):
        if self.cabeza is None:
            print("La lista esta vacia")
            return False
        
        if self.cabeza.valor == valor:
            self.cabeza = self.cabeza.siguiente
            print(f"El nodo con valor {valor} no ha sido eliminado")
            return True 
        
        nodo_actual = self.cabeza
        while nodo_actual.siguiente:
            if nodo_actual.siguiente.valor == valor:
                nodo_actual.siguiente = nodo_actual.siguiente.siguiente
                print(f"el nodo con valor {valor} no ha sido eliminado")
                return True
            nodo_actual = nodo_actual.siguiente

        print(f"el valor {valor} no se encuentra en la lista")
        
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        
    def agregar(self, valor):
        nuevo_nodo = nodo(valor)
        if self.cabeza == None:
                self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo
  
    def mostrar(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.valor, end = "->")
            nodo_actual = nodo_actual.siguiente
        print("none")
        
    def buscar(self, valor):
        nodo_actual = self.cabeza
        while nodo_actual:
            if nodo_actual.valor == valor:
                return True
            nodo_actual = nodo_actual.siguiente
        return False
    
lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregar(4)

lista.mostrar()
 
print(lista.buscar(2))
print(lista.buscar(0))
print(lista.buscar(9))

# Lista doblemente enlazada
class NodoDoble:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar(self, valor):
        nuevo_nodo = NodoDoble(valor)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo

    def mostrar_adelante(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" <-> ")
            actual = actual.siguiente
        print("None")

    def mostrar_atras(self):
        actual = self.cola
        while actual:
            print(actual.valor, end=" <-> ")
            actual = actual.anterior
        print("None")

    def eliminar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior
                print(f"Nodo con valor {valor} eliminado")
                return True
            actual = actual.siguiente
        print(f"Valor {valor} no encontrado")
        return False

print("\nLista doblemente enlazada:")
lista_doble = ListaDoblementeEnlazada()
lista_doble.agregar(10)
lista_doble.agregar(20)
lista_doble.agregar(30)
lista_doble.mostrar_adelante()
lista_doble.mostrar_atras()
lista_doble.eliminar(20)
lista_doble.mostrar_adelante()
