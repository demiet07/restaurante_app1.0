# modelos/bebida.py
from modelos.producto import Producto

class Bebida(Producto):
    def __init__(self, nombre: str, precio: float, tamano_ml: int, disponible: bool = True):
        """Constructor de Bebida que invoca al de la clase padre."""
        super().__init__(nombre, precio, disponible)
        # Atributo específico de la clase hija
        self.tamano_ml = tamano_ml  # Volumen en mililitros

    def mostrar_informacion(self) -> str:
        """Sobrescribe el método del padre para demostrar Polimorfismo."""
        info_base = super().mostrar_informacion()
        return f"{info_base} | Tipo: Bebida | Tamaño: {self.tamano_ml}ml"