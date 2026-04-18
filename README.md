🌦️ Weather App - Multi-City & Cache System
¡Hola! Soy Cori, Contadora Pública enfocada en la gestión y automatización de datos. Este proyecto es una aplicación de clima desarrollada en Python que pone en práctica conceptos de Data Engineering, optimización de recursos y consumo de APIs.

🚀 Qué hace esta aplicación
Mi app permite consultar el clima de varias ciudades al mismo tiempo. No solo trae la temperatura, sino que utiliza una lógica de caché en memoria para que, si vuelves a preguntar por la misma ciudad, la respuesta sea instantánea sin gastar recursos de internet.

Características Principales:
Procesamiento por lotes: Puedes ingresar varias ciudades separadas por comas.

Validación de Datos: El sistema rechaza números o entradas vacías para asegurar la calidad de la información.

Optimización (Caché): Guarda temporalmente las consultas para ahorrar peticiones a la API.

Arquitectura Modular: Separación clara entre la lógica de la API (api_client.py) y la interfaz de usuario (main.py).

🛠️ Instalación y Uso
Clonar el repositorio (o descargar los archivos).

Crear y activar un entorno virtual:

### Crear y activar un entorno virtual:

```bash
python -m venv venv
.\venv\Scripts\activate

Bash
pip install requests
Ejecutar la app:

Bash
python src/main.py
🔒 Seguridad y Ética
Uso de IA: Utilicé herramientas de IA para el diseño de la arquitectura y la depuración de errores técnicos, asegurándome de comprender la lógica detrás de cada función implementada.

Privacidad: Se seleccionó la API de Open-Meteo por ser de acceso abierto, evitando así el uso de llaves privadas (API Keys) que pudieran comprometer la seguridad del código en repositorios públicos.

Responsabilidad: El código sigue principios de Clean Code y manejo de excepciones para evitar fallos inesperados.

🧪 Pruebas Realizadas
Prueba de Funcionalidad: Consulta exitosa de múltiples ciudades (ej. Zapopan, Madrid, Tokyo).

Prueba de Caché: Verificación de recuperación de datos desde memoria (identificada con el mensaje [Caché] en la terminal).

Prueba de Error: Validación de rechazo cuando el usuario ingresa datos no alfabéticos.