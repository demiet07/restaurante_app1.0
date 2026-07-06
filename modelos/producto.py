# modelos/producto.py

class Producto:
    def __init__(self, nombre: str, precio_inicial: float, disponible: bool = True):
        """Constructor de la clase padre Producto."""
        self.nombre = nombre
        self.disponible = disponible
        # Atributo encapsulado (privado) mediante doble guion bajo
        self.__precio = 0.0
        
        # Asignamos el precio inicial usando el método de validación
        self.cambiar_precio(precio_inicial)

    def obtener_precio(self) -> float:
        """Getter para acceder de forma segura al precio encapsulado."""
        return self.__precio

    def cambiar_precio(self, nuevo_precio: float) -> None:
        """Setter para modificar el precio con validación integrada."""
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print(f"[Error]: El precio de '{self.nombre}' debe ser mayor a cero. No se aplicó el cambio.")

    def mostrar_informacion(self) -> str:
        """Método base para mostrar los datos comunes del producto."""
        estado = "Disponible" if self.disponible else "No disponible"
        return f"Producto: {self.nombre} | Precio: ${self.obtener_precio():.2f} | Estado: {estado}"