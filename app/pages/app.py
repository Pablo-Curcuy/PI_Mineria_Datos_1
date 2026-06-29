import streamlit as st
import pandas as pd

# 1. Configuración de la página (debe ser el primer comando de Streamlit)
st.set_page_config(
    page_title="Dashboard - Plataforma de Streaming",
    page_icon="🎬",
    layout="wide"
)

# 2. Título principal
st.title("🎬 Análisis de Usuarios de Plataforma de Streaming")
st.markdown("---")

# 3. Función para cargar los datos con caché (mejora el rendimiento)
@st.cache_data
def load_data():
    # IMPORTANTE: Streamlit lee desde la raíz del repositorio, 
    # por lo que la ruta hacia los datos debe ser correcta.
    # Asumiendo que tu dataset está en data/processed/
    df = pd.read_csv('data/processed/streaming_users_clean.csv')
    return df

# 4. Cargar los datos y mostrar un mensaje de éxito
try:
    df = load_data()
    st.success(f"Datos cargados exitosamente: {df.shape[0]} usuarios y {df.shape[1]} variables.")
    
    # 5. Mostrar una vista previa de los datos
    st.subheader("Vista previa del dataset limpio")
    st.dataframe(df.head())
    
except Exception as e:
    st.error(f"Error al cargar los datos: {e}")
