import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="PCA", page_icon="📈", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv('data/processed/streaming_users_clean.csv')

df = load_data()

st.title("📈 Análisis Multivariado y PCA")
st.markdown("Exploración de la relación matemática entre las variables numéricas del modelo.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Matriz de Correlación")
    fig, ax = plt.subplots(figsize=(6,5))
    vars_num = ['age', 'monthly_watch_time_mins', 'customer_support_tickets']
    corr = df[vars_num].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".3f", vmin=-1, vmax=1, ax=ax, square=True)
    st.pyplot(fig)

with col2:
    st.subheader("Interpretación de Componentes")
    st.info("""
    **Hallazgo clave (Notebook 04):**
    
    La matriz confirma que la correlación lineal entre las tres variables es cercana a cero. 
    
    Al aplicar el PCA, descubrimos que la varianza está distribuida de forma relativamente equitativa entre las componentes principales. Esto significa que **cada variable aporta información independiente**.
    
    *Ejemplo de negocio:* La edad de un usuario no es un factor que determine cuánto tiempo consume la plataforma, ni cuántos tickets de soporte generará.
    """)
