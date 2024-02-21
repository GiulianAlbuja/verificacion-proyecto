#language:es
Característica: Recolección de feedback de compras de los clientes (servicio/producto)
  Como vendedor
  quiero que mis clientes puedan calificar el producto y el servicio después del proceso de compra de un producto
  para aprender de los resultados y mejorar la satisfacción de mis clientes.

  Escenario: Obtener feedback de las calificaciones de los clientes sobre el producto
    Dado que el Cliente ha realizado el pago y el proceso de envío de la compra ha finalizado
    Y se tiene un Producto con las siguientes valoraciones totales
      | total de calificaciones | cantidad de estrellas | porcentaje de calificaciones |
      | 10                      | 5                     | 30%                          |
      | 5                       | 4                     | 16%                          |
      | 2                       | 3                     | 6%                           |
      | 6                       | 2                     | 18%                          |
      | 10                      | 1                     | 30%                          |
    Cuando el Cliente envíe una Calificación de tres sobre cinco estrellas del Producto
    Y seleccione algunas de las siguientes causas de su Calificación
      | causas                          |
      | Buenos acabados                 |
      | Concuerda con la descripción    |
      | Buena calidad de materiales     |
      | Buen funcionamiento             |
      | No concuerda con la descripción |
      | Mala calidad de materiales      |
      | Malos acabados                  |
      | Mal funcionamiento              |
    Entonces la valoración total de calificaciones de 3 estrellas del Producto aumentará en 1 de la siguiente manera
      | total de calificaciones | cantidad de estrellas |
      | 3                       | 3                     |
    Y el vendedor podrá visualizar  el siguiente reporte
      | Cantidad de estrellas | Porcentaje de calificaciones | causas                                          |
      | 1                     | 29%                          | No concuerda con la descripción, Malos acabados |
      | 2                     | 15%                          | Mala calidad de materiales, Mal funcionamiento  |
      | 3                     | 9%                           | Mal funcionamiento                              |
      | 4                     | 18%                          | Buen funcionamiento, Malos acabados             |
      | 5                     | 29%                          | Buenos acabados                                 |


  Escenario: Obtener feedback de las calificaciones de los clientes sobre el servicio
    Dado que el Cliente ha dado su feedback sobre el producto
    Y se tiene un Servicio con las siguientes valoraciones totales
      | total de calificaciones | cantidad de estrellas | porcentaje de calificaciones |
      | 10                      | 5                     | 30%                          |
      | 5                       | 4                     | 16%                          |
      | 2                       | 3                     | 6%                           |
      | 6                       | 2                     | 18%                          |
      | 10                      | 1                     | 30%                          |
    Cuando el Cliente envíe una Calificación de tres sobre cinco estrellas del Servicio
    Y seleccione algunas de las siguientes causas de su Calificación
      | causas           |
      | Paquete dañado   |
      | Entrega tardía   |
      | Entrega a tiempo |
      | Entrega rápida   |
    Entonces la valoración total de calificaciones de 3 estrellas del Servicio aumentará en 1 de la siguiente manera
      | total de calificaciones | cantidad de estrellas |
      | 3                       | 3                     |
    Y el vendedor podrá visualizar el siguiente reporte con todas las causas en orden descendente
      | Cantidad de estrellas | Porcentaje de calificaciones | causas                           |
      | 1                     | 10%                          | Paquete dañado (4)                  |
      | 2                     | 5%                           | Entrega tardía (2)                  |
      | 3                     | 5%                           | Entrega a tiempo (3), Paquete dañado (1) |
      | 4                     | 10%                          | Paquete dañado (3), Entrega rápida (2)   |
      | 5                     | 70%                          | Entrega a tiempo (1)                |
