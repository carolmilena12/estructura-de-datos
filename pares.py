from cola_simple import ColaSimple

def mostrar_numeros_pares(cola):
    if cola.es_vacia():
        print("La cola está vacía.")
        return []
    
    # Cola auxiliar para restaurar la original después de procesar los elementos
    cola_auxiliar = ColaSimple(cola.max)
    numeros_pares = []

    # Recorremos la cola y extraemos los números pares
    while not cola.es_vacia():
        elemento = cola.dequeue()
        if elemento % 2 != 0:  # Comprobar si el número es par
            numeros_pares.append(elemento)
        cola_auxiliar.enqueue(elemento)  # Guardamos el elemento en la cola auxiliar
    
    # Restauramos la cola original desde la cola auxiliar
    while not cola_auxiliar.es_vacia():
        cola.enqueue(cola_auxiliar.dequeue())
    
    return numeros_pares

# Ejecución directa del código sin main()

# Crear una cola con tamaño 5
cola1 = ColaSimple(10)

cola1.enqueue(7)
cola1.enqueue(25)
cola1.enqueue(70)
cola1.enqueue(6)
cola1.enqueue(1)
cola1.enqueue(4)
cola1.enqueue(8)
cola1.enqueue(12)

# Mostrar los números pares en la cola
numeros_pares = mostrar_numeros_pares(cola1)

print(f"Los números pares en la cola son: {numeros_pares}")


# Mostrar la cola después de procesarla (debería ser la misma)
print("Estado final de la cola:")
cola1.mostrar()
