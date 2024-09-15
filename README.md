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
.

## Preprocesamiento de datos
