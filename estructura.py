import streamlit as st
import pandas as pd

# ==============================================================================
# CONFIGURACIÓN GENERAL
# ==============================================================================
st.set_page_config(page_title="Motor EV - Maqueta Móvil", layout="wide", initial_sidebar_state="expanded")

# ==============================================================================
# SIDEBAR: FINANZAS, METAS Y TELEMETRÍA
# ==============================================================================
st.sidebar.title("⚙️ Panel Operativo")
menu = st.sidebar.radio("Navegación:", [
            "En Vivo (Partidos)", 
            "Parlays (SGP)", 
            "Inicio (Top EV)", 
            "Historial", 
            "Bankroll", 
            "Telemetría (Logs)"
])
st.sidebar.markdown("---")

# 1. Gestión Multicartera
st.sidebar.subheader("💼 Carteras de Inversión")
c_playdoit = st.sidebar.number_input("Playdoit (MXN)", value=5000.00, step=100.0)
c_winpot = st.sidebar.number_input("Winpot (MXN)", value=4250.00, step=100.0)
c_caliente = st.sidebar.number_input("Caliente (MXN)", value=6200.00, step=100.0)
c_otro = st.sidebar.number_input("Otro (MXN)", value=0.00, step=100.0)

capital_neto = c_playdoit + c_winpot + c_caliente + c_otro
st.sidebar.metric("Capital Neto Total", f"${capital_neto:,.2f} MXN")
st.sidebar.markdown("---")

# 2. Cascada de Metas Operativas
st.sidebar.subheader("📈 Meta Mensual y Costos Fijos")
ganancia_mensual = 1500.0  # Simulado visualmente
costo_vps, costo_api, gastos_extra, meta_utilidad = 300, 600, 400, 5000
total_meta = costo_vps + costo_api + gastos_extra + meta_utilidad

progreso = min(ganancia_mensual / total_meta, 1.0)
st.sidebar.progress(progreso, text=f"Progreso Total: ${ganancia_mensual:,.0f} / ${total_meta:,.0f}")
        
st.sidebar.caption(f"🖥️ VPS ($300): {'✅ Cubierto' if ganancia_mensual >= costo_vps else '⏳ Pendiente'}")
st.sidebar.caption(f"📡 API ($600): {'✅ Cubierto' if ganancia_mensual >= (costo_vps + costo_api) else '⏳ Pendiente'}")
st.sidebar.caption(f"☕ Extras ($400): {'✅ Cubierto' if ganancia_mensual >= (costo_vps + costo_api + gastos_extra) else '⏳ Pendiente'}")
utilidad_real = max(0, ganancia_mensual - (costo_vps + costo_api + gastos_extra))
st.sidebar.caption(f"💰 Utilidad Neta: ${utilidad_real:,.0f} / ${meta_utilidad:,.0f}")

st.sidebar.markdown("---")

# 3. Telemetría y Estado del Servidor
st.sidebar.subheader("🖥️ Estado del Sistema")
st.sidebar.progress(0.25, text="Consultas API Odds (125/500)")

st.sidebar.info("VPS Hostinger: Activo 🟢")
st.sidebar.success("Última Sincronización: 11:15 AM 🔄")

# ==============================================================================
# PANTALLA PRINCIPAL: RADAR DE JUGADORES (RESPONSIVE)
# ==============================================================================
st.title("📊 Terminal de Partidos")
st.write("Análisis algorítmico y ejecución rápida de órdenes.")
st.markdown("---") 

# Filtro general de partido
partido_seleccionado = st.selectbox(
    "Seleccione el partido a analizar:",
    ["Toronto Blue Jays (L) vs St. Louis Cardinals (V) | 🕒 11:37"]
)

st.markdown("---")

st.subheader("🎯 Radar de Jugadores")
st.write("Demostración de interfaces responsivas para análisis móvil.")

# Creación de los Tabs (Pestañas horizontales)
tab_hits, tab_bases, tab_hr = st.tabs(["🎯 1. Hits (Tarjetas)", "🏃 2. Bases (Tabla)", "🚀 3. Home Runs (Manual)"])

