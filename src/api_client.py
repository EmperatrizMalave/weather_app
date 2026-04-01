import requests # 1. Importamos la librería que nos permite "hablar" con URLs de internet.

def get_coordinates(city_name): # 2. Definimos una función que recibe el nombre de la ciudad.
    """Convierte el nombre de una ciudad en latitud y longitud."""
    
    # 3. Creamos la URL mágica. Usamos una "f-string" para meter el nombre de la ciudad dentro del link.
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=es&format=json"
    
    response = requests.get(url) # 4. Enviamos la petición a la API. 'response' guarda lo que la API nos contesta.
    data = response.json() # 5. Transformamos la respuesta (que es puro texto) en un diccionario de Python.

    if "results" in data: # 6. Verificamos: ¿La API encontró resultados para esa ciudad?
        result = data["results"][0] # 7. Si sí, tomamos el primer resultado (el índice 0).
        # 8. Devolvemos tres cosas: latitud, longitud y el nombre completo (ej: "Jalisco, México").
        return result["latitude"], result["longitude"], result["name"]
        
    return None, None, None # 9. Si no encontró nada, devolvemos "vacío" para no romper el programa.

def get_weather(lat, lon): # 10. Esta función recibe las coordenadas que obtuvimos arriba.
    """Obtiene la temperatura actual usando coordenadas."""
    
    # 11. Nueva URL para el clima, inyectando la latitud y longitud.
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    
    response = requests.get(url) # 12. Otra petición a internet.
    data = response.json() # 13. Convertimos a diccionario otra vez.
    
    if "current_weather" in data: # 14. ¿La respuesta tiene la sección de clima actual?
        return data["current_weather"]["temperature"] # 15. Devolvemos solo el número de la temperatura.
        
    return None # 16. Si algo falló, devolvemos None.