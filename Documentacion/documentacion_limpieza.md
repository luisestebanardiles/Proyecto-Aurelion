# Documentación del notebook `limpieza_datos.ipynb`

> **Objetivo del documento:** explicar de forma clara y didáctica el análisis y limpieza de datos realizado en el notebook, describir los pasos, resultados y ofrecer interpretaciones orientadas al problema.

---

## 1. Resumen general
El notebook realiza un **análisis y limpieza de datos** sobre los siguientes archivos detectados en el código:

- datasets/datasets_originales/ventas.xlsx
- datasets/datasets_originales/detalle_ventas.xlsx
- datasets/datasets_originales/clientes.xlsx
- datasets/datasets_originales/productos.xlsx

- datasets/datasets_limpios/clientes_limpio.xlsx
- datasets/datasets_limpios/productos_limpio.xlsx
- datasets/datasets_limpios/ventas_limpio.xlsx
- datasets/datasets_limpios/detalle_ventas_limpio.xlsx

- datasets/dataset_unificado/ventas_completo.csv

El flujo general incluye: carga y unión de tablas (ventas, detalle_ventas, clientes, productos), cálculo de estadísticas descriptivas, detección de valores faltantes, identificación de outliers, análisis de correlaciones y visualizaciones (histogramas, boxplots y gráficos de barras). Este documento es **explicativo**, pensado para que alguien sin mucha experiencia en Python/pandas entienda qué se hizo y por qué.

---

## 2. Archivos y tablas utilizados
- Los datasets se cargan desde la carpeta datasets/datasets_originales:
    ventas.xlsx
    detalle_ventas.xlsx
    clientes.xlsx
    productos.xlsx
- Los datasets limpios se guardan en datasets/datasets_limpios
- El dataset unificado se guardó en datasets/dataset_unificado

Las tablas son: `ventas`, `detalle_ventas`, `clientes`, `productos`. 

---

## 3. Paso a paso del análisis 

### 3.1 Carga y unificación de datos
- Se cargan las tablas principales: **ventas**, **detalle_ventas**, **clientes** y **productos**. 
Se trabajó con las tablas separadas, ya que no veia necesario unirlas en un comienzo.
Estas tablas suelen unirse porque la información relevante está distribuida: los importes se encuentran en `detalle_ventas`, la información del cliente en `clientes` y la cabecera de la venta en `ventas`.
- Al final se unieron todas las tablas y se lo alojo en un archivo csv, ya que esto será necesario para el proximo sprint
- Operaciones típicas usadas: value_counts, boxplot, corr, merge, groupby, outliers_iqr, plt, seaborn, numpy.

**Por qué:** unir tablas permite crear un dataframe 'completo' donde cada fila representa una venta con su cliente, producto, fecha e importe, lo que habilita análisis por cliente, por producto y por tiempo.

### 3.2 Analisis
- Se hizo un analisis exhaustivo buscando faltantes de datos o errores en la carga de datos
- utilicé funciones para reutilizar codigo
- Documenté cada dato relevante

**Por qué:** Los dataframes son relativamente extensos y lo mas conveniente era analizarlos automaticamente con codigo

### 3.3 Limpieza básica
- Búsqueda y tratamiento de valores nulos con `dropna()` o `fillna()`. Esto evita errores en métricas y gráficas.
- Estandarización de tipos (`fecha` como datetime, identificadores como enteros, `importe` como float).
- Conversión de textos a minúsculas/trim para campos como email o nombres (mejora joins y agregaciones).

**Por qué:** los datos sucios distorsionan resultados — por ejemplo, strings con espacios extras se consideran distintos, o un importe como texto impide calcular sumas/medias.

### 3.4 Estadísticas descriptivas básicas
Se buscó aplicar `describe()` para las variables numéricas y `value_counts()` para las categóricas. Las estadísticas que reportamos son:
- Conteo, media, desviación estándar, mínimos, percentiles (25%, 50%, 75%) y máximo para variables numéricas (`importe`, `cantidad`, `precio_unitario`, etc.).
- Frecuencias para variables categóricas (`medio_pago`, `categoria_producto`, `provincia` o `email_domain`).
- Se identificó el **tipo de distribución**


### 3.5 Análisis de correlaciones entre variables principales
- buscamos correlaciones con `corr()` entre variables numéricas (por ejemplo: `cantidad`, `precio_unitario`, `importe`). También puede usarse `sns.heatmap()` para visualizar la matriz de correlación.


### 3.6 Detección de outliers (valores extremos)
-Se los detectó con el metodo IQR (rango intercuartil) y visualmente.
- Regla IQR típica: valores por debajo de Q1 - 1.5·IQR o por encima de Q3 + 1.5·IQR son considerados atípicos.
- Revisamos cada outlier, lo interpretamos y decidimos que hacer con cada uno.

---

## 4. Gráficos representativos 
- Se graficaron todos los graficos lo que se pensaron necesario para entender mejor visualmente como se comportaban los datos

---

## 5. Interpretación de resultados orientada al problema
- El problema planteado es de que los datos no estaban estructurados y no se podian analizar facilmente, por lo tanto todos lo realizado se empeña en estructurar los datos, y aportarle al cliente una vista general de su negocio.

---
## 6. Se recomienda 
- Recorrer el notebook de arriba hacia abajo e ir ejecutando cada codigo y leyendo su repectivos comentarios
---
