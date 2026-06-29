import streamlit as st

st.set_page_config(page_title="Inicio - Proyecto Streaming", page_icon="🎬", layout="wide")

# Diseño de cabecera con columnas
col1, col2 = st.columns([3, 1])
with col1:
    st.title("🎬 Análisis de Usuarios: Plataforma de Streaming")
    st.markdown("### Proyecto Integrador Final")
with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/403/403800.png", width=120)

st.markdown("---")

# Tarjeta de bienvenida
st.info("""
**¡Bienvenido/a al Dashboard Interactivo!** 🚀  
Esta aplicación web presenta los resultados del procesamiento, análisis exploratorio (EDA) y reducción de dimensionalidad (PCA) aplicados a un dataset de usuarios de una plataforma de streaming.
""")

st.markdown("""
### 🧭 ¿Qué encontrarás aquí?
Utiliza el menú lateral izquierdo para navegar por las distintas fases del proyecto:
- **01. Dataset:** Exploración de los datos limpios, diccionario de variables y métricas generales.
- **02. EDA:** Análisis Demográfico interactivo con filtros, KPIs y visualizaciones.
- **03. PCA:** Análisis de correlaciones y Componentes Principales de las variables numéricas.
- **04. Conclusiones:** Hallazgos clave de negocio y recomendaciones.
""")

st.markdown("---")

# Sección de Integrantes y Enlaces
st.subheader("👨‍💻 Equipo de Trabajo")
col_eq1, col_eq2, col_eq3 = st.columns(3)

with col_eq1:
    st.markdown("""
    **Pablo Curcuy** *Tecnicatura en Ciencia de Datos e IA* [🔗 LinkedIn](#) | [🐙 GitHub](https://github.com/Pablo-Curcuy)
    """)
with col_eq2:
    st.markdown("""
    **[Nombre de tu Compañero]** *Tecnicatura en Ciencia de Datos e IA* [🔗 LinkedIn](#) | [🐙 GitHub](#)
    """)
with col_eq3:
    st.markdown("""
    **Repositorio del Proyecto** [📁 Ver código fuente y Notebooks en GitHub](https://github.com/Pablo-Curcuy/PI_Mineria_Datos_1)
    """)
