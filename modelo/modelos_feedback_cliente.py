class Producto:
    def __init__(self, id, nombre, descripcion):
        self.id_producto = id
        self.nombre_producto = nombre
        self.descripcion = descripcion
        self.calificaciones = {1: 0, 2: 1, 3: 1, 4: 0, 5: 2}
        self.calificaciones_recibidas = list()
        causas = ["Mala calidad de materiales"]
        self.calificaciones_recibidas.append(Calificacion(2, causas, self))
        causas = ["Mal funcionamiento"]
        self.calificaciones_recibidas.append(Calificacion(3, causas, self))
        causas = ["Buenos acabados", "Buena calidad de materiales"]
        self.calificaciones_recibidas.append(Calificacion(5, causas, self))
        causas = ["Buenos acabados", "Buena calidad de materiales"]
        self.calificaciones_recibidas.append(Calificacion(5, causas, self))


    def obtener_porcentajes_de_calificaciones(self):
        porcentajes_por_estrella = list()
        calificaciones_totales = 0
        for i in self.calificaciones:
            calificaciones_totales += self.calificaciones[i]

        for i in range(1, 6, 1):
            if i in self.calificaciones:
                porcentaje_calculado = (self.calificaciones[i] / calificaciones_totales) * 100
                porcentaje_calculado = round(porcentaje_calculado)
                porcentajes_por_estrella.append(str(porcentaje_calculado) + "%")
        return porcentajes_por_estrella

    def obtener_causas_de_cada_estrella(self):
        causas = {1: "", 2: "", 3: "", 4: "", 5: ""}
        causas_temp = {1: list(), 2: list(), 3: list(), 4: list(), 5: list()}

        for calificacion in self.calificaciones_recibidas:
            causas_temp[calificacion.estrellas].extend(calificacion.causas)

        for estrella, lista_causas in causas_temp.items():
            contador_causas = {}
            for causa in lista_causas:
                if causa is not None:
                    if causa in contador_causas:
                        contador_causas[causa] += 1
                    else:
                        contador_causas[causa] = 1

            causas[estrella] = ", ".join(
                [f"{causa} ({cantidad})" for causa, cantidad in contador_causas.items()])
        return causas


class Pedido:
    def __init__(self, id, estado, cantidad, direccion, productos):
        self.id_pedido = id
        self.estado = estado
        self.cantidad = cantidad
        self.direccion = direccion
        self.productos = productos
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
        calificacion.producto.calificaciones_recibidas.append(calificacion)

class Calificacion:
    def __init__(self, estrellas, causas, producto):
        self.estrellas = estrellas
        self.causas = causas
        self.producto = producto

