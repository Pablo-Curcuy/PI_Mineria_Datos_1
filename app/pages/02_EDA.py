import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="EDA", page_icon="📊", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv('data/processed/streaming_users_clean.csv')

df = load_data()

# Filtros en la barra lateral
st.sidebar.header("⚙️ Parámetros de Filtrado")
plan_sel = st.sidebar.multiselect("Selecciona el Plan:", df['subscription_plan'].unique(), default=df['subscription_plan'].unique())
pais_sel = st.sidebar.multiselect("Selecciona el País:", df['country'].unique(), default=df['country'].unique())

# Aplicar filtros
df_filtrado = df[(df['subscription_plan'].isin(plan_sel)) & (df['country'].isin(pais_sel))]

st.title("📊 Análisis Exploratorio de Datos (EDA)")
st.markdown("Análisis demográfico y de comportamiento basado en los filtros seleccionados.")

# KPIs interactivos con diseño de columnas
col1, col2, col3, col4 = st.columns(4)
col1.metric("Usuarios en segmento", f"{df_filtrado.shape[0]:,}")
col2.metric("Edad Promedio", f"{df_filtrado['age'].mean():.1f} años")
col3.metric("Tiempo Promedio (min)", f"{df_filtrado['monthly_watch_time_mins'].mean():.0f}")
col4.metric("Tickets Promedio", f"{df_filtrado['customer_support_tickets'].mean():.2f}")

st.markdown("---")

# Gráficos
st.subheader("Visualizaciones Principales")
col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    st.markdown("#### 👥 Distribución por Plan de Suscripción")
    fig, ax = plt.subplots(figsize=(6,4))
    sns.countplot(data=df_filtrado, x='subscription_plan', order=['Básico', 'Estándar', 'Premium'], palette='magma', ax=ax)
    ax.set_ylabel("Cantidad de Usuarios")
    ax.set_xlabel("")
    st.pyplot(fig)

with col_graf2:
    st.markdown("#### ⏱️ Tiempo de Visualización según Plan")
    fig2, ax2 = plt.subplots(figsize=(6,4))
    sns.boxplot(data=df_filtrado, x='subscription_plan', y='monthly_watch_time_mins', order=['Básico', 'Estándar', 'Premium'], palette='magma', ax=ax2)
    ax2.set_ylabel("Minutos Mensuales")
    ax2.set_xlabel("")
    st.pyplot(fig2)
