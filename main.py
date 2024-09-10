
from fastapi import FastAPI
import pandas as pd
from datetime import datetime


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
    mes_numero = mes_a_numero(mes)
    if mes_numero == 0:
        return {"error": "Mes inválido"}

    cantidad = sum(1 for fecha in peliculas_df['release_date'] 
                   if datetime.strptime(fecha, "%Y-%m-%d").month == mes_numero)
    
    return {f"Cantidad de películas estrenadas en {mes}": cantidad}

# 2. Cantidad de filmaciones por día
@app.get("/cantidad_filmaciones_dia/{dia}")
def cantidad_filmaciones_dia(dia: str):
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
