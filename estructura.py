import streamlit as st
import pandas as pd

# ==============================================================================
# CONFIGURACIÓN GENERAL DE LA PÁGINA
# ==============================================================================
st.set_page_config(
    page_title="Motor EV - Maqueta UI", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# ==============================================================================
# SIDEBAR (PANEL LATERAL)
# ==============================================================================
st.sidebar.title("⚙️ Panel de Control")

# 1. Navegación Principal
menu = st.sidebar.radio(
    "Navegación:",
    [
        "En Vivo (Partidos)", 
        "Parlays (SGP)", 
        "Inicio (Top EV)", 
        "Historial", 
        "Bankroll", 
        "Telemetría (Logs)"
    ]
)

st.sidebar.markdown("---")

# 2. Resumen Financiero Rápido
st.sidebar.subheader("💰 Finanzas")
st.sidebar.metric(
    label="Capital Neto Disponible", 
    value="$15,450.00 MXN", 
    delta="+ $450.00 Hoy"
)

st.sidebar.markdown("---")

# 3. Panel Operativo (Business Intelligence)
st.sidebar.subheader("🛠️ Estado del Sistema")

# Barra de progreso simulando el consumo de The Odds API
creditos_usados = 100
creditos_totales = 500
porcentaje_api = int((creditos_usados / creditos_totales) * 100)
st.sidebar.progress(porcentaje_api, text=f"API Odds ({creditos_usados}/{creditos_totales})")

# Indicadores de salud del VPS y Base de datos
st.sidebar.info("VPS Hostinger: Activo 🟢")
st.sidebar.success("MySQL Sync: Hace 2 horas 🔄")

# ==============================================================================
# CONTENIDO DE LAS SECCIONES (SIMULACIÓN)
# ==============================================================================

if menu == "En Vivo (Partidos)":
    st.title("📊 Partidos de hoy")
    st.write("Seleccione un encuentro para analizar las proyecciones algorítmicas con modelo híbrido (60% Poisson / 40% Casino).")
    st.markdown("---")
    
    # Simulación del selector
    st.selectbox(
        "Seleccione un partido:", 
        ["Washington Nationals (L) vs Atlanta Braves (V) | ⭐ Relevante | 🕒 18:30"]
    )
    st.markdown("---")
    
    # Simulación visual de los bloques
    col1, col2 = st.columns(2)
    with col1:
        st.info("🔵 Contenedor: Estadísticas H2H y Totales del Equipo Local")
    with col2:
        st.error("🔴 Contenedor: Estadísticas H2H y Totales del Equipo Visitante")
        
    st.header("🎯 Radar de Jugadores")
    st.success("Aquí se desplegarán los acordeones (expanders) con las proyecciones de Hits, Bases Totales y Home Runs de los bateadores.")

elif menu == "Parlays (SGP)":
    st.title("🔥 Parlays de hoy")
    st.write("Combinaciones algorítmicas con Valor Esperado (EV) Positivo.")
    st.markdown("---")
    
    st.subheader("I TOP 8 PARLAY HITS JUGADORES")
    with st.expander("Parlay 1 (Hits - Agresivo) | Cuota: 4.50 | Prob: 35.2%", expanded=False):
        st.write("Simulación de 4 picks globales de Hits cruzados de distintos partidos.")
        
    st.subheader("I TOP 8 PARLAY BASES JUGADORES")
    with st.expander("Parlay 2 (Bases - Conservador) | Cuota: 3.10 | Prob: 42.1%", expanded=False):
        st.write("Simulación de 4 picks globales de Bases Totales.")

    st.subheader("I PARLAY POR PARTIDO (SGP)")
    st.selectbox("Filtrar por partido:", ["Miami Marlins (L) vs Philadelphia Phillies (V)"])
    st.info("Aquí aparecerá el parlay con el bono de correlación (+15% Prob) por pertenecer al mismo encuentro.")

elif menu == "Inicio (Top EV)":
    st.title("🏠 Radar General (Top Oportunidades)")
    st.write("Las mejores oportunidades de todo el mercado ordenadas de mayor a menor probabilidad.")
    st.markdown("---")
    
    # Simulación de lista Top EV
    for i in range(1, 4):
        st.success(f"**Pick #{i}:** Jugador X (Equipo Y) | Mercado > Línea | 🔥 Prob: 75% | ✅ EV+ 12%")

elif menu == "Historial":
    st.title("📖 Libro Mayor y Liquidación")
    st.write("Auditoría de apuestas pasadas y liquidación de boletos abiertos.")
    st.markdown("---")
    
    st.info("📊 Dataframe interactivo mostrando los últimos boletos jugados.")
    
    st.subheader("⚖️ Panel de Liquidación")
    st.write("Seleccione un boleto pendiente para marcarlo como:")
    c1, c2, c3 = st.columns(3)
    c1.button("✅ Ganada")
    c2.button("❌ Perdida")
    c3.button("🔄 Push / Anulada")

elif menu == "Bankroll":
    st.title("💰 Tesorería y Flujo de Capital")
    st.write("Gestión de ingresos, retiros y ajustes de auditoría del Bankroll.")
    st.markdown("---")
    
    st.metric(label="Capital Neto Disponible", value="$15,450.00 MXN")
    
    with st.expander("⚙️ Ajuste Manual de Capital (Correcciones)"):
        st.number_input("Establecer saldo exacto (MXN):", value=15450.00)
        st.button("Aplicar Ajuste")
        
    st.info("📊 Dataframe mostrando el registro contable de cada peso apostado o ganado.")

elif menu == "Telemetría (Logs)":
    st.title("🖥️ Telemetría y Bitácora del Servidor")
    st.write("Auditoría en tiempo real de las ejecuciones autónomas del VPS Linux (Cronjob a las 6:00 AM).")
    st.markdown("---")
    
    # Simulación de tabla de logs
    data = {
        "Fecha/Hora": ["06:00:05", "06:01:22", "06:03:10"],
        "Fase": ["Arranque", "Extracción MLB", "Análisis EV"],
        "Mensaje": ["Iniciando Motor Maestro", "BD MLB actualizada con 1039 juegos", "Se inyectaron 416 registros EV+ a MySQL"]
    }
    df_logs = pd.DataFrame(data)
    st.dataframe(df_logs, use_container_width=True)
