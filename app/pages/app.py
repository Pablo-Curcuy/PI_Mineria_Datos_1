import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. CONFIGURACIÓN DE LA PÁGINA (¡Siempre va primero!)
# ==========================================
st.set_page_config(
    page_title="Dashboard - Plataforma de Streaming",
    page_icon="🎬",
    layout="wide"
)

# ==========================================
# 2. CARGA DE DATOS
# ==========================================
# Usamos caché para que no lea el CSV cada vez que tocas un filtro
@st.cache_data
def load_data():
    df = pd.read_csv('data/processed/streaming_users_clean.csv')
    return df

df = load_data()

# ==========================================
# 3. BARRA LATERAL (Menú interactivo)
# ==========================================
st.sidebar.title("⚙️ Filtros de Análisis")
st.sidebar.markdown("Usa estos controles para explorar los datos.")

# Filtro interactivo por Plan de Suscripción
planes_disponibles = df['subscription_plan'].unique().tolist()
plan_seleccionado = st.sidebar.multiselect(
    "Selecciona el Plan:",
    options=planes_disponibles,
    default=planes_disponibles
)

# Filtro interactivo por País
paises_disponibles = df['country'].unique().tolist()
pais_seleccionado = st.sidebar.multiselect(
    "Selecciona el País:",
    options=paises_disponibles,
    default=paises_disponibles
)

# El motor del dashboard: Filtra el dataset según lo que el usuario elige en el menú
df_filtrado = df[
    (df['subscription_plan'].isin(plan_seleccionado)) &
    (df['country'].isin(pais_seleccionado))
]

# ==========================================
# 4. ÁREA PRINCIPAL DEL DASHBOARD
# ==========================================
st.title("🎬 Dashboard Interactivo: Comportamiento de Usuarios")
st.markdown("Explora las métricas principales según los filtros aplicados en el menú lateral.")

# 4.1 KPIs (Indicadores Clave)
st.subheader("Métricas Principales")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Usuarios Totales", f"{df_filtrado.shape[0]:,}")
with col2:
    st.metric("Edad Promedio", f"{df_filtrado['age'].mean():.1f} años")
with col3:
    st.metric("Tiempo Promedio (min)", f"{df_filtrado['monthly_watch_time_mins'].mean():.0f}")
with col4:
    st.metric("Tickets Promedio", f"{df_filtrado['customer_support_tickets'].mean():.1f}")

st.markdown("---")

# 4.2 Gráficos Dinámicos (Usando matplotlib y seaborn)
st.subheader("Análisis Visual")
col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    st.markdown("**Distribución de Usuarios por Plan**")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(
        data=df_filtrado, 
        x='subscription_plan', 
        order=['Básico', 'Estándar', 'Premium'], 
        palette='viridis', 
        ax=ax
    )
    ax.set_ylabel("Cantidad")
    ax.set_xlabel("Plan")
    st.pyplot(fig)

with col_graf2:
    st.markdown("**Tiempo de Visualización por Plan**")
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    sns.boxplot(
        data=df_filtrado, 
        x='subscription_plan', 
        y='monthly_watch_time_mins', 
        order=['Básico', 'Estándar', 'Premium'], 
        palette='viridis', 
        ax=ax2
    )
    ax2.set_ylabel("Minutos Mensuales")
    ax2.set_xlabel("Plan")
    st.pyplot(fig2)

# 4.3 Tabla de datos (Ocultable para no ensuciar la pantalla)
st.markdown("---")
with st.expander("🔍 Ver tabla de datos detallada"):
    st.dataframe(df_filtrado.head(100)) # Mostramos solo 100 para mantener la web fluida
