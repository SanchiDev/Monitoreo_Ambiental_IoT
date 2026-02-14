# 🌍 Monitoreo Ambiental AIoT (ESP32 + Python + PostgreSQL)

[![Demostración del Proyecto](https://img.youtube.com)](https://www.youtube.com/watch?v=CHUrBSHAXWI)
*Haz clic para ver la demostración del sistema en tiempo real en YouTube.*


Sistema de monitoreo de temperatura y humedad en tiempo real con arquitectura desacoplada, alertas inteligentes de confort ambiental y una API REST para consulta de datos históricos.



\## 🚀 Arquitectura del Proyecto

El sistema utiliza un enfoque de \*\*Separación de Responsabilidades (SoC)\*\* para garantizar escalabilidad:



\*   \*\*Hardware (ESP32 + DHT22):\*\* Captura de datos físicos y transmisión vía Serial (UART).

\*   \*\*Ingestión y Lógica (Python - `main.py`):\*\* Script encargado de escuchar el puerto serial, procesar los datos, emitir alertas en consola e insertar los registros en la base de datos.

\*   \*\*Capa de Datos (PostgreSQL):\*\* Almacenamiento persistente de lecturas.

\*   \*\*Servicio de API (FastAPI - `api.py`):\*\* Expone los datos en formato JSON para posibles integraciones con dashboards o aplicaciones móviles.



\## 🛠️ Tecnologías Utilizadas



\*   \*\*Microcontrolador:\*\* ESP32 (C++/Arduino).

\*   \*\*Backend:\*\* Python 3.13+ (\[FastAPI](https://fastapi.tiangolo.com)).

\*   \*\*Base de Datos:\*\* PostgreSQL.

\*   \*\*Protocolo de Comunicación:\*\* Serial (UART).

\*   \*\*Librerías Clave:\*\* `pyserial`, `psycopg2-binary`, `python-dotenv`, `uvicorn`.



\## 🔌 Diagrama de Conexión (Hardware)



| Componente | Pin ESP32 |

| :--- | :--- |

| VCC (DHT22) | 3.3V |

| GND (DHT22) | GND |

| DATA (DHT22) | GPIO 27 |



\## 🗄️ Configuración de la Base de Datos

Ejecuta el siguiente script en tu instancia de \[PostgreSQL](https://www.postgresql.org) para preparar la tabla:



```sql

CREATE TABLE monitoreo\_clima (

&nbsp;   id SERIAL PRIMARY KEY,

&nbsp;   temperatura FLOAT NOT NULL,

&nbsp;   humedad FLOAT NOT NULL,

&nbsp;   fecha\_hora TIMESTAMP DEFAULT CURRENT\_TIMESTAMP

);

```



\## 📋 Requisitos Previos



\*   \*\*PostgreSQL:\*\* Instancia activa con una base de datos llamada `monitoreo\\\_esp32`.

\*   \*\*Arduino IDE:\*\* Librerías `DHT sensor library` y `Adafruit Unified Sensor` instaladas.



\## 🔧 Instalación y Configuración



\### 1. Preparar el Entorno Python

```bash



\# Clonar el repositorio



git clone https://github.com



cd proyecto-esp32-aiot







\# Crear y activar entorno virtual



python -m venv venv



\# En Windows: .\\\\venv\\\\Scripts\\\\activate



source venv/bin/activate 







\# Instalar dependencias



pip install -r requirements.txt



