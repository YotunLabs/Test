import streamlit as st

# ==========================================
# 1. TÍTULO Y DESCRIPCIÓN
# ==========================================
st.header("📊 Partidos de hoy")
st.write("Esta es la descripción de la página. Aquí puede detallar el propósito del dashboard, instrucciones de uso o cualquier contexto relevante para el análisis.")

st.markdown("---") # Línea divisoria horizontal

# ==========================================
# 2. MENÚ DESPLEGABLE
# ==========================================
opcion_elegida = st.selectbox(
    "Seleccione un partido:", #Aquí se almacenan los partidos del día.
    [
        "Washington Nationals (L) vs Atlanta Braves (V)", 
        "Chicago Cubs (L) vs St. Louis Cardinals (V)"
    ]
)

st.markdown("---")

# ==============================================================================
# CONTENEDOR GENERAL: EQUIPO LOCAL
# ==============================================================================
with st.container():
    # Nombre del equipo (Usamos st.header para que se vea grande) 
    st.subheader("🔵 Washington Nationals - Local ✅ Prob: 65%") #Probabilidad de ganar local o visitante, utilicemos un modelo que nos permita calcular la probabilidad de ganar con base en el historico de la MLB y los momios del casino-
    
    # --- Subcontenedor 1 (7 columnas) ---
    st.subheader("**Hits**")
    l_c1, l_c2, l_c3, l_c4, l_c5, l_c6, l_c7 = st.columns(7)
    
    # Encabezados del Subcontenedor 1
    l_c1.write("**Racha**")
    l_c2.write("**Hoy**")
    l_c3.write("**Momio**")
    l_c4.write("**Px**")
    l_c5.write("**Sug.**")
    l_c6.write("**Retorno**")
    l_c7.write("**Ingresar**")
    
    # Datos del Subcontenedor 1
    l_c1.write("6-5-4-3-2") # Historico de los ultimos 5 juegos del equipo con hits realizados.
    l_c2.write("+7.5") # Hits esperados para este partido podemos hacer el calculo con los hits realizados en historicos, los momios del casino y lanzadores. y determinar la probailidad si es over/under.
    l_c3.write("-120") #Momio del casino
    l_c4.write("65%") #Probabilidad de logar la meta ya sea over/under
    l_c5.write("$15.00") #Calculo Kelly
    l_c6.write("$25.89") #Calculo kelly con el momio extraido.
    l_c7.button("Apuesta", key="btn_loc_1")
    
    st.write("") # Espacio en blanco para separar
    
    # --- Subcontenedor 2 (7 columnas) ---
    st.subheader("**Carreras**")
    l_d1, l_d2, l_d3, l_d4, l_d5, l_d6, l_d7 = st.columns(7)
    
    # Encabezados del Subcontenedor 2
    l_d1.write("**Racha**")
    l_d2.write("**Hoy**")
    l_d3.write("**Momio**")
    l_d4.write("**Px**")
    l_d5.write("**Sug.**")
    l_d6.write("**Retorno**")
    l_d7.write("**Ingresar**")
    
    # Datos del Subcontenedor 2
    l_d1.write("10-9-4-5-4")
    l_d2.write("+4.5")
    l_d3.write("120")
    l_d4.write("45%")
    l_d5.write("$15.00")
    l_d6.write("$25.00")
    l_d7.button("Apuesta", key="btn_loc_2")

st.markdown("---") # Línea divisoria entre equipos

