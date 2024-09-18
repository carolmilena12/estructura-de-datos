from cola_simple import ColaSimple

def numero_mayor(self):
        if self.es_vacia():
            return None
        return max(self.cola[self.front + 1:self.back + 1])
    
def mostrar_pares(self):
        if self.es_vacia():
            print("cola vacia")
        else:
            pares = [x for x in self.cola[self.front + 1:self.back + 1] if x is not None and x % 2 == 0]
            print("numeros pares en la cola:", pares)
   
Cola = Cola_Simple(7)
for _ in range(7):
    elemento = int(input("ingrese datos de la cola: "))
    Cola.enqueue(elemento)

Cola.mostrar()
print("numero mayor en la cola:" , Cola.numero_mayor())

Cola.mostrar_pares()

Cola.dequeue()
Cola.mostrar()