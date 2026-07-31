import streamlit as st

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