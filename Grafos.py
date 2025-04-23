"""
Estructuras de datos: Grafos.
 
- Los grafos son una estructura de datos que consiste en un conjunto de nodos (o vértices) y un conjunto de aristas (o bordes) que conectan pares de nodos.

- Las conexiones se manejan de manera unidireccional o bidireccional, dependiendo de si las aristas tienen una dirección o no.

- Para saber si un grafo es dirigido o no, se puede usar la propiedad de que si existe una arista de A a B, pero no de B a A, entonces el grafo es dirigido. Se usan matrices adyacentes para representar los grafos, donde cada celda de la matriz indica si existe una conexión entre dos nodos.

- Se tiene que saber tambien "cuanto es la cantidad" de 'algo' enviada de un nodo a otro y se evalua en sus aristas la problematica del "costo". Se usa una matriz de pesos para representar los grafos ponderados, donde cada celda de la matriz indica el costo de la conexión entre dos nodos. Si no hay conexión, se usa un valor especial (como infinito) para indicar que no hay conexión entre esos nodos.

- Ejemplos de aplicaciones en la vida real:
1. Redes sociales: Los nodos representan personas y las aristas representan relaciones entre ellas.
2. Mapas: Los nodos representan ciudades y las aristas representan carreteras entre ellas.
3. Rutas: Los nodos representan paradas y las aristas representan rutas entre ellas.
4. Transporte: Los nodos representan estaciones y las aristas representan rutas entre ellas.
5. Informática: Los nodos representan computadoras y las aristas representan conexiones entre ellas.
6. Juegos: Los nodos representan personajes y las aristas representan relaciones entre ellos.
"""
grafo = {
    'A': ['B', 'C',],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}

# Imprimir el grado de cada nodo
def imprimir_grados(grafo):
    print("Grado de cada nodo: ")
    for nodo in grafo:
        grado = len(grafo[nodo])
        print(f"{nodo}: {grado}")
        
# Nodo de mayor grado
def nodo_mayor_grado(grafo):
    """ 
    max_nodo: nodo con mayor grado
    max_grado: grado del nodo con mayor grado
    
    Por que el maximo grado es -1?:
    R. Porque el grado de un nodo no puede ser negativo. Al final, si no se encuentra un nodo con grado mayor a -1, significa que el grafo está vacío o no tiene nodos. Por lo tanto, se inicializa en -1 para que cualquier grado encontrado sea mayor que -1 y se pueda actualizar el nodo con mayor grado. Si el grafo está vacío, max_nodo seguirá siendo None y max_grado seguirá siendo -1.
    
    Se busca el nodo con mayor grado ya que esto puede ser útil en diversas aplicaciones, como en redes sociales, donde se desea identificar al usuario más conectado o influyente. También puede ser útil en mapas, donde se desea identificar la ciudad más conectada; o en transporte, donde se desea identificar la estación más concurrida.
    """
    max_nodo = None
    max_grado = -1
    for nodo in grafo:
        grado = len(grafo[nodo])
        if grado > max_grado:
            max_grado = grado
            max_nodo = nodo
    return max_nodo, max_grado

# Si es regular o no
def es_regular(grafo):
    """ 
    Explicacion:
    Un grafo es regular si todos sus nodos tienen el mismo grado.
    Para verificar esto, se calcula el grado de cada nodo y se compara con el grado de los demás nodos. Si todos los grados son iguales, el grafo es regular.
    
    Aplicacion:
    - En redes sociales, un grafo regular podría representar una red donde cada persona tiene el mismo número de amigos.
    - En mapas, un grafo regular podría representar una red de carreteras donde cada ciudad tiene el mismo número de conexiones con otras ciudades.
    - En transporte, un grafo regular podría representar una red de estaciones donde cada estación tiene el mismo número de rutas.
    
    Se puede acceder a un grafo regular de manera eficiente, ya que todos los nodos tienen el mismo número de conexiones. Esto permite realizar búsquedas y recorridos de manera más rápida y eficiente.
    """
    grados = [len(grafo[nodo]) for nodo in grafo]
    return all(grado == grados[0] for grado in grados)

# Ejemplos de uso
imprimir_grados(grafo)
nodo_max, grado_max = nodo_mayor_grado(grafo)
print(f"Nodo con mayor grado: {nodo_max} (grado: {grado_max})")

if es_regular(grafo):
    print("El grafo es regular (todos los nodos tienen el mismo grado).")
else:
    print("El grafo no es regular (no todos los nodos tienen el mismo grado).")
