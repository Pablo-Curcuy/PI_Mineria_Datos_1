import streamlit as st

st.set_page_config(page_title="Inicio - Analytics", page_icon="👋", layout="wide")

st.title("🎬 Plataforma de Streaming - Dashboard Analítico")
st.markdown("---")
st.markdown("""
### ¡Bienvenido al panel interactivo!
Este dashboard es el resultado del procesamiento, limpieza y análisis exploratorio de un dataset de usuarios de una plataforma de streaming. 

👈 **Usa el menú lateral izquierdo** para navegar por las diferentes secciones de la aplicación:

- **1. Análisis Demográfico:** KPIs, filtros interactivos y distribución de usuarios.
- **2. Correlaciones y PCA:** Análisis profundo de las variables numéricas.
- **3. Conclusiones:** Hallazgos clave de negocio.

*Desarrollado como proyecto final integrador de la Tecnicatura en Ciencia de Datos e Inteligencia Artificial.*
""")
