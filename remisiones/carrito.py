class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get('carrito')
        if not carrito:
            self.session['carrito'] = {}
            self.carrito = self.session['carrito']
        else:
            self.carrito = carrito
    
    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                'producto_id': producto.id,
                'codigo': producto.codigo,
                'nombre': producto.nombre,
                'marca': producto.marca,
                'cantidad': 1,
                'peso': round(producto.peso,2)
            }
        else:
            self.carrito[id]['cantidad'] += 1
            #self.carrito[id]['peso'] += round(producto.peso,2)
        self.guardar_carrito()
    
    def guardar_carrito(self):
        self.session['carrito'] = self.carrito
        self.session.modified = True
    
    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()
    
    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]['cantidad'] -= 1
            #self.carrito[id]['peso'] -= round(producto.peso,2)
            if self.carrito[id]['cantidad'] <= 0: self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session['carrito'] = {}
        self.session.modified = True