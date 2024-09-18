#Creacion de la clase cola en Python
class ColaSimple:
    def __init__(self, max_size):
        self.max = max_size
        self.cola = [None] * (self.max + 1)  # Arreglo para la cola
        self.front = 0  # Inicio de la cola
        self.back = 0   # Final de la cola

    def es_vacia(self):
        return self.front == 0 and self.back == 0

    def es_llena(self):
        return self.back == self.max

    def size(self):
        return self.back - self.front

    def enqueue(self, elemento):
        if not self.es_llena():
            self.back += 1
            self.cola[self.back] = elemento  # Almacenar el nuevo elemento
        else:
            print("Cola llena...")
 
    def dequeue(self):
        elemento = None
        if not self.es_vacia():
            self.front += 1
            elemento = self.cola[self.front]
            # Si la cola está vacía después de la eliminación
            if self.front == self.back:
                self.front = 0
                self.back = 0
        else:
            print("Cola vacía...")
        return elemento
    
    def mostrar(self):
        if self.es_vacia():
            print("Cola vacía...")
        else:
            print(self.cola[self.front + 1:self.back + 1])


