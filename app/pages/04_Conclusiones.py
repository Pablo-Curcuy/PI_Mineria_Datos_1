import streamlit as st

st.set_page_config(page_title="Conclusiones", page_icon="📌", layout="wide")

st.title("📌 Conclusiones y Recomendaciones de Negocio")
st.markdown("Síntesis de los hallazgos obtenidos tras el ciclo completo de Minería de Datos.")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.success("""
    ### 💎 1. El valor del Plan Premium
    El plan de suscripción es la variable que mejor explica el comportamiento en la plataforma. Los usuarios Premium no solo representan mayor rentabilidad, sino que consumen consistentemente más minutos, demostrando un nivel de "engagement" muy superior.
    """)
    
    st.warning("""
    ### 🛠️ 2. Fricción en el Plan Básico
    El plan Básico concentra la mayor cantidad de usuarios, pero lidera la generación de tickets de soporte técnico. Existe una clara oportunidad operativa para mejorar la experiencia de uso en este segmento, lo que reduciría los costos de atención al cliente.
    """)

with col2:
    st.info("""
    ### 🌍 3. Audiencia Universal
    El análisis multivariado (PCA) demostró que el nivel de consumo es independiente de la edad. Esto permite a los equipos de Marketing diseñar estrategias intergeneracionales basadas en preferencias de contenido, en lugar de segmentar artificialmente por grupos etarios.
    """)
    
    st.markdown("""
    ### 🚀 Próximos Pasos (Futuro)
    * Incorporar modelos predictivos (Machine Learning) para detectar probabilidad de **Churn** (abandono).
    * Sumar variables de dispositivos para enriquecer el Análisis de Componentes Principales.
    * Analizar series temporales de inicios de sesión.
    """)
