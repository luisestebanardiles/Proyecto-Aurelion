# Instrucciones para GitHub Copilot

## Comportamiento del asistente
- El tono debe ser amable, empático y claro.
- No dar información inventada.
- Evitar respuestas extensas innecesarias.
- Confirmar con el usuario antes de ejecutar acciones sensibles.
- Priorizar ejemplos y explicaciones paso a paso.


## Estilo general
- Escribir todo el código y comentarios en español.
- Usar nombres de variables descriptivos (por ejemplo, `total_ventas` en lugar de `tv)
- Nombrar variables en snake_case (minúsculas con guiones bajos).
- Incluir comentarios explicativos en cada función.

## Restricciones
- No usar bucles infinitos.
- Evitar librerías externas innecesarias.


## Estructura del código
- Dividir el código en funciones pequeñas y reutilizables.
- Cada función debe realizar una única tarea.
- Evitar repetir código: usar funciones auxiliares si es necesario.


## Estructura del proyecto
- Los archivos de prueba deben estar en `/tests` y comenzar con `test_`.


## Pruebas
- Crear al menos una función de prueba por cada módulo.
- Usar datos realistas en las pruebas.
- Verificar casos extremos (por ejemplo, listas vacías, valores nulos, etc.).


## Documentación
- Cada función debe incluir una docstring que indique:
  - Qué hace la función.
  - Qué parámetros recibe (nombre y tipo de dato).
  - Qué valor devuelve (tipo y descripción).
- Incluir comentarios antes de bloques lógicos importantes.
- Los archivos deben comenzar con un comentario que describa su propósito general.


## Comentarios
- Explicar por qué se toma una decisión importante en el código.
- No describir lo obvio (por ejemplo, no poner “# sumar 1” si la línea ya es `x += 1`).
- Mantener los comentarios actualizados si se modifica el código.


## Dependencias
- No instalar dependencias externas sin aprobación.
- Importar siempre las librerías estándar antes que las externas.