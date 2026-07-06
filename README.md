# Sistema de Gestión - restaurante_app

**Estudiante:** [Tu Nombre Completo Aquí]  
**Asignatura:** Programación Orientada a Objetos (Semana 6)

## Descripción del Sistema
Este proyecto es una aplicación modular desarrollada en Python que simula la gestión interna de productos dentro de un restaurante. Permite registrar diferentes elementos del menú, diferenciando estructuralmente entre comidas sólidas y bebidas líquidas mediante una organización jerárquica limpia y eficiente.

## Estructura del Proyecto
El diseño del software sigue una arquitectura modular distribuida de la siguiente manera:
- **`modelos/`**: Paquete que almacena las entidades del negocio (`Producto`, `Platillo`, `Bebida`).
- **`servicios/`**: Contiene la lógica operativa y el control de los datos mediante la clase `Restaurante`.
- **`main.py`**: Punto de acceso y orquestador encargado de inicializar el programa.

## Aplicación de Principios POO

### 1. Herencia
Se implementó una estructura jerárquica donde `Producto` actúa como la clase base (padre), proveyendo los atributos comunes (`nombre`, `precio`, `disponible`). Las clases `Platillo` y `Bebida` actúan como clases derivadas (hijas), heredando estos campos mediante la instrucción `super().__init__()` e incorporando atributos especializados como `tiempo_preparacion` y `tamano_ml` respectivamente.

### 2. Encapsulación
El atributo `__precio` dentro de la clase `Producto` se configuró bajo acceso privado (utilizando doble guion bajo). Para interactuar con él, se implementaron métodos públicos de control de acceso (*Getters y Setters*): `obtener_precio()` y `cambiar_precio()`. Este último cuenta con una estructura lógica condicional que prohíbe taxativamente la asignación de valores menores o iguales a cero.

### 3. Polimorfismo
El polimorfismo se evidencia mediante el método `mostrar_informacion()`. La clase padre posee una implementación general que es posteriormente sobreescrita (*override*) por cada clase hija de forma única. Al ejecutarse el bucle del menú dentro del servicio `Restaurante`, el intérprete ejecuta dinámicamente el método correspondiente de acuerdo a la naturaleza exacta del objeto en memoria.

## Reflexión Personal
La modularización combinada con los pilares de la POO permite construir software altamente escalable y mantenible. Al aislar las responsabilidades en archivos independientes, se evita el código acoplado, facilitando que futuros cambios en la estructura de una `Bebida` o un `Platillo` no afecten de forma colateral la lógica del archivo principal o de los servicios de administración.