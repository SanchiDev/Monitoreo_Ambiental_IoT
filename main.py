import serial
import os
import psycopg2
import time
from dotenv import load_dotenv

load_dotenv(override=True)

# Configuración directa
db_params = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASS")
}
puerto_esp32 = 'COM5'
baudios = 115200

def guardar_datos(t, h):
    try:
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()
        cur.execute("INSERT INTO monitoreo_clima (temperatura, humedad) VALUES (%s, %s)", (t, h))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error de DB: {e}")

def verificar_alertas(t, h):
    T_MIN, T_MAX = 18.0, 24.0
    H_MIN, H_MAX = 40.0, 60.0
    alertas = []
    if t > T_MAX: alertas.append(f"⚠️ ¡CALOR! ({t}°C)")
    elif t < T_MIN: alertas.append(f"⚠️ ¡FRÍO! ({t}°C)")
    if h > H_MAX: alertas.append(f"💧 ¡HUMEDAD ALTA! ({h}%)")
    elif h < H_MIN: alertas.append(f"🌵 ¡AMBIENTE SECO! ({h}%)")
    if alertas: print(" >>> " + " | ".join(alertas))
    else: print("✅ Ambiente óptimo")

try:
    ser = serial.Serial(puerto_esp32, baudios, timeout=1)
    print("Conectado al ESP32. Sistema de Alertas Activo...")
    while True:
        linea = ser.readline().decode('utf-8').strip()
        if linea and "," in linea:
            try:
                temp, hum = map(float, linea.split(','))
                print(f"Dato recibido -> T: {temp}ºC, H: {hum}%")
                guardar_datos(temp, hum)
                verificar_alertas(temp, hum)
            except ValueError: pass
except KeyboardInterrupt:
    print("\nMonitoreo detenido.")
    if 'ser' in locals(): ser.close()
