from behave import *

from modelo.ModeloFeedback import *

use_step_matcher("re")


@step("que el Cliente ha realizado el pago y el proceso de envío de la compra ha finalizado")
def step_impl(context):
    context.cliente = Cliente("identificador","nombres", "apellidos", "correoElectronico", "numeroTelefonico")
    context.producto = Producto("identificador", "nombre", "descripcion", "calificacion")
    context.servicio = Servicio()
    context.pedido = Pedido("identificador", "estado", "cantidad", "direccion", context.cliente, context.producto, context.servicio)

    assert context.pedido.estado == "Entregado" and context.pedido.pagado, "No se entrego el pedido correctamente"


@step(
    "el Cliente envíe una Calificación entre uno y cinco estrellas del Producto y del Servicio, y mencione los motivos de su Calificación\.")
def step_impl(context):
    context.calificacion_producto = context.producto.calificacion
    context.calificacion_servicio = context.servicio.calificacion
    context.motivos_calificacion_producto = context.producto.obtener_motivos_calificacion_producto()
    context.motivos_calificacion_servicio = context.servicio.obtener_motivos_calificacion_servicio()
    assert (
        1 <= context.calificacion_producto <= 5
        and 1 <= context.calificacion_servicio <= 5
        and context.motivos_calificacion_producto is not None and len(context.motivos_calificacion_producto) > 0
        and context.motivos_calificacion_servicio is not None and len(context.motivos_calificacion_servicio) > 0
    ), "La calificación del producto o del servicio no es válida o los motivos no han sido proporcionados"


@step("la valoración total de calificaciones del (?P<item_de_calificacion>.+)  aumentarán")
def step_impl(context, item_de_calificacion):

    raise NotImplementedError(
        u'STEP: Entonces la valoración total de calificaciones del <item_de_calificacion>  aumentarán')


@step(
    "el vendedor podrá visualizar que el (?P<porcentaje>.+) de calificaciones de (?P<cantidad>.+) estrellas son por las (?P<causas>.+) correspondientes al (?P<item_de_calificacion>.+)\.")
def step_impl(context, porcentaje, cantidad, causas, item_de_calificacion):

    raise NotImplementedError(
        u'STEP: Y el vendedor podrá visualizar que el <porcentaje> de calificaciones de <cantidad> estrellas son por las <causas> correspondientes al <item_de_calificacion>.')