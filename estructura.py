import streamlit as st




# ==========================================
# 1. TÍTULO Y DESCRIPCIÓN
# ==========================================
st.title("📊 Partidos de hoy")
st.write("Seleccione un encuentro para analizar las proyecciones algorítmicas de Hits y Carreras esperadas, contrastadas contra los momios del casino en tiempo real.")

st.markdown("---") 

# ==========================================
# 2. MENÚ DESPLEGABLE DE PARTIDOS
# ==========================================
opcion_elegida = st.selectbox(
    "Seleccione un partido:", 
    [
        "Washington Nationals (L) vs Atlanta Braves (V)", 
        "Chicago Cubs (L) vs St. Louis Cardinals (V)",
        "Miami Marlins (L) vs Philadelphia Phillies (V)"
    ]
)

st.markdown("---")

# ==============================================================================
# CONTENEDOR GENERAL: EQUIPO LOCAL
# ==============================================================================
with st.container():
    # Encabezado del equipo con indicador de probabilidad de victoria (Moneyline)
    st.subheader("🔵 Washington Nationals - Local | ✅ Prob: 65%") 
    
    # --- Subcontenedor 1: HITS ESPERADOS (Local) ---
    st.markdown("**🎯 Proyección de Hits**")
    
    # Definimos 7 columnas (damos un poco más de ancho a la primera y última para el texto y botón)
    l_c1, l_c2, l_c3, l_c4, l_c5, l_c6, l_c7 = st.columns([1.5, 1, 1, 1, 1, 1.2, 1.5])
    
    # Encabezados
    l_c1.write("**Racha**")
    l_c2.write("**Hoy**")
    l_c3.write("**Momio**")
    l_c4.write("**Px**")
    l_c5.write("**Sug.**")
    l_c6.write("**Retorno**")
    l_c7.write("**Acción**")
    
    # Fila de Datos Simulares
    l_c1.write("6-5-4-3-2") 
    l_c2.write("+7.5") 
    l_c3.write("-120") 
    l_c4.write("65%") 
    l_c5.write("$15.00") 
    l_c6.write("$25.89") 
    l_c7.button("Apuesta", key="btn_loc_hits", use_container_width=True)
    
    st.write("") # Espacio en blanco para respirar
    
    # --- Subcontenedor 2: CARRERAS ESPERADAS (Local) ---
    st.markdown("**🏃 Proyección de Carreras**")
    l_d1, l_d2, l_d3, l_d4, l_d5, l_d6, l_d7 = st.columns([1.5, 1, 1, 1, 1, 1.2, 1.5])
    
    # Encabezados
    l_d1.write("**Racha**")
    l_d2.write("**Hoy**")
    l_d3.write("**Momio**")
    l_d4.write("**Px**")
    l_d5.write("**Sug.**")
    l_d6.write("**Retorno**")
    l_d7.write("**Acción**")
    
    # Fila de Datos Simulados
    l_d1.write("10-9-4-5-4")
    l_d2.write("+4.5")
    l_d3.write("120")
    l_d4.write("45%")
    l_d5.write("$15.00")
    l_d6.write("$25.00")
    l_d7.button("Apuesta", key="btn_loc_runs", use_container_width=True)

st.markdown("---") # Divisor visual entre equipos

# ==============================================================================
# CONTENEDOR GENERAL: EQUIPO VISITANTE
# ==============================================================================
with st.container():
    # Encabezado del equipo visitante
    st.subheader("🔴 Atlanta Braves - Visitante | ❌ Prob: 35%")
    
    # --- Subcontenedor 1: HITS ESPERADOS (Visitante) ---
    st.markdown("**🎯 Proyección de Hits**")
    v_c1, v_c2, v_c3, v_c4, v_c5, v_c6, v_c7 = st.columns([1.5, 1, 1, 1, 1, 1.2, 1.5])
    
    # Encabezados
    v_c1.write("**Racha**")
    v_c2.write("**Hoy**")
    v_c3.write("**Momio**")
    v_c4.write("**Px**")
    v_c5.write("**Sug.**")
    v_c6.write("**Retorno**")
    v_c7.write("**Acción**")
    
    # Fila de Datos Simulados
    v_c1.write("5-4-6-4-5")
    v_c2.write("-6.5")
    v_c3.write("135")
    v_c4.write("56%")
    v_c5.write("$10.00")
    v_c6.write("$45.87")
    v_c7.button("Apuesta", key="btn_vis_hits", use_container_width=True)
    
    st.write("") # Espacio en blanco
    
    # --- Subcontenedor 2: CARRERAS ESPERADAS (Visitante) ---
    st.markdown("**🏃 Proyección de Carreras**")
    v_d1, v_d2, v_d3, v_d4, v_d5, v_d6, v_d7 = st.columns([1.5, 1, 1, 1, 1, 1.2, 1.5])
    
    # Encabezados
    v_d1.write("**Racha**")
    v_d2.write("**Hoy**")
    v_d3.write("**Momio**")
    v_d4.write("**Px**")
    v_d5.write("**Sug.**")
    v_d6.write("**Retorno**")
    v_d7.write("**Acción**")
    
    # Fila de Datos Simulados
    v_d1.write("4-5-6-7-8")
    v_d2.write("+4.5")
    v_d3.write("200")
    v_d4.write("56%")
    v_d5.write("$15.00")
    v_d6.write("$34.60")
    v_d7.button("Apuesta", key="btn_vis_runs", use_container_width=True)

