import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Correlaciones y PCA", page_icon="📈", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv('data/processed/streaming_users_clean.csv')

df = load_data()

st.title("📈 Análisis de Variables Numéricas")
st.markdown("Exploración de la relación matemática entre edad, tiempo de visualización y tickets de soporte.")

col1, col2 = st.columns([1.2, 1])
with col1:
    fig, ax = plt.subplots(figsize=(5,4))
    corr = df[['age', 'monthly_watch_time_mins', 'customer_support_tickets']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".3f", vmin=-1, vmax=1, ax=ax)
    st.pyplot(fig)

with col2:
    st.info("""
    **💡 Hallazgo Analítico (Basado en PCA):**\n
    La matriz confirma que la correlación entre variables es cercana a cero. 
    Como demostramos en la Notebook 04 de Análisis de Componentes Principales, cada variable numérica es independiente. \n
    *Implicación:* No se puede predecir el comportamiento de consumo (minutos) basándose únicamente en la edad del usuario.
    """)

st.markdown("---")
with st.expander("🔍 Explorar Base de Datos Limpia"):
    st.dataframe(df)
