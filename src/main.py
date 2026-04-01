# 1. Traemos las funciones que escribimos en el otro archivo para poder usarlas aquí.
from api_client import get_coordinates, get_weather 

def run(): # 2. Definimos la función principal que arranca todo.
    print("--- Bienvenido a tu App del Clima ---") # 3. Un saludo bonito en consola.
    
    # 4. Le pedimos al usuario que escriba algo y lo guardamos en la variable 'city'.
    city = input("Escribe el nombre de una ciudad: ") 
    
    # 5. LLAMADA 1: Le pasamos el nombre a la función de coordenadas.
    # Recibimos tres valores: latitud, longitud y el nombre oficial.
    lat, lon, full_name = get_coordinates(city) 
    
    if lat and lon: # 6. ¿Obtuvimos coordenadas válidas? (Si no es None).
        
        # 7. LLAMADA 2: Si tenemos coordenadas, pedimos la temperatura.
        temp = get_weather(lat, lon) 
        
        if temp is not None: # 8. ¿La temperatura llegó correctamente?
            # 9. Mostramos el resultado final usando el nombre oficial y el número.
            print(f"\nEl clima en {full_name} es de {temp}°C.") 
        else:
            print("No se pudo obtener el clima.")
    else:
        # 10. Si la primera función no encontró la ciudad, avisamos al usuario.
        print("Ciudad no encontrada. Intenta de nuevo.")

# 11. Esta línea es un estándar en Python. 
# Dice: "Si este archivo se ejecuta directamente, corre la función run()".
if __name__ == "__main__":
    run()