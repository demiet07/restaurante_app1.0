# main.py
from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

def ejecutar_sistema():
    # 1. Instanciar el servicio principal
    mi_restaurante = Restaurante("Sabores Orientales")

    # 2. Crear objetos de tipo Platillo (Mínimo 2)
    platillo1 = Platillo("Ramen de Cerdo", 12.50, tiempo_preparacion=20)
    platillo2 = Platillo("Sushi Roll California", 8.90, tiempo_preparacion=15)

    # 3. Crear objetos de tipo Bebida (Mínimo 2)
    bebida1 = Bebida("Té Verde Helado", 2.50, tamano_ml=400)
    bebida2 = Bebida("Sake Tradicional", 15.00, tamano_ml=300)

    print("\n--- Cargando Productos al Sistema ---")
    # 4. Registrar los objetos en el servicio Restaurante
    mi_restaurante.agregar_producto(platillo1)
    mi_restaurante.agregar_producto(platillo2)
    mi_restaurante.agregar_producto(bebida1)
    mi_restaurante.agregar_producto(bebida2)

    # 5. Mostrar el menú inicial (Demostración de Polimorfismo)
    mi_restaurante.mostrar_menu()

    # 6. Demostración de Encapsulación y Validación de datos
    print("--- Pruebas de Encapsulación y Modificación de Precios ---")
    
    # Intentar cambiar a un precio válido
    print(f"Precio actual de {platillo1.nombre}: ${platillo1.obtener_precio()}")
    platillo1.cambiar_precio(13.99)
    print(f"Nuevo precio de {platillo1.nombre}: ${platillo1.obtener_precio()}\n")

    # Intentar cambiar a un precio inválido (Negativo)
    platillo1.cambiar_precio(-5.00) 
    
    # Mostrar el menú final reflejando los cambios autorizados
    mi_restaurante.mostrar_menu()

if __name__ == "__main__":
    ejecutar_sistema()