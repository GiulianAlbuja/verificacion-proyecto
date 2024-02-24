class Producto:
    def __init__(self, id, nombre, descripcion):
        self.id_producto = id
        self.nombre_producto = nombre
        self.descripcion = descripcion

    calificaciones = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    calificaiones_recibidas = list()

class Pedido:
    def __init__(self, id, estado, cantidad, direccion, productos, servicio):
        self.id_pedido = id
        self.estado = estado
        self.cantidad = cantidad
        self.direccion = direccion
        self.productos = productos
        self.servicio = servicio
        self.pagado = True

class Cliente:
    def __init__(self, cedula, nombre, apellido, correo, telefono, pedido):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono
        self.pedido = pedido

    def calificar_producto(self, calificacion):
        calificacion.producto.calificaciones[calificacion.estrellas] += 1
        calificacion.producto.calificaiones_recibidas.append(calificacion)