from api_client import get_coordinates, get_weather

def is_valid_input(text):
    """Valida que la entrada no sea solo números o esté vacía."""
    if text.isdigit():
        return False
    if not text.strip():
        return False
    return True

def run():
    print("--- Weather Monitor System (Cache Enabled) ---")
    
    while True: 
        print("\n" + "="*45)
        user_input = input("Escribe ciudades (o 'exit' para terminar): ")
        
        if user_input.lower() in ['exit', 'salir', 'quit']:
            print("Cerrando sistema... ¡Hasta luego!")
            break
        
        # Procesamos la entrada convirtiéndola en una lista limpia
        raw_cities = [c.strip() for c in user_input.split(",")]
        
        print("\nProcesando solicitudes...\n" + "-"*45)

        for city in raw_cities:
            # 1. Validación de calidad de datos
            if not is_valid_input(city):
                print(f"| {city:25} | Error: Formato inválido |") 
                continue 

            # 2. Obtención de ubicación
            lat, lon, full_name = get_coordinates(city)
            
            if lat and lon:
                # 3. Obtención de clima con soporte de caché
                temperature = get_weather(lat, lon, city) 
                
                if temperature is not None:
                    print(f"| {full_name:25} | {temperature:5}°C |")
                else:
                    print(f"| {city:25} | Error de clima |")
            else:
                print(f"| {city:25} | Ciudad no encontrada |")
        
        print("-" * 45)

if __name__ == "__main__":
    run()