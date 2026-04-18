import requests
from urllib.parse import quote

# --- Almacén de caché con nombre profesional ---
weather_cache = {}

def get_coordinates(city_name):
    """Busca coordenadas y usa caché si ya existen."""
    # Normalizamos la clave de búsqueda
    cache_key = city_name.lower()

    # Revisamos si ya buscamos esta ciudad antes
    if cache_key in weather_cache:
        print(f"  [Caché] Recuperando coordenadas de {city_name}...")
        data = weather_cache[cache_key]
        return data["lat"], data["lon"], data["full_name"]

    # Si no está en caché, preparamos la URL segura
    safe_city_name = quote(city_name.strip())
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={safe_city_name}&count=1&language=es&format=json"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        if "results" in data and len(data["results"]) > 0:
            result = data["results"][0]
            lat, lon, full_name = result["latitude"], result["longitude"], result["name"]
            
            # Guardamos en la caché global
            weather_cache[cache_key] = {
                "lat": lat, 
                "lon": lon, 
                "full_name": full_name,
                "temp": None 
            }
            return lat, lon, full_name
    except Exception as e:
        print(f"Error técnico: {e}")
    return None, None, None

def get_weather(lat, lon, city_name): 
    """Obtiene clima y actualiza la caché."""
    cache_key = city_name.lower()
    
    # ¿Ya tenemos la temperatura en nuestra caché?
    if cache_key in weather_cache and weather_cache[cache_key]["temp"] is not None:
        print(f"  [Caché] Recuperando temperatura de {city_name}...")
        return weather_cache[cache_key]["temp"]

    # Si no, consultamos la API de pronóstico
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    
    try:
        response = requests.get(url)
        weather_data = response.json()
        
        if "current_weather" in weather_data:
            temp = weather_data["current_weather"]["temperature"]
            # Actualizamos el registro existente en caché
            if cache_key in weather_cache:
                weather_cache[cache_key]["temp"] = temp
            return temp
    except Exception as e:
        print(f"Error al obtener clima: {e}")
        
    return None