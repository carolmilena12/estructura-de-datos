from cola_simple import ColaSimple

def encontrar_mayor(cola):
    if cola.es_vacia():
        print("La cola está vacía, no se puede encontrar el mayor número.")
        return None
    
    # Sacamos el primer elemento como base para comparar y lo guardamos en la cola auxiliar
    mayor = cola.dequeue()  
    cola_auxiliar = ColaSimple(cola.max)
    cola_auxiliar.enqueue(mayor)  # Guardamos el primer elemento en la cola auxiliar
    
    # Seguimos extrayendo elementos de la cola y encontramos el mayor
    while not cola.es_vacia():
        elemento = cola.dequeue()
        if elemento > mayor:
            mayor = elemento
        cola_auxiliar.enqueue(elemento)  # Guardamos el elemento en la cola auxiliar
    
    # Restauramos la cola original desde la cola auxiliar
    while not cola_auxiliar.es_vacia():
        cola.enqueue(cola_auxiliar.dequeue())
    
    return mayor

# Ejecución directa del código sin main()

# Crear una cola con tamaño 5
cola1 = ColaSimple(5)

cola1.enqueue(7)
cola1.enqueue(25)
cola1.enqueue(70)
cola1.enqueue(6)
cola1.enqueue(10)

# Encontrar el mayor número en la cola
mayor = encontrar_mayor(cola1)

if mayor is not None:
    print(f"El número mayor en la cola es: {mayor}")

# Mostrar la cola después de procesarla (debería ser la misma)
print("Estado final de la cola:")
cola1.mostrar()
