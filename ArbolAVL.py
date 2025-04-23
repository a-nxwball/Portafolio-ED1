# Clase que representa un nodo del AVL
class NodoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        self.altura = 1

# Clase para el árbol AVL con sus operaciones
class AVL:
    def __init__(self):
        self.raiz = None

    def altura_nodo(self, nodo):
        return nodo.altura if nodo else 0

    def obtener_balance(self, nodo):
        return self.altura_nodo(nodo.izq) - self.altura_nodo(nodo.der) if nodo else 0

    def rotar_derecha(self, y):
        x = y.izq
        T2 = x.der

        # Rotación
        x.der = y
        y.izq = T2

        # Actualización de alturas
        y.altura = 1 + max(self.altura_nodo(y.izq), self.altura_nodo(y.der))
        x.altura = 1 + max(self.altura_nodo(x.izq), self.altura_nodo(x.der))
        return x

    def rotar_izquierda(self, x):
        y = x.der
        T2 = y.izq

        # Rotación
        y.izq = x
        x.der = T2

        # Actualización de alturas
        x.altura = 1 + max(self.altura_nodo(x.izq), self.altura_nodo(x.der))
        y.altura = 1 + max(self.altura_nodo(y.izq), self.altura_nodo(y.der))
        return y

    def insertar(self, nodo, valor):
        if not nodo:
            return NodoAVL(valor)

        if valor < nodo.valor:
            nodo.izq = self.insertar(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self.insertar(nodo.der, valor)
        else:
            return nodo  # No permitir duplicados

        nodo.altura = 1 + max(self.altura_nodo(nodo.izq), self.altura_nodo(nodo.der))
        balance = self.obtener_balance(nodo)

        # Balanceo
        if balance > 1 and valor < nodo.izq.valor:
            return self.rotar_derecha(nodo)
        if balance < -1 and valor > nodo.der.valor:
            return self.rotar_izquierda(nodo)
        if balance > 1 and valor > nodo.izq.valor:
            nodo.izq = self.rotar_izquierda(nodo.izq)
            return self.rotar_derecha(nodo)
        if balance < -1 and valor < nodo.der.valor:
            nodo.der = self.rotar_derecha(nodo.der)
            return self.rotar_izquierda(nodo)

        return nodo

    def agregar(self, valor):
        self.raiz = self.insertar(self.raiz, valor)

    def obtener_in_order(self):
        recorrido = []
        self._in_order(self.raiz, recorrido)
        return recorrido

    def _in_order(self, nodo, recorrido):
        if nodo:
            self._in_order(nodo.izq, recorrido)
            recorrido.append(nodo.valor)
            self._in_order(nodo.der, recorrido)

    def print_tree_horizontal(self, nodo, nivel=0, prefijo="Raíz: "):
        """
        Imprime el árbol en formato horizontal con la raíz a la izquierda y los hijos expandiéndose a la derecha.
        """
        if nodo is not None:
            print(" " * (nivel * 8) + prefijo + str(nodo.valor))
            if nodo.izq or nodo.der:
                if nodo.izq:
                    self.print_tree_horizontal(nodo.izq, nivel + 1, "Izq ─> ")
                if nodo.der:
                    self.print_tree_horizontal(nodo.der, nivel + 1, "Der ─> ")

# Lista original con duplicados
valores = [5, 9, 6, 0, 3, 2, 5, 4, 8, 9, 2, -5, -9, -6, 8, 7, 56, 6, 4, 2, 33, 66, 55, 7, 4, 5, 8, 1, 6, 5]

# Eliminar duplicados manteniendo el orden original
valores_unicos = list(dict.fromkeys(valores))

# Crear árbol AVL e insertar valores
avl = AVL()
for v in valores_unicos:
    avl.agregar(v)

# Imprimir recorrido in-order
print("Recorrido in-order:", avl.obtener_in_order())

# Visualizar el árbol AVL en horizontal
print("\nÁrbol AVL en formato horizontal:")
avl.print_tree_horizontal(avl.raiz)