El archivo **limpieza_datos.ipynb**  contiene un flujo de trabajo para la limpieza y validación de datos en varios datasets (ventas, detalle_ventas, clientes, productos). Aquí está un resumen de su contenido:

1. Importación de librerías
Se utiliza pandas para la manipulación de datos.
2. Carga de datasets
Los datasets se cargan desde la carpeta datasets:
    ventas.xlsx
    detalle_ventas.xlsx
    clientes.xlsx
    productos.xlsx
3. Exploración inicial
Dimensiones de los datasets: Se imprime el número de filas y columnas de cada dataset.
Información general: Se revisan los tipos de datos y la cantidad de valores no nulos.
Primeras filas: Se muestran las primeras filas de cada dataset para entender su estructura.
4. Verificación de valores nulos y duplicados
Valores nulos: Se verifica si hay valores nulos en cada dataset.
Duplicados: Se revisa si hay filas duplicadas en cada dataset.
5. Validaciones específicas
Duplicados en nombre_cliente: Se identifican filas donde nombre_cliente está duplicado.
Clientes en ventas: Se valida que todos los id_cliente en ventas existan en clientes.
Productos en detalle de ventas: Se valida que todos los id_producto en detalle_ventas existan en productos.
6. Limpieza de datos
Valores nulos: Se sugieren métodos para eliminar o rellenar valores nulos.
Duplicados: Se sugieren métodos para eliminar filas duplicadas.
7. Estadísticas básicas
Se calculan estadísticas descriptivas para las columnas numéricas de detalle_ventas.
8. Resultados de validaciones
Se concluye que no hay valores nulos ni duplicados en los datasets principales.
Se valida que todos los id_cliente y id_producto en los datasets relacionados existen en sus respectivos datasets de referencia.