# ==============================================================================
# CONTENEDOR GENERAL: EQUIPO VISITANTE
# ==============================================================================
with st.container():
    # Nombre del equipo
    st.subheader("🔴 Equipo Visitante: Atlanta Braves")
    
    # --- Subcontenedor 1 (7 columnas) ---
    st.subheader("**Hits**")
    v_c1, v_c2, v_c3, v_c4, v_c5, v_c6, v_c7 = st.columns(7)
    
    # Encabezados del Subcontenedor 1
    v_c1.write("**Racha**")
    v_c2.write("**Hoy**")
    v_c3.write("**Momio**")
    v_c4.write("**Px**")
    v_c5.write("**Sug.**")
    v_c6.write("**Retorno**")
    v_c7.write("**Ingresar**")
    
    # Datos del Subcontenedor 1
    v_c1.write("5-4-6-4-5")
    v_c2.write("-6.5")
    v_c3.write("135")
    v_c4.write("56%")
    v_c5.write("$10.00")
    v_c6.write("$45.87")
    v_c7.button("Apuesta", key="btn_vis_1")
    
    st.write("") # Espacio en blanco
    
    # --- Subcontenedor 2 (7 columnas) ---
    st.subheader("**Carreras**")
    v_d1, v_d2, v_d3, v_d4, v_d5, v_d6, v_d7 = st.columns(7)
    
    # Encabezados del Subcontenedor 2
    v_d1.write("**Racha**")
    v_d2.write("**Hoy**")
    v_d3.write("**Momio**")
    v_d4.write("**Px**")
    v_d5.write("**Sug.**")
    v_d6.write("**Retorno**")
    v_d7.write("**Ingresar**")
    
    # Datos del Subcontenedor 2
    v_d1.write("4-5-6-7-8")
    v_d2.write("+4.5")
    v_d3.write("200")
    v_d4.write("56%")
    v_d5.write("$15.00")
    v_d6.write("$34.60")
    v_d7.button("Apuesta", key="btn_vis_2")

st.markdown("---")
# ==========================================
# 3. CONTENEDORES DESPLEGABLES (EXPANDERS)
# ==========================================
st.write("🎯 Hits jugadores")

# Vaciamos hits 
with st.expander("Tommy White (Athletics) | batter_hits > 0.5 | ✅ Prob: 74.4%"): #Agregamos el indicador de que esta apuesta tiene altas probabilidades de lograrse y es rentable.
    
    # Aquí definimos las columnas. Los números son proporciones de ancho.
    # Usamos 5 columnas para replicar los 5 bloques de su imagen.
    c1, c2, c3, c4, c5 = st.columns([1.5, 1.5, 1, 1, 1.2])
    
    # Llenado de la Columna 1
    with c1:
        st.write("Racha Reciente") #Racha de los últimos 5 juegos
        st.subheader("1-0-2-0-4")
        
    # Llenado de la Columna 2
    with c2:
        st.write("Probabilidad Modelo") #Calculamos la probabilidad de lograr con base en el historico, racha, momio del casino y los lanzadores-
        st.subheader("74.4%")
        
    # Llenado de la Columna 3
    with c3:
        st.write("Cuota Casino") #Indicamos la cuota del casino
        st.subheader("1.43")
        
    # Llenado de la Columna 4
    with c4:
        st.write("Sug.") #Calculo Kelly
        st.subheader("$10.00")
        
    # Llenado de la Columna 5 (Botón)
    with c5:
        st.write("Retorno: $14.30") #GAnancia
        # El parámetro 'key' es obligatorio y debe ser único para cada botón en Streamlit
        st.button("Ejecutar Apuesta", key="btn_ejemplo_1")
        
st.write("🎯 Bases jugadores")    
# Vachiamos Bases
with st.expander("Tommy White (Athletics) | batter_bases > 0.5 | Prob: 74.4%"):
    
    # Aquí definimos las columnas. Los números son proporciones de ancho.
    # Usamos 5 columnas para replicar los 5 bloques de su imagen.
    d1, d2, d3, d4, d5 = st.columns([1.5, 1.5, 1, 1, 1.2])
    
    # Llenado de la Columna 1
    with d1:
        st.write("Racha Reciente")
        st.subheader("1-0-2-0-4")
        
    # Llenado de la Columna 2
    with d2:
        st.write("Probabilidad Modelo")
        st.subheader("74.4%")
        
    # Llenado de la Columna 3
    with d3:
        st.write("Cuota Casino")
        st.subheader("1.43")
        
    # Llenado de la Columna 4
    with d4:
        st.write("Apuesta Kelly")
        st.subheader("$10.00")
        
    # Llenado de la Columna 5 (Botón)
    with d5:
        st.write("Retorno: $14.30")
        # El parámetro 'key' es obligatorio y debe ser único para cada botón en Streamlit
        st.button("Ejecutar Apuesta", key="btn_ejemplo_2")

