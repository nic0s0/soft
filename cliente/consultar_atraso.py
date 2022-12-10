#se activa este cliente
#registrar "fecha_actual"
#enviar a servicio "consultar_fecha_devolucion" data: "rut", "id_libro"
#recibir "fecha_devolucion" desde servicio
#calcular atraso en "dias_atraso" y "monto_deuda" con "fecha_actual" y "fecha_devolucion"