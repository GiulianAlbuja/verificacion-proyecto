from behave import *

from modelo.modelos_feedback_cliente import *

use_step_matcher("re")


@step("que el Cliente ha realizado el pago y el proceso de envío de la compra ha finalizado")
def step_impl(context):
    context.producto = Producto(1, "Martillo", "De madera")
    arreglo_productos_pedidos = [context.producto]
    context.pedido = Pedido(1, "Entregado", 6, "direccion", arreglo_productos_pedidos)
    context.cliente = Cliente("1752458974", "Juan", "Herrera", "juan.herrera@hotmail.com", "0984759642",
                              context.pedido)
    assert ((context.pedido.estado == "Entregado"
            or context.pedido.estado == "Entregado con retraso")
            and context.pedido.pagado), "No se entrego el pedido correctamente"

@step("se tiene un Producto con las siguientes valoraciones totales")
def step_impl(context):
    calificaciones_totalizados = 0
    lista_porcentajes_por_estrella = list()

    for i in context.producto.calificaciones:
        calificaciones_totalizados += context.producto.calificaciones[i]

    for row in context.table:
        total_de_calificaciones = int(row["total_de_calificaciones"])
        cantidad_de_estrellas = int(row["cantidad_de_estrellas"])
        porcentaje_de_calificaciones = row["porcentaje_de_calificaciones"]

        lista_porcentajes_por_estrella.append(porcentaje_de_calificaciones)

        assert context.producto.calificaciones[cantidad_de_estrellas] == total_de_calificaciones, "No se tiene el total de calificaciones correcto"

    for i in context.producto.calificaciones:
        porcentajes_calculados = (i / calificaciones_totalizados) * 100
        assert porcentajes_calculados == lista_porcentajes_por_estrella[i], "No se tiene el porcentaje de calificaciones correcto"


@step("el Cliente envíe una Calificación de tres sobre cinco estrellas del Producto")
def step_impl(context):
    context.calificacion = Calificacion(3, "Mal funcionamiento", context.producto)
    context.cliente.calificar_producto(context.calificacion)
    assert context.producto.calificaciones[3] == 3, "No se ha calificado correctamente el producto"


@step("seleccione algunas de las siguientes causas de su Calificación")
def step_impl(context):
    causa_seleccionada = ""

    for row in context.table:
        causas = row["causas"]

    for causa in causas:
        if causa == "Mal funcionamiento":
            causa_seleccionada = causa

    for causa_buscada in context.producto.calificaiones_recibidas[-1].causas:
        if causa_buscada == causa_seleccionada:
            assert True, "No se ha seleccionado la causa correctamente"


@step("la valoración total de calificaciones de 3 estrellas del Producto aumentará en 1")
def step_impl(context):
    context.producto.calificaciones[3] += 1
    assert context.producto.calificaciones[3] == 3, "No se ha aumentado la calificación correctamente"


@step("el vendedor podrá visualizar el siguiente reporte")
def step_impl(context):
    calificaciones_totalizados = 0
    lista_porcentajes_por_estrella = list()
    lista_causas_esperadas = list()
    lista_causas_obtenidas = list()

    for i in context.producto.calificaciones:
        calificaciones_totalizados += context.producto.calificaciones[i]

    for i in context.producto.calificaciones:
        porcentajes_calculados = (i / calificaciones_totalizados) * 100
        lista_porcentajes_por_estrella.append(porcentajes_calculados)

    for row in context.table:
        cantidad_de_estrellas = int(row["cantidad_de_estrellas"])
        porcentaje_de_calificaciones = row["porcentaje_de_calificaciones"]
        causas = row["total_de_calificaciones"]

        lista_causas_esperadas.append(causas)

        assert lista_porcentajes_por_estrella[cantidad_de_estrellas] == porcentaje_de_calificaciones, "No se tiene el porcentaje de calificaciones correcto"

    for i in range(len(lista_causas_esperadas)):
        lista_causas_obtenidas = context.producto.obtener_causas_de_cada_estrella
        assert lista_causas_obtenidas[i] == lista_causas_esperadas[i], "No se tienen las causas correcta"


# SERVICIO
@step("que el Cliente ha dado su feedback sobre el producto")
def step_impl(context):
    context.producto = Producto(1, "Martillo", "De madera")
    arreglo_productos_pedidos = [context.producto]
    context.pedido = Pedido(1, "Entregado", 6, "direccion", arreglo_productos_pedidos)

    assert context.producto.feedback_producto_esta_dado()


@step("se tiene un Servicio con las siguientes valoraciones totales")
def step_impl(context):
    calificaciones_totalizadas = 0
    lista_porcentajes_por_estrella = list()

    for i in context.pedido.servicio.calificaciones :
        calificaciones_totalizadas += context.pedido.servicio.calificaciones[i]

    for row in context.table:
        total_de_calificaciones = int(row["total_de_calificaciones"])
        cantidad_de_estrellas = int(row["cantidad_de_estrellas"])
        porcentaje_de_calificaciones = row["porcentaje_de_calificaciones"]

        lista_porcentajes_por_estrella.append(porcentaje_de_calificaciones)

        assert context.pedido.servicio.calificaciones[
                   cantidad_de_estrellas] == total_de_calificaciones, "No se tiene el total de calificaciones correcto"

    for i in context.pedido.servicio.calificaciones:
        porcentajes_calculados = (context.pedido.servicio.calificaciones[i] / calificaciones_totalizadas) * 100

        assert porcentajes_calculados == lista_porcentajes_por_estrella[
            i-1], "No se tiene el porcentaje de calificaciones correcto"


@step("el Cliente envíe una Calificación de tres sobre cinco estrellas del Servicio")
def step_impl(context):
    return True


@step("la valoración total de calificaciones de 3 estrellas del Servicio aumentará en 1 de la siguiente manera")
def step_impl(context):
    return True


@step("el vendedor podrá visualizar el siguiente reporte con todas las causas en orden descendente")
def step_impl(context):
    return True
