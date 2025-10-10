# Documentación del Proyecto

## Información, pasos, pseudocódigo y diagrama del programa (Sprint 1)
En esta etapa, el programa funciona como un visor interactivo de la documentación, para que el usuario obtenga rápidamente la información clave del proyecto desde la terminal.

### Contenidos accesibles desde el menú
1. Tema, problema y solución.
2. Dataset de referencia. Resumen de fuente y definición.
3. Estructura por tabla. Columnas y tipo.
4. Escalas de medición. Descripción y ejemplos.
5. Sugerencias y mejoras con Copilot.
6. Salir.

### Pasos
1) Cargar en memoria los textos leyendo textos.py.
2) Mostrar un menú numérico con las secciones enumeradas arriba.
3) Según la opción elegida, imprimir el texto correspondiente en pantalla.
4) Permitir volver al menú hasta seleccionar “Salir”.

### Pseudocódigo
Inicio 
    Importar diccionario de datos llamado "documentacion" desde textos.py

    Mientras Verdadero hacer:
        Mostrar "Menú de Documentación"
        Mostrar "1. Tema, problema y solución"
        Mostrar "2. Dataset de referencia"
        Mostrar "3. Estructura por tabla"
        Mostrar "4. Escalas de medición"
        Mostrar "5. Sugerencias y mejoras con Copilot"
        Mostrar "6. Salir"

        Leer opción del usuario

        Si opción pertenece a "documentacion" entonces
            Mostrar el texto correspondiente a opción en "documentacion"

            Si opción es igual a "6" entonces
                Romper bucle
            FinSi
        Sino
            Mostrar "Opción inválida. Por favor, elegí un número del 1 al 6."
        FinSi
    FinMientras
Fin

### Diagrama de flujo
 Imagen adjunta en carpeta


## 1. Tema, problema y solución
Este proyecto simula la gestión de una Tienda a partir de datos sintéticos.
El objetivo es disponer de un escenario consistente para practicar análisis, visualización y modelado.

**Tema:** Optimización del desempeño comercial de la tienda  
**Problemática:** La tienda carece de un análisis organizado y estructurado sobre sus clientes, productos y ventas.  
**Solución:** Limpieza, análisis y visualización de los datos proporcionados por la gerencia del local.

## 2. Dataset de referencia: fuente, definición, estructura, tipos y escala de medición
Fuente: datos generados con fines educativos.  
Definición: base que representa una Tienda, con catálogo de productos, registro de clientes y operaciones de venta.

## 3. Estructura por tabla (tipo y escala)

### Productos (`productos.csv`)  ~100 filas
| Campo           | Tipo | Escala   |
|-----------------|------|----------|
| id_producto     | int  | Nominal  |
| nombre_producto | str  | Nominal  |
| categoria       | str  | Nominal  |
| precio_unitario | int  | Razón    |

### Clientes (`clientes.csv`)  ~100 filas
| Campo          | Tipo | Escala    |
|----------------|------|-----------|
| id_cliente     | int  | Nominal   |
| nombre_cliente | str  | Nominal   |
| email          | str  | Nominal   |
| ciudad         | str  | Nominal   |
| fecha_alta     | date | Intervalo |

### Ventas (`ventas.csv`)  ~120 filas
| Campo         | Tipo | Escala    |
|---------------|------|-----------|
| id_venta      | int  | Nominal   |
| fecha         | date | Intervalo |
| id_cliente    | int  | Nominal   |
| nombre_cliente| str  | Nominal   |
| email         | str  | Nominal   |
| medio_pago    | str  | Nominal   |

### Detalle_Ventas (`detalle_ventas.csv`)  ~343 filas
| Campo           | Tipo | Escala   |
|-----------------|------|----------|
| id_venta        | int  | Nominal  |
| id_producto     | int  | Nominal  |
| nombre_producto | str  | Nominal  |
| cantidad        | int  | Razón    |
| precio_unitario | int  | Razón    |
| importe         | int  | Razón    |


## 4. Escalas de medición
- **Nominal:** categorías sin orden (ej. ciudad, nombre).
- **Ordinal:** categorías con orden (ej. talles, niveles de satisfacción).
- **Intervalo:** diferencias significativas pero sin cero absoluto (ej. fechas).
- **Razón:** valores numéricos con cero absoluto (ej. precio, cantidad).

## 5. Sugerencias y mejoras con Copilot
- Separar la documentación en plantillas reutilizables.
- Realizar documentacion en el archivo Documentacion.md
- Analizar las tablas

### Analisis de tablas
Se registraron los siguientes errores de datos en las tablas:

**Tabla: productos**
Inconsistencia en la categoría:

Hay productos como “Pepsi”, “Fanta”, “Yerba Mate Intensa”, “Helado Chocolate”, etc., que están asignados a la categoría “Limpieza” cuando claramente son alimentos o bebidas.

Esto afecta cualquier análisis por categoría, visualización o segmentación.

**Tabla: clientes**
Duplicación de nombres con emails distintos.

Hay varios casos donde el mismo nombre aparece más de una vez con diferente email, lo que puede indicar:
Clientes distintos con mismo nombre (válido)
O bien duplicados mal cargados

Ejemplos:
Bruno Castro → dos registros con bruno.castro@mail.com y bruno.castro2@mail.com
Karina Acosta → dos registros con karina.acosta@mail.com y karina.acosta2@mail.com
Olivia Perez → dos registros con olivia.perez@mail.com y olivia.perez2@mail.com
Agustina Martinez → dos registros con agustina.martinez@mail.com y agustina.martinez2@mail.com

Recomendación: Validar si son personas distintas o duplicados. Si son duplicados, consolidar.

**Tabla: ventas**
Acarrea el “error” de clientes
Ejemplo:
Bruno Castro aparece con id_cliente 8 y 34, y dos emails (bruno.castro@mail.com y bruno.castro2@mail.com).
Recomendación: Validar si son clientes distintos o duplicados mal cargados. Si son duplicados, consolidar en la tabla de clientes y corregir en ventas.

**Tabla: detalle_ventas**
Unificar los productos con el mismo id_producto y el mismo id_venta en un solo detalle de venta

Ejemplo:
| 118 | 68 | Vino Blanco 750ml | 5 |
| 118 | 68 | Vino Blanco 750ml | 3 |

Debería ser:
| 118 | 68 | Vino Blanco 750ml | 8 |


## 6. Salida
Se cerrará el visor. ¡Hasta luego!
