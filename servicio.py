from abc import ABC, abstractmethod
from excepciones import ServicioInvalidoError

class Servicio(ABC):
    def __init__(self, codigo: str, nombre_servicio: str, costo_base: float):
        self.codigo = codigo
        self.nombre_servicio = nombre_servicio
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self, *args, **kwargs) -> float:
        pass

    @abstractmethod
    def describir(self) -> str:
        pass

    def validar_parametros(self) -> bool:
        if self.costo_base < 0:
            raise ServicioInvalidoError("El costo base no puede ser negativo.")
        return True

# ReservaSala (Integrante 2)
class ReservaSala(Servicio):
    def __init__(self, codigo: str, nombre_servicio: str, costo_base: float, capacidad: int):
        super().__init__(codigo, nombre_servicio, costo_base)
        self.capacidad = capacidad

    def calcular_costo(self, horas: int, incluir_proyector: bool = False) -> float:
        if horas <= 0:
            raise ValueError("Las horas deben ser mayores a 0.")
        total = self.costo_base * horas
        if incluir_proyector:
            total += 50.0
        return total

    def describir(self) -> str:
        return f"Sala: {self.nombre_servicio} (Capacidad: {self.capacidad})"

# AlquilerEquipo (Integrante 3)
class AlquilerEquipo(Servicio):
    def __init__(self, codigo: str, nombre_servicio: str, costo_base: float, tipo_hardware: str):
        super().__init__(codigo, nombre_servicio, costo_base)
        self.tipo_hardware = tipo_hardware

    def calcular_costo(self, dias: int, seguro_danos: bool = False) -> float:
        if dias <= 0:
            raise ValueError("Los días deben ser mayores a 0.")
        total = self.costo_base * dias
        if seguro_danos:
            total += 30.0 * dias
        return total

    def describir(self) -> str:
        return f"Equipo: {self.nombre_servicio} ({self.tipo_hardware})"

# AsesoriaEspecializada (Integrante 4 - Tu aporte)
class AsesoriaEspecializada(Servicio):
    def __init__(self, codigo: str, nombre_servicio: str, costo_base: float, especialidad: str):
        super().__init__(codigo, nombre_servicio, costo_base)
        self.especialidad = especialidad

    def calcular_costo(self, sesiones: int, nivel_senior: bool = False) -> float:
        if sesiones <= 0:
            raise ValueError("Las sesiones deben ser mayores a 0.")
        mult = 1.5 if nivel_senior else 1.0
        return (self.costo_base * sesiones) * mult

    def describir(self) -> str:
        return f"Asesoría: {self.nombre_servicio} ({self.especialidad})"
