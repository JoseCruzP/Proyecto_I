
from fastapi import FastAPI
import pandas as pd
from datetime import datetime
from sklearn.metrics.pairwise import cosine_similarity 
import numpy as np


app = FastAPI()

# Carga de bases de datos

# Cargar los DataFrame
peliculas_df = pd.read_csv('movies_df.csv')
credit_df = pd.read_csv('credit_df.csv')


# Funciones para los endpoint

def mes_a_numero(mes: str) -> int:
    """
    Convierte el nombre de un mes en español a su número correspondiente.

    Parámetros:
    mes (str): El nombre del mes en español. Se acepta cualquier combinación de mayúsculas y minúsculas.

    Retorna:
    int: El número del mes correspondiente (1 para enero, 2 para febrero, etc.).
         Retorna 0 si el nombre del mes no es válido.

    Ejemplos:
    >>> mes_a_numero("enero")
    1
    >>> mes_a_numero("Junio")
    6
    >>> mes_a_numero("mes desconocido")
    0
    """
    meses = {
        "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5,
        "junio": 6, "julio": 7, "agosto": 8, "septiembre": 9, "octubre": 10,
        "noviembre": 11, "diciembre": 12
    }
    return meses.get(mes.lower(), 0)



#### End Points ####

# 1. Cantidad de filmaciones por mes
@app.get("/cantidad_filmaciones_mes/{mes}")
def cantidad_filmaciones_mes(mes: str):
    """
    Obtiene la cantidad de películas estrenadas en un mes específico.

    Este endpoint recibe el nombre de un mes y devuelve la cantidad total de películas
    que se estrenaron en ese mes, utilizando el DataFrame `peliculas_df`.

    Parámetros:
    mes (str): El nombre del mes en inglés o español (e.g., "enero", "February").

    Retorna:
    dict: Un diccionario que contiene la cantidad de películas estrenadas en el mes
    especificado. Si el mes es inválido, se devuelve un diccionario de error.

    Ejemplo de respuesta:
    - Si se solicita "junio", la respuesta podría ser:
      {"Cantidad de películas estrenadas en junio": 15}
    - Si se solicita un mes inválido, la respuesta será:
      {"error": "Mes inválido"}
    """
    mes_numero = mes_a_numero(mes)
    if mes_numero == 0:
        return {"error": "Mes inválido"}

    cantidad = sum(1 for fecha in peliculas_df['release_date'] 
                   if datetime.strptime(fecha, "%Y-%m-%d").month == mes_numero)
    
    return {f"Cantidad de películas estrenadas en {mes}": cantidad}


# 2. Cantidad de filmaciones por día
@app.get("/cantidad_filmaciones_dia/{dia}")
def cantidad_filmaciones_dia(dia: str):
    """
    Obtiene la cantidad de películas estrenadas en un día específico de la semana.

    Parámetros:
    dia (str): El día de la semana para el cual se desea obtener la cantidad de películas.
               Debe ser uno de los siguientes: 'lunes', 'martes', 'miércoles', 
               'jueves', 'viernes', 'sábado' o 'domingo'.

    Retorna:
    dict: Un diccionario que contiene la cantidad de películas estrenadas en el día especificado.
          Si el día es inválido, retorna un diccionario con un mensaje de error.

    Ejemplo de uso:
    - Solicitud: GET /cantidad_filmaciones_dia/lunes
    - Respuesta: {"Cantidad de películas estrenadas en lunes": 5}
    """
    dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    dia_numero = dias_semana.index(dia.lower()) if dia.lower() in dias_semana else None

    if dia_numero is None:
        return {"error": "Día inválido"}

    cantidad = sum(1 for fecha in peliculas_df['release_date'] 
                   if datetime.strptime(fecha, "%Y-%m-%d").weekday() == dia_numero)

    return {f"Cantidad de películas estrenadas en {dia}": cantidad}


# 3. Score de una película por título
@app.get("/score_titulo/{titulo}")
def score_titulo(titulo: str):
    """
    Obtiene el score de una película por su título.

    Este endpoint busca una película en el DataFrame `peliculas_df` 
    utilizando el título proporcionado. Si la película se encuentra, 
    devuelve su título, el año de estreno y su score de popularidad. 
    Si no se encuentra la película, devuelve un mensaje de error.

    Parámetros:
    titulo (str): El título de la película a buscar.

    Retorna:
    dict: Un diccionario que contiene:
        - "Título": El título de la película.
        - "Año de estreno": El año en que se estrenó la película.
        - "Score": El score de popularidad de la película.

    Ejemplo de respuesta en caso de éxito:
    {
        "Título": "Inception",
        "Año de estreno": "2010",
        "Score": 87.5
    }

    Ejemplo de respuesta en caso de error:
    {
        "error": "Película no encontrada"
    }
    """
    pelicula = peliculas_df[peliculas_df['title'].str.lower() == titulo.lower()]
    if pelicula.empty:
        return {"error": "Película no encontrada"}
    
    return {
        "Título": pelicula['title'].values[0],
        "Año de estreno": pelicula['release_date'].values[0][:4],
        "Score": pelicula['popularity'].values[0]  # Asegúrate de que esto sea correcto
    }


