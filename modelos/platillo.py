# modelos/platillo.py
from modelos.producto import Producto

class Platillo(Producto):
    def __init__(self, nombre: str, precio: float, tiempo_preparacion: int, disponible: bool = True):
        """Constructor de Platillo que invoca al de la clase padre."""
        super().__init__(nombre, precio, disponible)
        # Atributo específico de la clase hija
        self.tiempo_preparacion = tiempo_preparacion  # Medido en minutos

    def mostrar_informacion(self) -> str:
        """Sobrescribe el método del padre para demostrar Polimorfismo."""
        info_base = super().mostrar_informacion()
        return f"{info_base} | Tipo: Platillo | Prep: {self.tiempo_preparacion} min"