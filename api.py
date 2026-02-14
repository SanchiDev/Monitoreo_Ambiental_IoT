import os
from fastapi import FastAPI, HTTPException
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv(override=True)
app = FastAPI(title="API de Monitoreo Ambiental AIoT")

db_params = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASS")
}

@app.get("/")
def inicio():
    return {"mensaje": "API de Monitoreo Activa", "sensor": "DHT22"}

@app.get("/clima/ultimo")
def obtener_ultimo_dato():
    try:
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM monitoreo_clima ORDER BY fecha_hora DESC LIMIT 1")
        dato = cur.fetchone()
        cur.close()
        conn.close()
        return dato if dato else HTTPException(status_code=404, detail="Sin datos")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/clima/historial")
def obtener_historial(limite: int = 10):
    try:
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM monitoreo_clima ORDER BY fecha_hora DESC LIMIT %s", (limite,))
        datos = cur.fetchall()
        cur.close()
        conn.close()
        return datos
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
