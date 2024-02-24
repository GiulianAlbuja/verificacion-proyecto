class Producto:
    def __init__(self, id, nombre, descripcion):
        self.id_producto = id
        self.nombre_producto = nombre
        self.descripcion = descripcion

    calificaciones = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    calificaiones_recibidas = list()

    def feedback_producto_esta_dado(self):
        return True


class Pedido:
    def __init__(self, id, estado, cantidad, direccion, productos):
        self.id_pedido = id
        self.estado = estado
        self.cantidad = cantidad
        self.direccion = direccion
        self.productos = productos
        self.servicio = Servicio(self)
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


class Servicio:
    def __init__(self, pedido):
        self.pedido = pedido

        self.calificaciones = [
            {'estrellas': 1, "cantidad": 0, "porcentaje": "0"},
            {'estrellas': 2, "cantidad": 0, "porcentaje": "0"},
            {'estrellas': 3, "cantidad": 0, "porcentaje": "0"},
            {'estrellas': 4, "cantidad": 0, "porcentaje": "0"},
            {'estrellas': 5, "cantidad": 0, "porcentaje": "0"}
        ]

        self.calificaiones_recibidas = list()
    def calificar_servicio(self, calificacion_cliente):
        for calificacion in self.calificaciones:
            if calificacion["estrellas"] == calificacion_cliente:
                calificacion["cantidad"] += 1
                break
        self.calcular_porcentajes()


    def calcular_porcentajes(self):
        total_estrellas = sum(calificacion["cantidad"] for calificacion in self.calificaciones)
        for calificacion in self.calificaciones:
            porcentaje_calculado = (calificacion["cantidad"] / total_estrellas) * 100
            porcentaje_calculado = round(porcentaje_calculado)
            calificacion["porcentaje"] = str(porcentaje_calculado) + "%"



