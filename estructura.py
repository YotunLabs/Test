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

# 1. Gestión de Carteras (Bankroll Fraccionado)
st.sidebar.subheader("💰 Carteras de Inversión")
saldo_caliente = 5450.00
saldo_winpot = 4000.00
saldo_playdoit = 3500.00
saldo_otro = 2500.00
capital_total = saldo_caliente + saldo_winpot + saldo_playdoit + saldo_otro

st.sidebar.metric(label="Capital Neto Disponible", value=f"${capital_total:,.2f} MXN")

c1, c2 = st.sidebar.columns(2)
c1.metric("Caliente", f"${saldo_caliente:,.0f}")
c2.metric("Winpot", f"${saldo_winpot:,.0f}")
c1.metric("Playdoit", f"${saldo_playdoit:,.0f}")
c2.metric("Otro", f"${saldo_otro:,.0f}")

st.sidebar.markdown("---")

# 2. Cascada de Amortización y Meta Mensual
st.sidebar.subheader("📈 Meta Mensual (Cascada)")
ingresos_mes = 1850.00 # Dinero ganado este mes (simulación)
gastos_operativos = 1300.00 # 300 VPS + 600 API + 400 Extras
meta_neta = 5000.00
meta_bruta = gastos_operativos + meta_neta

# Lógica visual de la cascada
if ingresos_mes <= gastos_operativos:
    progreso_gastos = ingresos_mes / gastos_operativos
    st.sidebar.progress(progreso_gastos, text=f"Cubriendo Operación: ${ingresos_mes:,.0f} / ${gastos_operativos:,.0f}")
    st.sidebar.progress(0.0, text=f"Ganancia Neta: $0 / ${meta_neta:,.0f}")
else:
    st.sidebar.progress(1.0, text=f"Operación Cubierta ✅ (${gastos_operativos:,.0f})")
    ganancia_real = ingresos_mes - gastos_operativos
    progreso_meta = min(ganancia_real / meta_neta, 1.0)
    st.sidebar.progress(progreso_meta, text=f"Ganancia Neta: ${ganancia_real:,.0f} / ${meta_neta:,.0f}")

st.sidebar.markdown("---")

# 3. Telemetría y Estado del Servidor
st.sidebar.subheader("🖥️ Estado del Sistema")
st.sidebar.progress(0.25, text="Consultas API Odds (125/500)")

st.sidebar.info("VPS Hostinger: Activo 🟢")
st.sidebar.success("Última Sincronización: 11:15 AM 🔄")

# ==============================================================================
# PANTALLA PRINCIPAL: RADAR DE JUGADORES (RESPONSIVE)
# ==============================================================================
st.title("🎯 Radar de Jugadores")
st.write("Demostración de interfaces responsivas para análisis móvil.")

# Filtro general de partido
partido_seleccionado = st.selectbox(
    "Seleccione el partido a analizar:",
    ["Toronto Blue Jays (L) vs St. Louis Cardinals (V) | 🕒 11:37"]
)
st.markdown("---")

# Creación de los Tabs (Pestañas horizontales)
tab_hits, tab_bases, tab_hr = st.tabs(["🎯 1. Hits (Tarjetas)", "🏃 2. Bases (Tabla)", "🚀 3. Home Runs (Manual)"])

# ------------------------------------------------------------------------------
# TAB 1: OPCIÓN A (Tarjetas Móviles / Acordeones)
# ------------------------------------------------------------------------------
with tab_hits:
    st.subheader("Proyección de Hits (Formato Tarjeta Responsiva)")
    st.write("Diseño optimizado para celular. Los botones de acción rápida están siempre visibles.")
    
    # Simulación de un jugador EV+
    with st.container(border=True, ✅ EV: +15.4%** | 🔥 Prob: 68.4% | George Springer (TOR) | Hits > 0.5""):
        st.markdown("#### George Springer (TOR) | Hits > 0.5")
        st.markdown("**✅ EV: +15.4%** | 🔥 Prob: 68.4%")
        
        # Botones de acción rápida siempre visibles
        col_btn1, col_btn2, col_btn3 = st.columns(3)
        col_btn1.button("Caliente", key="c_springer", use_container_width=True)
        col_btn2.button("Winpot", key="w_springer", use_container_width=True)
        col_btn3.button("Playdoit", key="p_springer", use_container_width=True)

        with st.expander():
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
    st.subheader("Calculadora Híbrida en RAM (Home Runs)")
    st.write("Ingrese el momio americano (ej. +350) para ejecutar el modelo matemático en tiempo real.")
    
    col_input1, col_input2 = st.columns([2, 1])
    
    with col_input1:
        jugador_hr = st.selectbox("Seleccione Bateador:", ["George Springer (TOR)", "Vladimir Guerrero Jr. (TOR)", "Nolan Arenado (STL)"])
        
        # Simulación: El sistema ya tiene la Px pura calculada por el modelo (60%)
        prob_modelo_pura = 0.18 # 18% de probabilidad de HR según nuestra BD
        st.caption(f"Racha HR: 0-1-0-0-0 | Probabilidad Base Modelo: {prob_modelo_pura*100:.1f}%")
        
    with col_input2:
        momio_americano = st.text_input("Momio Americano:", placeholder="Ej: +450 o -110")
        
    if momio_americano:
        try:
            # Conversión Matemática: Americano a Decimal
            momio_num = float(momio_americano)
            if momio_num > 0:
                momio_decimal = (momio_num / 100) + 1
            else:
                momio_decimal = (100 / abs(momio_num)) + 1
                
            # Probabilidad Implícita del Casino (40%)
            prob_casino = 1 / momio_decimal
            
            # Fusión Híbrida 60/40
            px_hibrida = (prob_modelo_pura * 0.60) + (prob_casino * 0.40)
            
            # Cálculo de EV
            ventaja_ev = (px_hibrida * momio_decimal) - 1
            
            # Fórmula de Kelly (Reducida al 25% por gestión de riesgo)
            b = momio_decimal - 1.0
            q = 1.0 - px_hibrida
            kelly_puro = ((px_hibrida * b) - q) / b
            kelly_sugerido = (capital_total * kelly_puro * 0.25) if kelly_puro > 0 else 0.0
            
            # Despliegue de Resultados Rápidos
            st.markdown("---")
            r1, r2, r3, r4 = st.columns(4)
            r1.metric("Px Híbrida", f"{px_hibrida*100:.1f}%")
            r2.metric("Momio Decimal", f"{momio_decimal:.2f}")
            r3.metric("Ventaja (EV)", f"{ventaja_ev*100:+.1f}%", delta="EV+" if ventaja_ev > 0 else "-EV", delta_color="normal" if ventaja_ev > 0 else "inverse")
            r4.metric("Kelly Sugerido", f"${kelly_sugerido:,.2f}")
            
            if ventaja_ev > 0:
                st.success("¡Apuesta Rentable! Seleccione la cartera para registrar la operación:")
                b1, b2, b3 = st.columns(3)
                b1.button("Disparar en Caliente", use_container_width=True)
                b2.button("Disparar en Winpot", use_container_width=True)
                b3.button("Disparar en Playdoit", use_container_width=True)
            else:
                st.error("El momio ingresado no ofrece valor matemático suficiente para disparar.")
                
        except ValueError:
            st.warning("Por favor ingrese un momio americano válido (solo números y signos + o -).")
