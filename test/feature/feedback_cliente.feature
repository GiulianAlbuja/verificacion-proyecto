#language:es
Característica: Recolección de feedback de compras de los clientes (servicio/producto)
  Como vendedor
  quiero que mis clientes puedan calificar el producto y el servicio después del proceso de compra de un producto
  para aprender de los resultados y mejorar la satisfacción de mis clientes.

  Esquema del escenario: Obtener feedback de calificaciones de los clientes
    Dado que el Cliente ha realizado el pago y el proceso de envío de la compra ha finalizado
    Cuando el Cliente envíe una Calificación entre uno y cinco estrellas del Producto y del Servicio, y mencione los motivos de su Calificación.
    Entonces la valoración total de calificaciones del <item_de_calificacion>  aumentarán
    Y el vendedor podrá visualizar que el <porcentaje> de calificaciones de <cantidad> estrellas son por las <causas> correspondientes al <item_de_calificacion>.
    Ejemplos:
      | item_de_calificacion | causas | porcentaje |  cantidad  |
      | Martillo | Buena calidad, Concuerda con la descripción | 70% | 5 |
      | Martillo | Malos acabados, Buena calidad | 10% | 4 |
      | Martillo | No concuerda con la descripción | 10% | 3 |
      | Martillo | Materiales de baja calidad | 5% | 2 |
      | Martillo | Funcionamiento defectuoso, Mala calidad | 5% | 1 |
      | Productos | Buena calidad, Concuerda con la descripción | 70% | 5 |
      | Productos | Malos acabados, Buena calidad | 5% | 4 |
      | Productos | No concuerda con la descripción | 5% | 3 |
      | Productos | Materiales de baja calidad | 10% | 2 |
      | Productos | Funcionamiento defectuoso, Mala calidad | 10% | 1 |
      | Servicio | Entrega a tiempo | 10% | 5 |
      | Servicio | Embalaje inadecuado, Entrega a tiempo | 70% | 4 |
      | Servicio | Entrega tardía | 5% | 3 |
      | Servicio | Paquete dañado, Entrega Tardía | 10% | 2 |
      | Servicio | No entregado | 5% | 1 |