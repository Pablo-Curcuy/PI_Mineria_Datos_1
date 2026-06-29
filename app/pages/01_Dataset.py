import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dataset", page_icon="🗂️", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv('data/processed/streaming_users_clean.csv')

try:
    df = load_data()
    
    st.title("🗂️ Exploración del Dataset")
    st.markdown("Vista general de los datos tras el proceso de limpieza y tratamiento de nulos/outliers (Notebooks 01 y 02).")
    
    # Tarjetas de métricas
    st.subheader("Dimensiones Finales")
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Usuarios Válidos", f"{df.shape[0]:,}")
    c2.metric("Variables Analizadas", df.shape[1])
    c3.metric("Tasa de Retención", "72.0%")
    
    st.markdown("---")
    
    # Diccionario de variables desplegable
    with st.expander("📖 Ver Diccionario de Variables"):
        st.markdown("""
        * **user_id:** Identificador único del usuario.
        * **age:** Edad del usuario (filtrada entre 18 y 100 años).
        * **country:** País de residencia (Normalizado a 7 categorías).
        * **subscription_plan:** Tipo de plan (Básico, Estándar, Premium).
        * **monthly_watch_time_mins:** Minutos de visualización mensual.
        * **customer_support_tickets:** Reclamos técnicos generados.
        * **favorite_genre:** Género de contenido preferido.
        * **last_login_date:** Última conexión (Límite temporal: 2025-06-28).
        """)
    
    st.subheader("Vista de los Datos")
    st.dataframe(df.head(100), use_container_width=True)
    st.caption("Se muestran los primeros 100 registros para optimizar el rendimiento de la web.")

except Exception as e:
    st.error(f"Error al cargar los datos. Verifica que el archivo CSV exista en la ruta correcta. Detalles: {e}")