st.markdown("---")

# ==============================================================================
# MÓDULO 2: RADAR DE JUGADORES (PROPS INDIVIDUALES)
# ==============================================================================
st.header("🎯 Radar de Jugadores")
st.write("Análisis individual de bateadores. Expanda cada tarjeta para ver la ventaja matemática (EV+).")

# --- SECCIÓN 1: HITS ---
st.subheader("1. Proyección de Hits")
with st.expander("Tommy White (Athletics) | batter_hits > 0.5 | ✅ Prob: 74.4%"):
    c1, c2, c3, c4, c5 = st.columns([1.5, 1.5, 1, 1, 1.2])
    
    with c1:
        st.write("Racha Reciente")
        st.subheader("1-0-2-0-4")
    with c2:
        st.write("Probabilidad Modelo")
        st.subheader("74.4%")
    with c3:
        st.write("Cuota Casino")
        st.subheader("1.43")
    with c4:
        st.write("Sug. Kelly")
        st.subheader("$10.00")
    with c5:
        st.write("Retorno: $14.30")
        st.button("Ejecutar Apuesta", key="btn_hit_1", use_container_width=True)

# --- SECCIÓN 2: BASES TOTALES ---
st.subheader("2. Proyección de Bases Totales")
with st.expander("Lane Thomas (WSH) | batter_bases > 1.5 | ✅ Prob: 55.0%"):
    d1, d2, d3, d4, d5 = st.columns([1.5, 1.5, 1, 1, 1.2])
    
    with d1:
        st.write("Racha Reciente")
        st.subheader("2-1-3-0-2")
    with d2:
        st.write("Probabilidad Modelo")
        st.subheader("55.0%")
    with d3:
        st.write("Cuota Casino")
        st.subheader("1.85")
    with d4:
        st.write("Sug. Kelly")
        st.subheader("$15.00")
    with d5:
        st.write("Retorno: $27.75")
        st.button("Ejecutar Apuesta", key="btn_base_1", use_container_width=True)

# --- SECCIÓN 3: HOME RUNS ---
st.subheader("3. Proyección de Home Runs")
with st.expander("CJ Abrams (WSH) | batter_home_runs > 0.5 | 🔥 Prob: 28.5%"):
    f1, f2, f3, f4, f5 = st.columns([1.5, 1.5, 1, 1, 1.2])
    
    with f1:
        st.write("Racha Reciente")
        st.subheader("0-0-1-0-1")
    with f2:
        st.write("Probabilidad Modelo")
        st.subheader("28.5%")
    with f3:
        st.write("Cuota Casino")
        st.subheader("3.20")
    with f4:
        st.write("Sug. Kelly")
        st.subheader("$5.00")
    with f5:
        st.write("Retorno: $16.00")
        st.button("Ejecutar Apuesta", key="btn_hr_1", use_container_width=True)

st.markdown("---")

# ==============================================================================
# MÓDULO 3: MÁQUINA DE PARLAYS DINÁMICOS
# ==============================================================================
st.header("🔥 Parlays de hoy")
st.write("Combinaciones algorítmicas con Valor Esperado (EV) Positivo. El motor cruza las mejores probabilidades y aplica bonos de correlación ofensiva.")

st.markdown("---")

# --- SECCIÓN 1: PARLAYS DE HITS ---
st.subheader("I TOP 8 PARLAY HITS JUGADORES")

