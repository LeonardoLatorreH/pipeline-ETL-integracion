# Pipeline ETL — Integración de Datos E-Commerce

Pipeline ETL desarrollado en Python para extraer, transformar y cargar datos de e-commerce hacia una base de datos MySQL. El proyecto cubre el flujo completo desde la lectura de archivos fuente hasta la persistencia en un modelo relacional, con manejo de errores, logging y validación de datos.

---

## Objetivo

Automatizar el flujo de integración de datos de múltiples fuentes CSV hacia una base de datos relacional MySQL, aplicando transformaciones de limpieza y validación en cada etapa del pipeline.

---

## Dataset

Brazilian E-Commerce Public Dataset by Olist — dataset público con 100K órdenes reales de e-commerce en Brasil durante 2016–2018.  
Fuente: [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)  
Archivos: 9 CSVs | +100,000 registros | Modelo relacional con 8 tablas

---

## Estructura del repositorio

```
pipeline-etl-integracion/
│
├── data/
│   ├── raw/              # CSVs originales sin modificar (no versionados)
│   └── processed/        # Datos procesados (no versionados)
│
├── logs/                 # Logs de ejecución (no versionados)
│
├── sql/
│   └── 01_create_tables.sql   # Esquema relacional en MySQL
│
├── src/
│   ├── extract.py        # Módulo de extracción
│   ├── transform.py      # Módulo de transformación y limpieza
│   ├── load.py           # Módulo de carga a MySQL
│   └── main.py           # Orquestador del pipeline
│
├── images/               # Capturas del proceso y resultados
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Flujo del pipeline

**1. Extract — `extract.py`**  
Lee los 9 CSVs de Olist desde `data/raw/` con Pandas. Registra cantidad de registros y columnas por archivo.

**2. Transform — `transform.py`**  
Limpieza y normalización de cada tabla: eliminación de duplicados, manejo de nulos, conversión de fechas, estandarización de columnas.

**3. Load — `load.py`**  
Conecta a MySQL con SQLAlchemy. Desactiva foreign keys temporalmente para respetar el orden de carga. Valida DataFrames antes de cargar, elimina duplicados y registra cada operación con logging. Manejo de errores con rollback automático.

**4. Main — `main.py`**  
Orquesta el pipeline completo — llama extract → transform → load en secuencia con logs de cada paso. Lee credenciales desde `.env`.

---

## Modelo de datos

8 tablas relacionales cargadas en MySQL con integridad referencial mediante foreign keys.

![Modelo relacional](images/diagramabd.png)

---

## Ejecución del pipeline

Log completo de la ejecución — extract, transform y load con registros procesados por tabla.

![Log del pipeline](images/pipeline.png)

---

## Validación en MySQL

### Tablas creadas

![Show Tables](images/02_show_tables.png)

### Conteo de registros por tabla

![Conteo registros](images/03_conteo_registros.png)

---

## Análisis exploratorio post-carga

### Top 10 categorías por ingresos

![Top categorías](images/04_top_categorias.png)

### Distribución de métodos de pago

![Distribución pagos](images/05_distribucion_pagos.png)

### Promedio de review score por categoría

![Review score](images/06_review_score.png)

---

## Configuración

Crea un archivo `.env` en la raíz del proyecto:

```
DB_USER=root
DB_PASSWORD=tu_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=olist_etl
```

---

## Ejecución

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el pipeline
cd src
python main.py
```

---

## Stack tecnológico

`Python` `Pandas` `SQLAlchemy` `PyMySQL` `MySQL` `python-dotenv` `Git`

---

## Mejoras futuras

- Implementar UPSERT para evitar duplicados en cargas repetidas
- Agregar métricas de calidad de datos por tabla
- Orquestación con Apache Airflow
- Soporte para múltiples motores de base de datos (PostgreSQL, SQL Server)
- Logging con timestamps y duración por etapa

---
