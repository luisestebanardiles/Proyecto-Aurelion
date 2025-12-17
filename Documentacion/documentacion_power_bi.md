# Documentación del Modelo de Datos y Métricas en power BI

## Objetivo del Dashboard
El objetivo del dashboard es analizar el desempeño de ventas, rentabilidad y comportamiento de clientes,
permitiendo evaluar la evolución temporal, la contribución por categoría y producto,
y métricas clave de clientes como recurrencia, ARPU y retención.

## Decisiones de Modelado
- Se eliminaron columnas redundantes para evitar inconsistencias.
- Se creó una tabla calendario independiente para permitir análisis temporal avanzado.
- Se utilizó DISTINCTCOUNT para métricas de clientes para evitar duplicados.


## 1. Relaciones y Modelo
- Las **relaciones** entre tablas y las **direcciones de los filtros** se generaron de manera automática.
- Relaciones establecidas:
  - `ventas_limpio` ↔ `clientes_limpios` por `id_cliente`
  - `ventas_limpio` ↔ `detalles_ventas_limpio` por `id_venta`
  - `detalles_ventas_limpio` ↔ `productos_limpio` por `id_producto`

---

## 2. Transformaciones por Tabla

### Tabla `detalle`
- Cambio de tipo de dato:
  - `importe`: de entero a **decimal**

- Columnas eliminadas:
  - `nombre_producto` (se repite en producto)
  - `precio_unitario` (se repite en producto)
  - `importe` (se la puede calcular multiplicando el precio unitario * cantidad)

---

### Tabla `venta`
- Cambio de tipo de dato:
  - `fecha`: convertida a **fecha**
- Columnas eliminadas:
  - `nombre_cliente` (se repite en cliente)
  - `email` (se repite en cliente)


---

### Tabla `clientes`
- Cambio de tipo de dato:
  - `fecha_alta`: convertida a **fecha**

---

### Tabla `productos`
- Cambio de tipo de dato:
  - `precio_unitario`: de entero a **decimal**

---

## 3. Organización de Medidas
- Se creó una **tabla de medidas** donde se movieron todas las medidas creadas hasta el momento, con el objetivo de mantenerlas centralizadas y mejorar la organización del modelo.

---

## 4. Tabla Calendario
- Se creó una **tabla calendario** utilizando:
  - Fecha mínima y fecha máxima provenientes de la tabla `ventas`
- Se definió una **jerarquía de fechas**:
  - Año → Mes → Día

---

## 5. Agrupaciones
- Se creó una **agrupación de clientes por nivel de compra** según la cantidad:
  - Poca compra
  - Media compra
  - Mucha compra

---
## 6. Columnas calculadas:
  - **Año**: extrae el año de la transacción a partir de la fecha


## 7. Métricas Principales

 - **% del Total**: 
DIVIDE(
    [Ventas Totales],
    CALCULATE(
        [Ventas Totales],
            ALL(productos)
    )
)


- **% Participación Ventas**: DIVIDE([Ventas Totales], CALCULATE([Ventas Totales], ALL(productos)))

- **ARPU**: DIVIDE([Ventas Totales],[Clientes activos])

- **Cantidad vendida**: SUM(detalle[cantidad])

- **Cantidad Ventas**: COUNTROWS(venta)

- **cartera**: DISTINCTCOUNT(venta[id_cliente])

- **Clientes por Producto**:  DISTINCTCOUNT(venta[id_cliente])

- **Clientes Recurrentes**: 
    CALCULATE(
        DISTINCTCOUNT(venta[id_cliente]),
        FILTER(
            VALUES(venta[id_cliente]),
            CALCULATE(COUNT(venta[id_venta])) > 1
        )
    )

- **Costo Total**
SUMX(
    detalle,
    detalle[cantidad] * RELATED(productos[Valor Neto Producto])
)


- **Crecimiento Ventas Mensual %**: 
VAR VentasActual = [Ventas Totales]
VAR VentasMesAnt = CALCULATE(
    [Ventas Totales],
    PREVIOUSMONTH(calendario[Date])
)
RETURN DIVIDE(VentasActual - VentasMesAnt, VentasMesAnt, 0)

- **Ingresos Totales MTD**:
TOTALMTD([Ventas Totales], calendario[Date])

- **Margen ($)**: [Ventas Totales] - [Costo Total]

- **Margen %**:  DIVIDE(
    [Margen ($)],
    [Ventas Totales]
)

- **Meta Crecimiento Ventas** = 0.05 (fijo)

- **s** = 500000 (fijo)


- **Tasa de Retención**: 
DIVIDE(
    [Clientes Recurrentes],
    [Clientes Activos]
)

- **Ticket Promedio**: 
DIVIDE([Ventas Totales], [Cantidad Ventas])

- **Total ventas**: DISTINCTCOUNT(venta[id_venta])

- **Ventas por MedioPago**: 
CALCULATE(
    [Ventas Totales],
    ALLEXCEPT(venta, venta[medio_pago])
)

- **Ventas Totales**: SUMX( detalle, detalle[cantidad] * RELATED(productos[precio_unitario]))


## 8. Visualizaciones

Lo dividimos en 5 secciones(pestañas):

- **Facturacion por periodo**:

    - Ventas totales en pesos pot mes, donde el mes 5 es el que mayor ingresos se obtuvo
    - Medios de pagos utilizados
    - Cantidad dde clientes activos
    - Monto de ventas totales
    - Cantidad de ventas

    **KPIs**:
        - Crecimiento de ventas: se fijó un 5% de crecimiento con respecto al mes anterior como objetivo
        - Ingresos totales: se fijó como objetivo $500000 por mes


- **Margen por categoria**:

    - Margen de ganancia por mes
    - Margen de ganancia con respecto a la categoria (aqui se incluyeron más categorias para mayor analisis)
    - Lo que aporta cada catergoria con respecto al Margen de ganancia al total

- **Productos**:

    - Top 10 productos mas vendidos
    - Top 10 Productos menos vendidos
    - Correlacion entre las ventas y la cantidad vendida


- **ARPU (Average Revenue Per Use)**:

    - ARPU por mes
    - Clientes que mayor dinero aportan 
    - Top 15 de clientes con mayor aporte

    **KPIs**:
        - ARPU


- **Clientes Activos**:

    - Clientes activos
    - segmentador de periodo

    **KPIs**:
        - Tasa de retencion
        