with st.expander("Parlay 1 (Hits - Agresivo) | Cuota: 4.50 | Prob: 35.2%", expanded=False):
    
    st.info("💡 Correlación Ofensiva: Bateadores en racha enfrentando a un pitcher con WHIP > 1.40")
    
    # 4 Picks divididos en dos filas de 2 columnas
    sel1, sel2 = st.columns(2)
    sel1.success("**Pick 1:** CJ Abrams (WSH) | Hits > 0.5 (Prob: 65%)")
    sel2.success("**Pick 2:** Lane Thomas (WSH) | Hits > 0.5 (Prob: 62%)")

    sel3, sel4 = st.columns(2)
    sel3.success("**Pick 3:** Luis Garcia (WSH) | Hits > 0.5 (Prob: 58%)")
    sel4.success("**Pick 4:** Jesse Winker (WSH) | Hits > 0.5 (Prob: 55%)")
    
    st.markdown("---")
    
    # Métricas financieras del Parlay
    m1, m2, m3, m4 = st.columns(4)
    m1.metric(label="Inversión Sugerida", value="$25.00")
    m2.metric(label="Retorno (Payout)", value="$112.50", delta="Rentable")
    m3.metric(label="Ventaja (EV)", value="+18.5%", delta="EV Positivo", delta_color="normal")
    
    with m4:
        st.write("")
        st.button("Ejecutar Parlay 1", key="btn_parlay_hits_1", type="primary")

st.markdown("---")

# --- SECCIÓN 2: PARLAYS DE BASES TOTALES ---
st.subheader("I TOP 8 PARLAY BASES JUGADORES")

with st.expander("Parlay 2 (Bases - Conservador) | Cuota: 3.10 | Prob: 42.1%", expanded=False):
    
    sel5, sel6 = st.columns(2)
    sel5.success("**Pick 1:** Marcell Ozuna (ATL) | Bases > 1.5 (Prob: 52%)")
    sel6.success("**Pick 2:** Austin Riley (ATL) | Bases > 1.5 (Prob: 50%)")

    sel7, sel8 = st.columns(2)
    sel7.success("**Pick 3:** Matt Olson (ATL) | Bases > 0.5 (Prob: 60%)")
    sel8.success("**Pick 4:** Ozzie Albies (ATL) | Bases > 0.5 (Prob: 61%)")
    
    st.markdown("---")
    
    m5, m6, m7, m8 = st.columns(4)
    m5.metric(label="Inversión Sugerida", value="$30.00")
    m6.metric(label="Retorno (Payout)", value="$93.00", delta="Rentable")
    m7.metric(label="Ventaja (EV)", value="+12.4%", delta="EV Positivo", delta_color="normal")
    
    with m8:
        st.write("")
        st.button("Ejecutar Parlay 2", key="btn_parlay_bases_1", type="primary")

st.markdown("---")

# --- SECCIÓN 3: PARLAY FILTRADO POR PARTIDO ---
st.subheader("I PARLAY POR PARTIDO")
st.write("Filtre las combinaciones matemáticas exclusivas para un encuentro específico.")

# Menú desplegable con clave única
partido_parlays = st.selectbox(
    "Seleccione el partido para ver sus Parlays:",
    [
        "Miami Marlins (L) vs Philadelphia Phillies (V)",
        "Washington Nationals (L) vs Atlanta Braves (V)",
        "Chicago Cubs (L) vs St. Louis Cardinals (V)"
    ],
    key="selector_parlay_unico"
)

st.markdown("---")

# El título del expander es dinámico según lo que se elija arriba
with st.expander(f"TOP 2 {partido_parlay} | Cuota: 5.20 | Prob: 31.8%", expanded=False): 
    
    sel9, sel10 = st.columns(2)
    sel9.success("**Pick 1:** Jazz Chisholm (MIA) | Bases > 1.5 (Prob: 48%)")
    sel10.success("**Pick 2:** Bryan De La Cruz (MIA) | Hits > 0.5 (Prob: 55%)")

    sel11, sel12 = st.columns(2)
    sel11.success("**Pick 3:** Bryce Harper (PHI) | Bases > 1.5 (Prob: 51%)")
    sel12.success("**Pick 4:** Trea Turner (PHI) | Hits > 0.5 (Prob: 62%)")
    
    st.markdown("---")
    
    m9, m10, m11, m12 = st.columns(4)
    m9.metric(label="Inversión Sugerida", value="$20.00")
    m10.metric(label="Retorno (Payout)", value="$104.00", delta="Rentable")
    m11.metric(label="Ventaja (EV)", value="+15.2%", delta="EV Positivo", delta_color="normal")
    
    with m12:
        st.write("")
        st.button("Ejecutar Parlay", key="btn_ejecutar_parlay_partido", type="primary")
