class Producto:
    def __init__(self, codigo_prod, nombre_prod, precio_prod, marca_prod):
        self.codigo_prod = codigo_prod
        self.nombre_prod = nombre_prod
        self.precio_prod = precio_prod
        self.marca_prod = marca_prod
    
    def get_precio(self):
        return self.precio_prod
    
    def get_nombre(self):
        return self.nombre_prod
    
    def get_codigo(self):
        return self.codigo_prod
    
    def get_marca(self):
        return self.codigo_marca
    
    def set_precio(self, nuevo_precio):
        self.precio_prod = nuevo_precio

    def set_nombre(self, nuevo_nombre):
        self.nombre_prod = nuevo_nombre

    def set_marca(self, nuevo_marca):
        self.nombre_prod = nuevo_marca
    
    def __str__(self):
        return f"{self.nombre_prod} -- {self.precio_prod}"
    