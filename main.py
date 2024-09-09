
from fastapi import FastAPI
import pandas as pd
from datetime import datetime


app = FastAPI()

# Carga de bases de datos

# Cargar los DataFrame
peliculas_df = pd.read_csv('movies_df.csv')
credit_df = pd.read_csv('credit_df.csv')


# Funciones para los endpoint

# Función para convertir nombres de meses en español a números de mes
def mes_a_numero(mes: str) -> int:
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
