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
        if elemento % 2 == 0:  # Comprobar si el número es par
            numeros_pares.append(elemento)
        cola_auxiliar.enqueue(elemento)  # Guardamos el elemento en la cola auxiliar
    
    # Restauramos la cola original desde la cola auxiliar
    while not cola_auxiliar.es_vacia():
        cola.enqueue(cola_auxiliar.dequeue())
    
    return numeros_pares

# Ejecución directa del código sin main()

# Pedir al usuario el tamaño de la cola
num_elem = int(input("Ingrese el tamaño de la cola: "))
cola1 = ColaSimple(num_elem)

# Llenar la cola con números ingresados por el usuario
for i in range(num_elem):
    valor = int(input(f"Ingrese el valor {i + 1} para la cola: "))
    cola1.enqueue(valor)

# Mostrar los números pares en la cola
numeros_pares = mostrar_numeros_pares(cola1)

if numeros_pares:
    print(f"Los números pares en la cola son: {numeros_pares}")
else:
    print("No hay números pares en la cola.")

# Mostrar la cola después de procesarla (debería ser la misma)
print("Estado final de la cola:")
cola1.mostrar()
