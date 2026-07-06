# servicios/restaurante.py

class Restaurante:
    def __init__(self, nombre_establecimiento: str):
        """Inicializa el servicio con una lista vacía de productos."""
        self.nombre_establecimiento = nombre_establecimiento
        self.__lista_productos = []

    def agregar_producto(self, producto) -> None:
        """Añade un producto (Platillo o Bebida) a la lista."""
        self.__lista_productos.append(producto)
        print(f"[Sistema]: '{producto.nombre}' ha sido registrado con éxito.")

    def mostrar_menu(self) -> None:
        """Recorre la lista aplicando Polimorfismo al llamar a mostrar_informacion()."""
        print(f"\n======================================")
        print(f"   MENÚ DE: {self.nombre_establecimiento.upper()}   ")
        print(f"======================================")
        
        if not self.__lista_productos:
            print("El menú se encuentra vacío en este momento.")
            return

        for producto in self.__lista_productos:
            # Polimorfismo puro: Python sabe en tiempo de ejecución si llama 
            # al 'mostrar_informacion' de un Platillo o de una Bebida.
            print(producto.mostrar_informacion())
        
        print(f"======================================\n")