# ------------------------------------------------------------------------------
# TAB 1: OPCIÓN A (Tarjetas Móviles / Acordeones)
# ------------------------------------------------------------------------------
with tab_hits:
    st.subheader("Proyección de Hits (Formato Tarjeta Responsiva)")
    st.write("Diseño optimizado para celular. Los botones de acción rápida están siempre visibles.")
    
    with st.expander("#### George Springer (TOR) | Hits > 0.5 | **✅ EV: +15.4%** | 🔥 Prob: 68.4%"):
        #st.markdown("#### George Springer (TOR) | Hits > 0.5")
        #st.markdown("**✅ EV: +15.4%** | 🔥 Prob: 68.4%")
        
        # Botones de acción rápida siempre visibles
        col_btn1, col_btn2, col_btn3 = st.columns(3)
        col_btn1.button("Caliente", key="c_springer", use_container_width=True)
        col_btn2.button("Winpot", key="w_springer", use_container_width=True)
        col_btn3.button("Playdoit", key="p_springer", use_container_width=True)
        
        d1, d2, d3, d4 = st.columns(4)
        d1.metric("Racha", "2-1-1-4-1")
        d2.metric("Momio", "1.65")
        d3.metric("Sug. Kelly", "$12.50")
        d4.metric("Retorno", "$20.62")

    # Simulación de un jugador EV-
    with st.container(border=True):
        st.markdown("#### Vladimir Guerrero Jr. (TOR) | Hits > 0.5")
        st.markdown("**❌ EV: -9.6%** | 📊 Prob: 42.0%")
        
        col_btn4, col_btn5, col_btn6 = st.columns(3)
        col_btn4.button("Caliente", key="c_vlad", use_container_width=True, disabled=True)
        col_btn5.button("Winpot", key="w_vlad", use_container_width=True, disabled=True)
        col_btn6.button("Playdoit", key="p_vlad", use_container_width=True, disabled=True)
        
        with st.expander("Ver Detalles Analíticos"):
            d1, d2, d3, d4 = st.columns(4)
            d1.metric("Racha", "1-0-1-0-0")
            d2.metric("Momio", "2.15")
            d3.metric("Sug. Kelly", "$0.00")
            d4.metric("Retorno", "$0.00")

# ------------------------------------------------------------------------------
# TAB 2: OPCIÓN B (Tabla con Scroll Horizontal)
# ------------------------------------------------------------------------------
with tab_bases:
    st.subheader("Proyección de Bases (Formato Tabla Nativa)")
    st.write("Deslice hacia la izquierda o derecha en su celular para ver todas las columnas.")
    
    # Simulación de datos
    datos_tabla = {
        "Jugador": ["Alec Burleson", "Ernie Clement", "Jordan Walker"],
        "Mercado": ["Bases > 1.5", "Bases > 0.5", "Bases > 1.5"],
        "EV": ["+12.1%", "-5.4%", "+8.3%"],
        "Prob (Px)": ["58.5%", "45.2%", "52.1%"],
        "Racha": ["2-1-1-1-0", "1-0-1-1-1", "2-3-0-1-0"],
        "Momio": ["1.95", "2.10", "2.05"],
        "Sug. Kelly": ["$15.00", "$0.00", "$10.50"]
    }
    df_bases = pd.DataFrame(datos_tabla)
    
    # st.dataframe activa automáticamente el scroll horizontal en móviles
    st.dataframe(df_bases, use_container_width=False, hide_index=True)

# ------------------------------------------------------------------------------
# TAB 3: CALCULADORA MANUAL DE HOME RUNS (MODO HÍBRIDO)
# ------------------------------------------------------------------------------
with tab_hr:
    st.subheader("Proyección de Hits (Formato Tarjeta Responsiva)")
            
    st.write("Diseño optimizado para celular. Los botones de acción rápida están siempre visibles.")
    # Simulación de un jugador EV+
    with st.expander("#### George Springer (TOR) | Hits > 0.5 | **✅ EV: +15.4%** | 🔥 Prob: 68.4%"):
        #st.markdown("#### George Springer (TOR) | Hits > 0.5")
        #st.markdown("**✅ EV: +15.4%** | 🔥 Prob: 68.4%")
        
        # Botones de acción rápida siempre visibles
        col_btn1, col_btn2, col_btn3 = st.columns(3)
        col_btn1.button("Caliente", key="c_springer", use_container_width=True)
        col_btn2.button("Winpot", key="w_springer", use_container_width=True)
        col_btn3.button("Playdoit", key="p_springer", use_container_width=True)
        
        d1, d2, d3, d4 = st.columns(4)
        d1.metric("Racha", "2-1-1-4-1")
        d2.number_input("Momio", min_value=1, value=10)
        d3.metric("Sug. Kelly", "$12.50")
        d4.metric("Retorno", "$20.62")


st.header("🔥 Parlays de hoy")
st.write("Esta es la descripción de la página. Aquí puede detallar el propósito del dashboard, instrucciones de uso o cualquier contexto relevante para el análisis.")

st.markdown("---") # Línea divisoria horizontal

st.subheader("I TOP 8 PARLAY HITS JUGADORES") #Aqui vamos calcular parlays de 3 o 4  con la mejor Prob y con EV positivo, el siguiente parlay será con los que tienen menor cantidad de prob, y el último parlay sea el soñado.

