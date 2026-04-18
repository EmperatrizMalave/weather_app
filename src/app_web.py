import streamlit as st
from api_client import get_coordinates, get_weather

# Configuración de la página (Título en la pestaña del navegador)
st.set_page_config(page_title="Weather Data Monitor", page_icon="🌤️", layout="centered")

# --- Estilos y Título ---
st.title("🌦️ Weather Monitor System")
st.markdown("""
Esta herramienta orquesta una consulta doble a APIs climáticas para **normalizar 
ubicaciones** y extraer **datos meteorológicos en tiempo real**.
""")

# --- Interfaz de Usuario en la Barra Lateral ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/4052/4052984.png", width=100)
st.sidebar.header("Configuración de Consulta")
cities_input = st.sidebar.text_input(
    "Ciudades (separadas por comas):", 
    placeholder="Ej: Guadalajara, Madrid, Tokyo"
)

search_button = st.sidebar.button("🚀 Obtener Clima")

# --- Lógica de Procesamiento ---
if search_button:
    if not cities_input.strip():
        st.sidebar.warning("⚠️ Por favor, ingresa al menos una ciudad.")
    else:
        raw_cities = [c.strip() for c in cities_input.split(",")]
        
        st.subheader("📊 Resultados del Pipeline de Datos")
        
        # Lista para almacenar resultados formateados
        weather_results = []
        
        # Contenedor para la barra de progreso
        progress_text = "Procesando ciudades..."
        progress_bar = st.progress(0, text=progress_text)
        
        for i, city in enumerate(raw_cities):
            # 1. Validación de entrada (evitar solo números)
            if city.isdigit():
                st.error(f"❌ '{city}' no parece ser un nombre de ciudad válido.")
                continue
                
            # 2. Obtener Coordenadas (Usando lógica modular con caché)
            lat, lon, full_name = get_coordinates(city)
            
            if lat and lon:
                # 3. Obtener Clima
                temp = get_weather(lat, lon, city)
                
                if temp is not None:
                    weather_results.append({
                        "Ubicación": full_name,
                        "Temperatura": f"{temp} °C",
                        "Estado": "✅ Datos Listos"
                    })
                else:
                    weather_results.append({
                        "Ubicación": city,
                        "Temperatura": "N/A",
                        "Estado": "⚠️ Error de Conexión"
                    })
            else:
                weather_results.append({
                    "Ubicación": city,
                    "Temperatura": "N/A",
                    "Estado": "🔍 No Encontrada"
                })
            
            # Actualizar barra de progreso visualmente
            progress_bar.progress((i + 1) / len(raw_cities), text=f"Procesando {city}...")

        # --- Visualización de Datos Final ---
        if weather_results:
            # Mostramos una tabla estilizada
            st.table(weather_results)
            st.success("¡Pipeline de datos ejecutado con éxito!")
            
            # Mostrar un indicador clave (Metric) de la primera ciudad consultada
            col1, col2 = st.columns(2)
            with col1:
                if "°C" in weather_results[0]["Temperatura"]:
                    st.metric(
                        label=f"Ciudad Principal: {weather_results[0]['Ubicación']}", 
                        value=weather_results[0]["Temperatura"]
                    )
            with col2:
                st.info("💡 Sugerencia: Reintenta la búsqueda para probar la velocidad de la Caché.")

# --- Pie de página informativo ---
st.divider()
st.caption("© 2024 Weather App | Desarrollado con Python & Streamlit | Enfoque en Data Engineering")