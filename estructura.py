import streamlit as st
import pandas as pd

# ==========================================
# 1. TÍTULO Y DESCRIPCIÓN
# ==========================================
st.title("📊 Tablero de Prototipado Visual")
st.write("Esta es la descripción de la página. Aquí puede detallar el propósito del dashboard, instrucciones de uso o cualquier contexto relevante para el análisis.")

st.markdown("---") # Línea divisoria horizontal

# ==========================================
# 2. MENÚ DESPLEGABLE
# ==========================================
opcion_elegida = st.selectbox(
    "Seleccione el Partido (Ejemplo de Menú Desplegable):",
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
    st.header("🔵 Equipo Local: Washington Nationals")
    
    # --- Subcontenedor 1 (7 columnas) ---
    st.markdown("**Bloque 1: Estadísticas de Hits (Ejemplo)**")
    l_c1, l_c2, l_c3, l_c4, l_c5, l_c6, l_c7 = st.columns(7)
    
    # Encabezados del Subcontenedor 1
    l_c1.write("**Col 1**")
    l_c2.write("**Col 2**")
    l_c3.write("**Col 3**")
    l_c4.write("**Col 4**")
    l_c5.write("**Col 5**")
    l_c6.write("**Col 6**")
    l_c7.write("**Col 7**")
    
    # Datos del Subcontenedor 1
    l_c1.write("Dato L1")
    l_c2.write("Dato L2")
    l_c3.write("Dato L3")
    l_c4.write("Dato L4")
    l_c5.write("Dato L5")
    l_c6.write("Dato L6")
    l_c7.button("Acción", key="btn_loc_1")
    
    st.write("") # Espacio en blanco para separar
    
    # --- Subcontenedor 2 (7 columnas) ---
    st.markdown("**Bloque 2: Proyección de Bases/Carreras (Ejemplo)**")
    l_d1, l_d2, l_d3, l_d4, l_d5, l_d6, l_d7 = st.columns(7)
    
    # Encabezados del Subcontenedor 2
    l_d1.write("**Col 1**")
    l_d2.write("**Col 2**")
    l_d3.write("**Col 3**")
    l_d4.write("**Col 4**")
    l_d5.write("**Col 5**")
    l_d6.write("**Col 6**")
    l_d7.write("**Col 7**")
    
    # Datos del Subcontenedor 2
    l_d1.write("Valor 1")
    l_d2.write("Valor 2")
    l_d3.write("Valor 3")
    l_d4.write("Valor 4")
    l_d5.write("Valor 5")
    l_d6.write("Valor 6")
    l_d7.button("Acción", key="btn_loc_2")

st.markdown("---") # Línea divisoria entre equipos

# ==============================================================================
# CONTENEDOR GENERAL: EQUIPO VISITANTE
# ==============================================================================
with st.container():
    # Nombre del equipo
    st.header("🔴 Equipo Visitante: Atlanta Braves")
    
    # --- Subcontenedor 1 (7 columnas) ---
    st.markdown("**Bloque 1: Estadísticas de Hits (Ejemplo)**")
    v_c1, v_c2, v_c3, v_c4, v_c5, v_c6, v_c7 = st.columns(7)
    
    # Encabezados del Subcontenedor 1
    v_c1.write("**Col 1**")
    v_c2.write("**Col 2**")
    v_c3.write("**Col 3**")
    v_c4.write("**Col 4**")
    v_c5.write("**Col 5**")
    v_c6.write("**Col 6**")
    v_c7.write("**Col 7**")
    
    # Datos del Subcontenedor 1
    v_c1.write("Dato V1")
    v_c2.write("Dato V2")
    v_c3.write("Dato V3")
    v_c4.write("Dato V4")
    v_c5.write("Dato V5")
    v_c6.write("Dato V6")
    v_c7.button("Acción", key="btn_vis_1")
    
    st.write("") # Espacio en blanco
    
    # --- Subcontenedor 2 (7 columnas) ---
    st.markdown("**Bloque 2: Proyección de Bases/Carreras (Ejemplo)**")
    v_d1, v_d2, v_d3, v_d4, v_d5, v_d6, v_d7 = st.columns(7)
    
    # Encabezados del Subcontenedor 2
    v_d1.write("**Col 1**")
    v_d2.write("**Col 2**")
    v_d3.write("**Col 3**")
    v_d4.write("**Col 4**")
    v_d5.write("**Col 5**")
    v_d6.write("**Col 6**")
    v_d7.write("**Col 7**")
    
    # Datos del Subcontenedor 2
    v_d1.write("Valor 1")
    v_d2.write("Valor 2")
    v_d3.write("Valor 3")
    v_d4.write("Valor 4")
    v_d5.write("Valor 5")
    v_d6.write("Valor 6")
    v_d7.button("Acción", key="btn_vis_2")
# ==========================================
# 3. CONTENEDORES DESPLEGABLES (EXPANDERS)
# ==========================================
st.subheader("🎯 Tarjetas de Jugadores (Ejemplo de su captura)")

# El texto que va dentro de los paréntesis de st.expander es lo que se ve ANTES de dar clic
with st.expander("Tommy White (Athletics) | batter_hits_alternate > 0.5 | Prob: 74.4%"):
    
    # Aquí definimos las columnas. Los números son proporciones de ancho.
    # Usamos 5 columnas para replicar los 5 bloques de su imagen.
    c1, c2, c3, c4, c5 = st.columns([1.5, 1.5, 1, 1, 1.2])
    
    # Llenado de la Columna 1
    with c1:
        st.write("Racha Reciente")
        st.subheader("1-0-2-0-4")
        
    # Llenado de la Columna 2
    with c2:
        st.write("Probabilidad Modelo")
        st.subheader("74.4%")
        
    # Llenado de la Columna 3
    with c3:
        st.write("Cuota Casino")
        st.subheader("1.43")
        
    # Llenado de la Columna 4
    with c4:
        st.write("Apuesta Kelly")
        st.subheader("$10.00")
        
    # Llenado de la Columna 5 (Botón)
    with c5:
        st.write("Retorno: $14.30")
        # El parámetro 'key' es obligatorio y debe ser único para cada botón en Streamlit
        st.button("Ejecutar Apuesta", key="btn_ejemplo_1")



# ==========================================
# 4. EJEMPLO EXTRA: ESTRUCTURA H2H 
# ==========================================
st.subheader("Ejemplo de Estructura H2H (Para sus ideas de 9 columnas)")

with st.expander("Previsualización de H2H (Equipos)"):
    # Creamos 9 columnas. La primera (Equipo) es doblemente ancha (2), el resto son normales (1)
    col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns([2, 1, 1, 1, 1, 1, 1, 1, 1])
    
    # Encabezados (Para cambiar los textos, simplemente edite lo que está entre comillas)
    col1.write("**Equipo Local**")
    col2.write("**Hits Hist.**")
    col3.write("**H-Hoy**")
    col4.write("**H-Momio**")
    col5.write("**Prob Real**")
    col6.write("**Momio**")
    col7.write("**EV Esp.**")
    col8.write("**Kelly**")
    col9.write("**Acción**")
    
    # Fila de datos ficticios
    col1.write("Washington Nationals")
    col2.write("7.8")
    col3.write("8.2")
    col4.write("7.5")
    col5.write("✅ 65%")
    col6.write("1.85")
    col7.write("+12%")
    col8.write("$25.00")
    col9.button("Apostar", key="btn_h2h_local")

# ==============================================================================
# CONTENEDOR GENERAL: EQUIPO LOCAL
# ==============================================================================
with st.container():
    # Nombre del equipo (Usamos st.header para que se vea grande)
    st.header("🔵 Equipo Local: Washington Nationals")
    
    # --- Subcontenedor 1 (7 columnas) ---
    st.markdown("**Bloque 1: Estadísticas de Hits (Ejemplo)**")
    l_c1, l_c2, l_c3, l_c4, l_c5, l_c6, l_c7 = st.columns(7)
    
    # Encabezados del Subcontenedor 1
    l_c1.write("**Col 1**")
    l_c2.write("**Col 2**")
    l_c3.write("**Col 3**")
    l_c4.write("**Col 4**")
    l_c5.write("**Col 5**")
    l_c6.write("**Col 6**")
    l_c7.write("**Col 7**")
    
    # Datos del Subcontenedor 1
    l_c1.write("Dato L1")
    l_c2.write("Dato L2")
    l_c3.write("Dato L3")
    l_c4.write("Dato L4")
    l_c5.write("Dato L5")
    l_c6.write("Dato L6")
    l_c7.button("Acción", key="btn_loc_1")
    
    st.write("") # Espacio en blanco para separar
    
    # --- Subcontenedor 2 (7 columnas) ---
    st.markdown("**Bloque 2: Proyección de Bases/Carreras (Ejemplo)**")
    l_d1, l_d2, l_d3, l_d4, l_d5, l_d6, l_d7 = st.columns(7)
    
    # Encabezados del Subcontenedor 2
    l_d1.write("**Col 1**")
    l_d2.write("**Col 2**")
    l_d3.write("**Col 3**")
    l_d4.write("**Col 4**")
    l_d5.write("**Col 5**")
    l_d6.write("**Col 6**")
    l_d7.write("**Col 7**")
    
    # Datos del Subcontenedor 2
    l_d1.write("Valor 1")
    l_d2.write("Valor 2")
    l_d3.write("Valor 3")
    l_d4.write("Valor 4")
    l_d5.write("Valor 5")
    l_d6.write("Valor 6")
    l_d7.button("Acción", key="btn_loc_2")

st.markdown("---") # Línea divisoria entre equipos

# ==============================================================================
# CONTENEDOR GENERAL: EQUIPO VISITANTE
# ==============================================================================
with st.container():
    # Nombre del equipo
    st.header("🔴 Equipo Visitante: Atlanta Braves")
    
    # --- Subcontenedor 1 (7 columnas) ---
    st.markdown("**Bloque 1: Estadísticas de Hits (Ejemplo)**")
    v_c1, v_c2, v_c3, v_c4, v_c5, v_c6, v_c7 = st.columns(7)
    
    # Encabezados del Subcontenedor 1
    v_c1.write("**Col 1**")
    v_c2.write("**Col 2**")
    v_c3.write("**Col 3**")
    v_c4.write("**Col 4**")
    v_c5.write("**Col 5**")
    v_c6.write("**Col 6**")
    v_c7.write("**Col 7**")
    
    # Datos del Subcontenedor 1
    v_c1.write("Dato V1")
    v_c2.write("Dato V2")
    v_c3.write("Dato V3")
    v_c4.write("Dato V4")
    v_c5.write("Dato V5")
    v_c6.write("Dato V6")
    v_c7.button("Acción", key="btn_vis_1")
    
    st.write("") # Espacio en blanco
    
    # --- Subcontenedor 2 (7 columnas) ---
    st.markdown("**Bloque 2: Proyección de Bases/Carreras (Ejemplo)**")
    v_d1, v_d2, v_d3, v_d4, v_d5, v_d6, v_d7 = st.columns(7)
    
    # Encabezados del Subcontenedor 2
    v_d1.write("**Col 1**")
    v_d2.write("**Col 2**")
    v_d3.write("**Col 3**")
    v_d4.write("**Col 4**")
    v_d5.write("**Col 5**")
    v_d6.write("**Col 6**")
    v_d7.write("**Col 7**")
    
    # Datos del Subcontenedor 2
    v_d1.write("Valor 1")
    v_d2.write("Valor 2")
    v_d3.write("Valor 3")
    v_d4.write("Valor 4")
    v_d5.write("Valor 5")
    v_d6.write("Valor 6")
    v_d7.button("Acción", key="btn_vis_2")

