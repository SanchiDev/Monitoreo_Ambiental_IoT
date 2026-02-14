# 🌍 Monitoreo Ambiental IoT (ESP32 + Python + PostgreSQL)

[![Demostración del Proyecto](https://img.youtube.com)](https://www.youtube.com/watch?v=CHUrBSHAXWI)
*Haz clic para ver la demostración del sistema en tiempo real en YouTube.*

Sistema de monitoreo de temperatura y humedad en tiempo real con arquitectura desacoplada, alertas inteligentes de confort ambiental y una API REST para consulta de datos históricos.

## 🚀 Arquitectura del Proyecto

El sistema utiliza un enfoque de **Separación de Responsabilidades (SoC)** para garantizar escalabilidad:

* **Hardware (ESP32 + DHT22):** Captura de datos físicos y transmisión vía Serial (UART).
* **Ingestión y Lógica (Python - main.py):** Script encargado de escuchar el puerto serial, procesar los datos, emitir alertas en consola e insertar los registros en la base de datos.
* **Capa de Datos (PostgreSQL):** Almacenamiento persistente de lecturas.
* **Servicio de API (FastAPI - api.py):** Expone los datos en formato JSON para posibles integraciones con dashboards o aplicaciones móviles.

## 🛠️ Tecnologías Utilizadas

* **Microcontrolador:** ESP32 (C++/Arduino).
* **Backend:** Python 3.13+ ([FastAPI](https://fastapi.tiangolo.com)).
* **Base de Datos:** PostgreSQL.
* **Protocolo de Comunicación:** Serial (UART).
* **Librerías Clave:** `pyserial`, `psycopg2-binary`, `python-dotenv`, `uvicorn`.

## 🔌 Diagrama de Conexión (Hardware)

| Componente | Pin ESP32 |
| :--- | :--- |
| VCC (DHT22) | 3.3V |
| GND (DHT22) | GND |
| DATA (DHT22) | GPIO 27 |

## 🗄️ Configuración de la Base de Datos

```sql
CREATE TABLE monitoreo_clima (
    id SERIAL PRIMARY KEY,
    temperatura FLOAT NOT NULL,
    humedad FLOAT NOT NULL,
    fecha_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```



# Clonar el repositorio
git clone https://github.com
cd Monitoreo_Ambiental_IoT

# Crear y activar entorno virtual
python -m venv venv
# En Windows: .\venv\Scripts\activate
# En Linux/Mac: source venv/bin/activate 

# Instalar dependencias
pip install -r requirements.txt




