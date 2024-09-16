# Machine Learning Operations (MLOps)
Este proyecto consiste en una API para recomendar películas basada en Machine Learning y FastAPI. Fue desarrollado como parte de un proyecto de MLOps.

## Descripción
El sistema de recomendación de películas desarrollado,  es parte de un proyecto individual en el curso de Data Science de *Henry*. Utiliza técnicas de Machine Learning y análisis de datos para sugerir películas a los usuarios en función de sus preferencias y comportamientos.

<p align="center">
  <img src="./pelicula.png" alt="Película" width="600"/>
</p>

Se simula el trabajo de Data Scientist en una start-up que provee servicios de agregación de plataformas de streaming.

## Tabla de Contenidos
1. [Instalación y requisitos](#Instalación-y-requisitos)
2. [Data Engineering](#Data-engineering)
   - [Repositorio y Conjuntos de Datos](#Repositorio-y-conjuntos-de-datos)
   - [Preprocesamiento de Datos](#Preprocesamiento-de-datos)
   - [Descripción del Proyecto](#Descripción-del-proyecto)
3. [Funciones de la API](#funciones-de-la-api)
4. [Deployment y la API](#deployment-y-la-api)
5. [Archivos Generados](#archivos-generados)
6. [Contribuciones y Colaboraciones](#contribuciones-y-colaboraciones)
7. [Links](#links)
8. [Contacto](#contacto)


# Instalación y requisitos

## Requisitos:
- Python 3.7 o superior
- pandas
- numpy
- matplotlib
- scikit-learn

## Pasos de instalación:

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/JoseCruzP/Proyecto_I
   
2. Crear un entorno virtual:
   ```bash
   python -m venv venv

3. Activar el entorno virtual:

   - Windows:
     ```bash
     venv\Scripts\activate

   - macOS/Linux:
     ```bash
     source venv/bin/activate

4. Instalar las dependencias:
   
   ```bash
   pip install -r requirements.txt


# Data Engineering

## Repositorio y conjuntos de datos

 - El repositorio original del proyecto se encuentra disponible en [GitHub](https://github.com/soyHenry/fe-ct-pimlops2)
 - Los conjuntos de datos utilizados se encuentran disponibles en [Google Drive](https://drive.google.com/drive/folders/1X_LdCoGTHJDbD28_dJTxaD4fVuQC9Wt5).
 - El diccionario con algunas descripciones de las columnas se encuentra disponible en [Google Drive](https://docs.google.com/spreadsheets/d/1QkHH5er-74Bpk122tJxy_0D49pJMIwKLurByOfmxzho/edit?gid=0#gid=0).

## Preprocesamiento de datos

Se realiza la carga y limpieza de los conjuntos de datos utilizando Python y las siguientes librerías:

 - ast
 - pandas
 - numpy
 - matplotlib
 - sklearn
 - seaborn

puedes revisar más en detalle los pasos realizados dentro del archivo [ETL_y_EDA_Proyecto_individual_I.ipynb](ETL_y_EDA_Proyecto_individual_I.ipynb)


Descripción del Proyecto

El proceso de ETL (extracción, transformación y carga) se divide en las siguientes secciones principales:

- Exploración inicial de Datos: Análisis inicial de los conjuntos de datos para comprender su estructura y características.
- Limpieza de Datos: Proceso de limpieza y preprocesamiento de los datos para eliminar valores nulos, duplicados y realizar correcciones.
- Transformación de Datos: Conversión de tipos de datos, extracción de información relevante y preparación de los datos para su análisis.

El EDA (análisis exploratorio de datos) se divide en las siguientes secciones principales:

- Resumen general de los datos: Las películas tienen presupuestos y recaudaciones con alta variabilidad, donde muchas tienen valores cercanos a 0. La duración promedio es de 94 minutos y el promedio de votos es de 5.6.

- Valores faltantes: Las columnas más importantes, como budget, genres y revenue, no tienen valores faltantes. Sin embargo, columnas como overview y tagline presentan un número significativo de datos faltantes.

- Distribución de variables: La mayoría de las películas tienen presupuestos, ingresos y retornos bajos, mientras que unas pocas alcanzan valores extremadamente altos. El inglés es el idioma dominante y la mayoría de las películas están en estado "Released".

- Relaciones entre variables: Existe una correlación positiva entre el número de votos, el presupuesto y los ingresos, lo que sugiere que películas con mayor presupuesto tienden a generar más votos e ingresos.

- Análisis temporal: La producción y los ingresos de películas aumentan significativamente a partir de los años 80, con un pico hacia el 2000. La cantidad de películas producidas crece exponencialmente hasta 2015, pero decrece ligeramente después, posiblemente debido al impacto del COVID-19.

- Finalmente, se tomó una muestra de 30,000 filas para el deploy de la API, esto debido al tamaño de archivos soportado por la versión gratuira de [Render](https://render.com/).