st.write("🎯 HomeRun Jugadores)")
# Vaciamos HR
with st.expander("Tommy White (Athletics) | HomeRuns > 0.5 | Prob: 74.4%"):
    
    # Aquí definimos las columnas. Los números son proporciones de ancho.
    # Usamos 5 columnas para replicar los 5 bloques de su imagen.
    f1, f2, f3, f4, f5 = st.columns([1.5, 1.5, 1, 1, 1.2])
    
    # Llenado de la Columna 1
    with f1:
        st.write("Racha Reciente")
        st.subheader("1-0-2-0-4")
        
    # Llenado de la Columna 2
    with f2:
        st.write("Probabilidad Modelo")
        st.subheader("74.4%")
        
    # Llenado de la Columna 3
    with f3:
        st.write("Cuota Casino")
        st.subheader("1.43")
        
    # Llenado de la Columna 4
    with f4:
        st.write("Apuesta Kelly")
        st.subheader("$10.00")
        
    # Llenado de la Columna 5 (Botón)
    with f5:
        st.write("Retorno: $14.30")
        # El parámetro 'key' es obligatorio y debe ser único para cada botón en Streamlit
        st.button("Ejecutar Apuesta", key="btn_ejemplo_3")

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
st.write("Filtre las combinaciones matemáticas exclusivas para un encuentro específico.")

# ==============================================================================
# MENÚ DESPLEGABLE (CON IDENTIFICADOR ÚNICO)
# ==============================================================================
partido_parlay = st.selectbox(
    "Seleccione el partido para ver sus Parlays:",
    [
        "Miami Marlins (L) vs Philadelphia Phillies (V)",
        "Washington Nationals (L) vs Atlanta Braves (V)",
        "Chicago Cubs (L) vs St. Louis Cardinals (V)"
    ],
    key="selector_parlay_unico" # Este key es vital para que no choque con el menú de la pestaña En Vivo
)

st.markdown("---")

# ==============================================================================
# CONTENEDOR DEL PARLAY (EL TÍTULO SE ADAPTA AL PARTIDO SELECCIONADO)
# ==============================================================================
# Usamos una variable f"" para que el título del expander cambie según lo que se elija arriba
with st.expander(f"TOP 2 {partido_parlay} | Cuota: 4.50 | Prob: 35.2%", expanded=False): 
    
    # Dividimos las selecciones en columnas en lugar de lista hacia abajo
    sel5, sel6 = st.columns(2)
    sel5.success("**Pick 1:** CJ Abrams (WSH) | Hits > 1.5 (Prob: 45%)")
    sel6.success("**Pick 2:** Lane Thomas (WSH) | Bases > 1.5 (Prob: 50%)")

    sel7, sel8 = st.columns(2)
    sel7.success("**Pick 3:** Luis Arraez (MIA) | Hits > 0.5 (Prob: 65%)")
    sel8.success("**Pick 4:** Jazz Chisholm (MIA) | Bases > 0.5 (Prob: 55%)")
    
    st.markdown("---")
    
    # Métricas de finanzas
    m5, m6, m7, m8 = st.columns(4)
    m5.metric(label="Inversión Sugerida", value="$25.00")
    m6.metric(label="Retorno (Payout)", value="$112.50", delta="Rentable")
    m7.metric(label="Ventaja (EV)", value="+18.5%", delta="EV Positivo", delta_color="normal")
    
    with m8:
        st.write("")
        st.button("Ejecutar Parlay", key="btn_ejecutar_parlay_partido", type="primary")



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
partido_parlay = st.selectbox(
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
