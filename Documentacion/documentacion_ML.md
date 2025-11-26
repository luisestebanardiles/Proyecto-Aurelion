# Documentación del Modelo de Machine Learning

## Objetivo

El objetivo del modelo es clasificar a cada cliente en dos categorías según su nivel de gasto:

Bajo: importe < 5.000

Alto: importe ≥ 5.000

Este es un problema de clasificación binaria, ya que se busca asignar cada registro a una de dos clases posibles.

## Algoritmo elegido: Regresion logística

Se selecciona el algoritmo de Regresión Logística porque está diseñado específicamente para problemas de clasificación binaria.

## Variables

### variable de salida (y) 


La variable objetivo será una variable binaria creada a partir del importe:

y= ventas_altas

y = 1 → Cliente de gasto alto (importe ≥ 5000)

y = 0 → Cliente de gasto bajo (importe < 5000)

### Variables de entrada (X)

Están compuestas por todas las características independientes que pueden influir en la predicción de la clase.

X: precio_unitario, cantidad, categoria, medio_pago, ciudad

## Métricas de evaluación

### Accuracy (Exactitud)

Porcentaje de predicciones correctas sobre el total.

### Matriz de confusión

Permite ver cuántos casos fueron correctamente y incorrectamente clasificados.

## Modelo ML implementado

El modelo implementado es regresion logistica 

Calcula la probabilidad de que una venta sea "Alta" (Clase 1). Si la probabilidad es mayor al 50%, lo clasifica como 1; si es menor, como 0.

## Division train/test y entrenamiento

Hacemos una division donde usamos el 80% de los datos para entrenar el modelo y el 20% restante queda para prueba del modelo y ver que tan bueno es


## Predicciones y metricas calculadas

Se calcularon:

- Matriz de Confusión

- Precision

- Recall

- F1-Score

- Accuracy

## Resultados en graficos

Se generaron las siguientes visualizaciones:

- Matriz de Confusión

- Curva ROC

- Correlaciones