# ==============================================================================
# VARIANTE 2: ENFOQUE EN MÉTRICAS (MÁS VISUAL Y MODERNO)
# ==============================================================================
with st.expander("Parlay 2 (Agresivo) | Cuota: 4.50 | Prob: 35.2%", expanded=False):
    
    # Dividimos las selecciones en columnas en lugar de lista hacia abajo
    sel1, sel2 = st.columns(2)
    sel1.success("**Pick 2:** Lane Thomas (WSH) | Bases > 1.5 (Prob: 50%)")
    sel2.success("**Pick 2:** Lane Thomas (WSH) | Bases > 1.5 (Prob: 50%)")

        # Dividimos las selecciones en columnas en lugar de lista hacia abajo
    sel3, sel4 = st.columns(2)
    sel3.success("**Pick 1:** CJ Abrams (WSH) | Hits > 1.5 (Prob: 45%)")
    sel4.success("**Pick 2:** Lane Thomas (WSH) | Bases > 1.5 (Prob: 50%)")
    
    st.markdown("---")
    
    # Usamos st.metric para números grandes y llamativos
    m1, m2, m3, m4 = st.columns(4)
    m1.metric(label="Inversión Sugerida", value="$25.00")
    m2.metric(label="Retorno (Payout)", value="$112.50", delta="Rentable")
    m3.metric(label="Ventaja (EV)", value="+18.5%", delta="EV Positivo", delta_color="normal")
    
    with m4:
        st.write("")
        st.button("Ejecutar Parlay 2", key="btn_v2", type="primary") # type="primary" lo pone de color rojo/destacado

st.markdown("---") # Línea divisoria horizontal

st.subheader("I TOP 8 PARLAY BASES JUGADORES") #Aqui vamos calcular parlays de 3 o 4  con la mejor Prob y con EV positivo, el siguiente parlay será con los que tienen menor cantidad de prob, y el último parlay sea el soñado.

# ==============================================================================
# VARIANTE 2: ENFOQUE EN MÉTRICAS (MÁS VISUAL Y MODERNO)
# ==============================================================================
with st.expander("Parlay 2 (Agresivo) | Cuota: 4.50 | Prob: 35.2%", expanded=False):
    
    # Dividimos las selecciones en columnas en lugar de lista hacia abajo
    sel9, sel10 = st.columns(2)
    sel9.success("**Pick 2:** Lane Thomas (WSH) | Bases > 1.5 (Prob: 50%)")
    sel10.success("**Pick 2:** Lane Thomas (WSH) | Bases > 1.5 (Prob: 50%)")

        # Dividimos las selecciones en columnas en lugar de lista hacia abajo
    sel11, sel12 = st.columns(2)
    sel11.success("**Pick 1:** CJ Abrams (WSH) | Hits > 1.5 (Prob: 45%)")
    sel12.success("**Pick 2:** Lane Thomas (WSH) | Bases > 1.5 (Prob: 50%)")
    
    st.markdown("---")
    
    # Usamos st.metric para números grandes y llamativos
    m9, m10, m11, m12 = st.columns(4)
    m9.metric(label="Inversión Sugerida", value="$25.00")
    m10.metric(label="Retorno (Payout)", value="$112.50", delta="Rentable")
    m11.metric(label="Ventaja (EV)", value="+18.5%", delta="EV Positivo", delta_color="normal")
    
    with m12:
        st.write("")
        st.button("Ejecutar Parlay 2", key="btn_v3", type="primary") # type="primary" lo pone de color rojo/destacado

st.markdown("---") # Línea divisoria horizontal

st.subheader("I PARLAY POR PARTIDO")
st.subheader("Menú desplegable")

st.markdown("---")

# ==============================================================================
# PARLAY POR PARTIDO
# ==============================================================================

with st.expander("TOP 2 Miami Marlins vs Phillies | Cuota: 4.50 | Prob: 35.2%", expanded=False): #Aqui vamos calcular parlays de 2 parlays con mejor prob, mezclando hits por equipo, hits por jugador, carreras, etc.
    # Dividimos las selecciones en columnas en lugar de lista hacia abajo
    sel5, sel6 = st.columns(2)
    sel5.success("**Pick 2:** Lane Thomas (WSH) | Bases > 1.5 (Prob: 50%)")
    sel6.success("**Pick 2:** Lane Thomas (WSH) | Bases > 1.5 (Prob: 50%)")

        # Dividimos las selecciones en columnas en lugar de lista hacia abajo
    sel7, sel8 = st.columns(2)
    sel7.success("**Pick 1:** CJ Abrams (WSH) | Hits > 1.5 (Prob: 45%)")
    sel8.success("**Pick 2:** Lane Thomas (WSH) | Bases > 1.5 (Prob: 50%)")
    
    st.markdown("---")
    
    # Usamos st.metric para números grandes y llamativos
    m5, m6, m7, m8 = st.columns(4)
    m5.metric(label="Inversión Sugerida", value="$25.00")
    m6.metric(label="Retorno (Payout)", value="$112.50", delta="Rentable")
    m7.metric(label="Ventaja (EV)", value="+18.5%", delta="EV Positivo", delta_color="normal")
    
    with m8:
        st.write("")
        st.button("Ejecutar Parlay 2", key="btn_v4", type="primary") # type="primary" lo pone de color rojo/destacado
