import logging
from cliente import Cliente
from servicio import Servicio
from excepciones import ReservaError, ClienteInvalidoError, ServicioInvalidoError

class Reserva:
    contador = 1000

    def __init__(self, cliente: Cliente, servicio: Servicio):
        Reserva.contador += 1
        self.id_reserva = f"RES-{Reserva.contador}"
        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"
        self.costo_final = 0.0

    def confirmar(self, *args, **kwargs):
        self.procesar(*args, **kwargs)

    def cancelar(self):
        if self.estado == "Confirmada":
            self.estado = "Cancelada"
            logging.info(f"Reserva {self.id_reserva} cancelada.")
            print(f" [CANCELADA] Reserva {self.id_reserva} anulada.")
        else:
            print(f" [AVISO] No se puede cancelar la reserva {self.id_reserva}.")

    def procesar(self, *args, **kwargs):
        try:
            logging.info(f"Procesando {self.id_reserva}")
            if not self.cliente.validar_documento() or not self.servicio.validar_parametros():
                raise ReservaError("Datos inválidos en cliente o servicio.")
            
            self.costo_final = self.servicio.calcular_costo(*args, **kwargs)
            self.estado = "Confirmada"
        except (ClienteInvalidoError, ServicioInvalidoError, ValueError) as e:
            self.estado = "Fallida"
            logging.error(f"Error en {self.id_reserva}: {e}")
            raise ReservaError(f"Fallo en reserva: {e}") from e
        except Exception as e:
            self.estado = "Fallida"
            logging.error(f"Error crítico en {self.id_reserva}: {e}")
            raise ReservaError("Error desconocido.") from e
        else:
            logging.info(f"{self.id_reserva} confirmada. Total: {self.costo_final}")
            print(f" [ÉXITO] {self.id_reserva} confirmada. Total: ${self.costo_final}")
        finally:
            print(f" [ESTADO] Fin de intento para {self.id_reserva}. Estado: {self.estado}\n")

    def mostrar_reserva(self):
        return f"Reserva [{self.id_reserva}] - Cliente: {self.cliente.get_nombre()} | Servicio: {self.servicio.describir()} | Estado: {self.estado}"
