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


## Descripción del Proyecto

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

# Funciones de la API

El proyecto también incluye la implementación de una API para proporcionar acceso a datos procesados y funcionalidades específicas. Esta fue desarrollada en el archivo main.py. Las principales funciones de la API incluyen:

1. def cantidad_filmaciones_mes( `Mes` ): Se ingresa un mes en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en el mes consultado en la totalidad del dataset.
                    Ejemplo de retorno: `X` cantidad de películas fueron estrenadas en el mes de `X`

2. def cantidad_filmaciones_dia( `Dia` ): Se ingresa un día en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en día consultado en la totalidad del dataset.
                    Ejemplo de retorno: `X` cantidad de películas fueron estrenadas en los días `X`

3. def score_titulo( `titulo_de_la_filmación` ): Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score.
                    Ejemplo de retorno: La película `X` fue estrenada en el año X con un score/popularidad de `X`

4. def votos_titulo( `titulo_de_la_filmación` ): Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones. La misma variable deberá de contar con al menos 2000 valoraciones, caso contrario, debemos contar con un mensaje avisando que no cumple esta condición y que por ende, no se devuelve ningun valor.
                    Ejemplo de retorno: La película X fue estrenada en el año X. La misma cuenta con un total de `X` valoraciones, con un promedio de `X`

5. def get_actor( `nombre_actor` ): Se ingresa el nombre de un actor que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, la cantidad de películas que en las que ha participado y el promedio de retorno. La definición no deberá considerar directores.
                    Ejemplo de retorno: El actor `X` ha participado de X cantidad de filmaciones, el mismo ha conseguido un retorno de `X` con un promedio de `X` por filmación

6. def get_director( `nombre_director` ): Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.

    Para más información se puede consultar la documentación de la api en : [https://proyecto-i-44rn.onrender.com/docs](https://proyecto-i-44rn.onrender.com/docs)

# Deployment 

La API puede ser probada en local utilizando uvicorn con el siguiente comando dentro de la carpeta raíz del proyecto:

```python
uvicorn main:app --reload
```

la API está deployada en Render, cada modificación hecha en el archivo main.py se verá de forma automática en uvicorn, pero debe ser actualizada manualmente en el Deploy de Render.
