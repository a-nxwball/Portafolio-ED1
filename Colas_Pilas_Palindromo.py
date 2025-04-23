from collections import deque

# Pila simple (LIFO)
class NodoPila:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Pila:
    def __init__(self):
        self.cima = None

    def apilar(self, valor):
        nuevo = NodoPila(valor)
        nuevo.siguiente = self.cima
        self.cima = nuevo

    def desapilar(self):
        if self.cima is None:
            return None
        valor = self.cima.valor
        self.cima = self.cima.siguiente
        return valor

    def mostrar(self):
        actual = self.cima
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

# Cola simple (FIFO)
class NodoCola:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None

    def encolar(self, valor):
        nuevo = NodoCola(valor)
        if self.final is None:
            self.frente = self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo

    def desencolar(self):
        if self.frente is None:
            return None
        valor = self.frente.valor
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        return valor

    def mostrar(self):
        actual = self.frente
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

# Demostración de pila y cola con nodos
print("\nPila simple con nodos:")
pila_nodos = Pila()
pila_nodos.apilar(1)
pila_nodos.apilar(2)
pila_nodos.apilar(3)
pila_nodos.mostrar()
print("Desapilado:", pila_nodos.desapilar())
pila_nodos.mostrar()

print("\nCola simple con nodos:")
cola_nodos = Cola()
cola_nodos.encolar(1)
cola_nodos.encolar(2)
cola_nodos.encolar(3)
cola_nodos.mostrar()
print("Desencolado:", cola_nodos.desencolar())
cola_nodos.mostrar()


# Definición de la función es_palindromo
# Esta función verifica si una palabra es un palíndromo utilizando una pila y una cola.
def es_palindromo(palabra_palindromo):
    palabra_palindromo = palabra_palindromo.lower().replace(" ", "")

    pila = []
    cola = deque()

    for letra in palabra_palindromo:
        pila.append(letra)
        cola.append(letra)

    while pila:
        if pila.pop() != cola.popleft():
            return False

    return True
palabra_palindromo = input("Ingrese una palabra para que registre el usuario y que contenga las ultimas letras iguales: ")

if es_palindromo(palabra_palindromo):
    print(f"{palabra_palindromo} la palabra es correcta es un palindromo.")
else:
    print(f"{palabra_palindromo}  error la palabra no es un palindromo.")
