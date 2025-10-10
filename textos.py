# Aquí pongo el texto de la documentación, presentada en forma de diccionario
documentacion = {
    "1": """Tema, problema y solución
Este proyecto simula la gestión de una Tienda a partir de datos sintéticos.
El objetivo es disponer de un escenario consistente para practicar análisis, visualización y modelado.

Tema: Optimización del desempeño comercial de la tienda
Problemática: La tienda carece de un análisis organizado y estructurado sobre sus clientes, productos y ventas.
Solución: Limpieza, análisis y visualización de los datos proporcionados por la gerencia del local.
""",
    "2": """Dataset de referencia: fuente, definición, estructura, tipos y escala de medición
Fuente: datos generados con fines educativos.
Definición: base que representa una Tienda, con catálogo de productos, registro de clientes y operaciones de venta.
""",
    "3": """Estructura por tabla (tipo y escala)

Productos (productos.csv)  ~100 filas
| Campo            | Tipo | Escala   |
|------------------|------|----------|
| id_producto      | int  | Nominal  |
| nombre_producto  | str  | Nominal  |
| categoria        | str  | Nominal  |
| precio_unitario  | int  | Razón    |

Clientes (clientes.csv)  ~100 filas
| Campo            | Tipo | Escala   |
|------------------|------|----------|
| id_cliente       | int  | Nominal  |
| nombre_cliente   | str  | Nominal  |
| email            | str  | Nominal  |
| ciudad           | str  | Nominal  |
| fecha_alta       | date | Intervalo|

Ventas (ventas.csv)  ~120 filas
| Campo            | Tipo | Escala   |
|------------------|------|----------|
| id_venta         | int  | Nominal  |
| fecha            | date | Intervalo|
| id_cliente       | int  | Nominal  |
| nombre_cliente   | str  | Nominal  |
| email            | str  | Nominal  |
| medio_pago       | str  | Nominal  |

Detalle_Ventas (detalle_ventas.csv)  ~343 filas
| Campo            | Tipo | Escala   |
|------------------|------|----------|
| id_venta         | int  | Nominal  |
| id_producto      | int  | Nominal  |
| nombre_producto  | str  | Nominal  |
| cantidad         | int  | Razón    |
| precio_unitario  | int  | Razón    |
| importe          | int  | Razón    |
""",
    "4": """Escalas de medición
- Nominal: categorías sin orden (ej. ciudad, nombre).
- Ordinal: categorías con orden (ej. talles, niveles de satisfacción).
- Intervalo: diferencias significativas pero sin cero absoluto (ej. fechas).
- Razón: valores numéricos con cero absoluto (ej. precio, cantidad).
""",
    "5": """Sugerencias y mejoras con Copilot
- Separar la documentación en plantillas reutilizables.
- Realizar documentacion en el archivo Documentacion.md
- Analizar las tablas
""",
    "6": "Se cerrará el visor. ¡Hasta luego!"
}