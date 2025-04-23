class Nodo:
     # Nodo de un árbol binario
     def __init__(self, clave):
         self.izquierda = None
         self.derecha = None
         self.clave = clave
        
class ArbolBinario:
     # Árbol binario de búsqueda
     def __init__(self):
         self.raiz = None
        
     def insertar(self, clave):
         # Inserta una clave en el árbol
         if self.raiz is None:
             self.raiz = Nodo(clave)
         else:
             self._insertar_recursivo(self.raiz, clave)
        
     def _insertar_recursivo(self, nodo, clave):
         # Inserción recursiva
         if clave < nodo.clave:
             if nodo.izquierda is None:
                 nodo.izquierda = Nodo(clave)
             else:
                 self._insertar_recursivo(nodo.izquierda, clave)

         else:
             if nodo.derecha is None:
                 nodo.derecha = Nodo(clave)
             else:
                 self._insertar_recursivo(nodo.derecha, clave)
                
     def recorrido_inorden(self, nodo):
         # Recorrido inorden (izquierda, raíz, derecha)
         if nodo:
             self.recorrido_inorden(nodo.izquierda)
             print(nodo.clave, end=" ")
             self.recorrido_inorden(nodo.derecha)
            
     def recorrido_preorden(self, nodo):
         # Recorrido preorden (raíz, izquierda, derecha)
         if nodo:
             print(nodo.clave, end=" ")
             self.recorrido_preorden(nodo.izquierda)
             self.recorrido_preorden(nodo.derecha)
            
     def recorrido_posorden(self, nodo):
         # Recorrido postorden (izquierda, derecha, raíz)
         if nodo:
             self.recorrido_posorden(nodo.izquierda)
             self.recorrido_posorden(nodo.derecha)
             print(nodo.clave, end=" ")
        
        
# Llamar al árbol
arbol = ArbolBinario()
valores = [5, 3, 1, 8, 4]

for i in valores:
     arbol.insertar(i)
    
print("Recorrido inorden")
arbol.recorrido_inorden(arbol.raiz)
print("\nRecorrido preorden")
arbol.recorrido_preorden(arbol.raiz)
print("\nRecorrido postorden")
arbol.recorrido_posorden(arbol.raiz)