# 4. Votos de una película por título
@app.get("/votos_titulo/{titulo}")
def votos_titulo(titulo: str):
    """
    Obtiene la información de votos de una película por su título.

    Este endpoint permite consultar la cantidad de votos y el promedio de votaciones 
    de una película específica, identificada por su título.

    Parámetros:
    - titulo (str): El título de la película a buscar. Se ignorará el caso.

    Respuestas:
    - Si la película se encuentra y tiene 2000 o más votos:
        - "Título": El título de la película.
        - "Año de estreno": El año de lanzamiento de la película.
        - "Cantidad de votos": El número total de votos recibidos.
        - "Promedio de votaciones": El promedio de las votaciones recibidas.

    - Si la película no se encuentra:
        - {"error": "Película no encontrada"}

    - Si la película tiene menos de 2000 valoraciones:
        - {"error": "La película no cumple con el mínimo de 2000 valoraciones."}
    """
    pelicula = peliculas_df[peliculas_df['title'].str.lower() == titulo.lower()]
    if pelicula.empty:
        return {"error": "Película no encontrada"}
    
    if pelicula['vote_count'].values[0] < 2000:
        return {"error": "La película no cumple con el mínimo de 2000 valoraciones."}
    
    return {
        "Título": pelicula['title'].values[0],
        "Año de estreno": pelicula['release_date'].values[0][:4],
        "Cantidad de votos": pelicula['vote_count'].values[0],
        "Promedio de votaciones": pelicula['vote_average'].values[0]
    }




# 5. Información sobre un actor
@app.get("/get_actor/{nombre_actor}")
def get_actor(nombre_actor: str):
    """
    Obtiene información sobre un actor específico, incluyendo la cantidad de películas en las que ha participado, 
    el retorno total de esas películas y el promedio de retorno.

    Parámetros:
    nombre_actor (str): El nombre del actor cuyo información se desea obtener.

    Retorna:
    dict: Un diccionario con la siguiente información:
        - "Actor": Nombre del actor.
        - "Cantidad de filmaciones": Número total de películas en las que el actor ha participado.
        - "Retorno total": La suma de los retornos de todas las películas del actor.
        - "Promedio de retorno": El retorno promedio de las películas del actor. 

    Si el actor no se encuentra en el reparto de ninguna película, se retorna un diccionario con un mensaje de error.

    Ejemplo de respuesta en caso de éxito:
    {
        "Actor": "Nombre del Actor",
        "Cantidad de filmaciones": 10,
        "Retorno total": 5000000,
        "Promedio de retorno": 500000
    }

    Ejemplo de respuesta en caso de error:
    {
        "error": "Actor no encontrado"
    }
    """
    # Filtrar las películas donde el actor está en el reparto
    peliculas_actor = credit_df[credit_df['reparto'].str.contains(nombre_actor, na=False)]
    
    if peliculas_actor.empty:
        return {"error": "Actor no encontrado"}

    # Unir el DataFrame de películas con el de créditos para obtener el retorno
    peliculas_info = peliculas_df[peliculas_df['id'].isin(peliculas_actor['id'])]
    
    total_retornado = peliculas_info['return'].sum()
    total_peliculas = len(peliculas_info)

    promedio_retorno = total_retornado / total_peliculas if total_peliculas > 0 else 0

    return {
        "Actor": nombre_actor,
        "Cantidad de filmaciones": total_peliculas,
        "Retorno total": total_retornado,
        "Promedio de retorno": promedio_retorno
    }

# 6. Información sobre un director
@app.get("/get_director/{nombre_director}")
def get_director(nombre_director: str):
    """
    Obtiene información sobre las películas dirigidas por un director específico.

    Parámetros:
    nombre_director (str): El nombre del director cuyas películas se desean consultar.

    Retorna:
    dict: Un diccionario con la siguiente información:
        - "Director": Nombre del director.
        - "Películas": Lista de diccionarios, cada uno conteniendo la información de una película
          (título, fecha de lanzamiento, retorno de inversión y presupuesto).
        - "Retorno total": La suma del retorno de inversión de todas las películas del director.

    Respuesta de error:
    dict: Un diccionario con un mensaje de error si el director no se encuentra en los registros
          de películas.
          - "error": Mensaje indicando que el director no fue encontrado.
    """
    # Filtrar las películas donde el director coincide
    peliculas_director = credit_df[credit_df['Director'].str.lower() == nombre_director.lower()]
    
    if peliculas_director.empty:
        return {"error": "Director no encontrado"}

    # Unir el DataFrame de películas con el de créditos para obtener la información de las películas
    peliculas_info = peliculas_df[peliculas_df['id'].isin(peliculas_director['id'])]

    retorno_total = peliculas_info['return'].sum()

    return {
        "Director": nombre_director,
        "Películas": peliculas_info[['title', 'release_date', 'return', 'budget']].to_dict(orient='records'),
        "Retorno total": retorno_total
    }
