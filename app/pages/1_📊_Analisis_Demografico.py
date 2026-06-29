import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Análisis Demográfico", page_icon="📊", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv('data/processed/streaming_users_clean.csv')

df = load_data()

st.sidebar.header("⚙️ Filtros")
plan_sel = st.sidebar.multiselect("Plan de Suscripción:", df['subscription_plan'].unique(), df['subscription_plan'].unique())
pais_sel = st.sidebar.multiselect("País:", df['country'].unique(), df['country'].unique())

df_filtrado = df[(df['subscription_plan'].isin(plan_sel)) & (df['country'].isin(pais_sel))]

st.title("📊 Análisis Demográfico y KPIs")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Usuarios", f"{df_filtrado.shape[0]:,}")
c2.metric("Edad Media", f"{df_filtrado['age'].mean():.1f} años")
c3.metric("Minutos (Promedio)", f"{df_filtrado['monthly_watch_time_mins'].mean():.0f}")
c4.metric("Tickets", f"{df_filtrado['customer_support_tickets'].mean():.1f}")

st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    st.markdown("**Usuarios por Plan**")
    fig, ax = plt.subplots(figsize=(6,4))
    sns.countplot(data=df_filtrado, x='subscription_plan', order=['Básico', 'Estándar', 'Premium'], palette='viridis', ax=ax)
    st.pyplot(fig)
with col2:
    st.markdown("**Minutos vs Plan**")
    fig2, ax2 = plt.subplots(figsize=(6,4))
    sns.boxplot(data=df_filtrado, x='subscription_plan', y='monthly_watch_time_mins', order=['Básico', 'Estándar', 'Premium'], palette='viridis', ax=ax2)
    st.pyplot(fig2)
