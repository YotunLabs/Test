# ==============================================================================
# MÓDULO 1: CONFIGURACIÓN Y CONEXIÓN
# ==============================================================================
import streamlit as st
import mysql.connector
import pandas as pd

st.set_page_config(page_title="Motor MLB - PRO v2.0", layout="wide", initial_sidebar_state="expanded")

# --- FUNCIONES MATEMÁTICAS Y DE CONVERSIÓN ---
def calcular_kelly(prob, cuota_decimal, capital):
    b = cuota_decimal - 1.0
    if b <= 0: return 10.0
    q = 1.0 - prob
    kelly_puro = (prob * b - q) / b
    stake_sugerido = capital * kelly_puro * 0.25 
    return max(round(stake_sugerido, 2), 10.0) if stake_sugerido > 0 else 0.0

def americano_a_decimal(americano):
    """Convierte momio americano (+350 o -120) a cuota decimal."""
    if americano == 0: return 0
    if americano > 0:
        return (americano / 100) + 1
    else:
        return (100 / abs(americano)) + 1

# ==============================================================================
# MÓDULO 2: SIDEBAR - FINANZAS Y TELEMETRÍA OPERATIVA
# ==============================================================================
st.sidebar.title("⚙️ Panel Operativo")

menu = st.sidebar.radio("Navegación:", ["En Vivo (Partidos)", "Parlays (SGP)", "Inicio (Top EV)", "Historial", "Bankroll", "Telemetría (Logs)"])
st.sidebar.markdown("---")

# 1. Gestión Multicartera (Simulada para visualización; luego se enlazará a BD)
st.sidebar.subheader("💼 Carteras de Inversión")
c_playdoit = st.sidebar.number_input("Playdoit (MXN)", value=5000.00, step=100.0)
c_winpot = st.sidebar.number_input("Winpot (MXN)", value=4250.00, step=100.0)
c_caliente = st.sidebar.number_input("Caliente (MXN)", value=6200.00, step=100.0)
c_otro = st.sidebar.number_input("Otro (MXN)", value=0.00, step=100.0)

capital_neto = c_playdoit + c_winpot + c_caliente + c_otro
st.sidebar.metric("Capital Neto Total", f"${capital_neto:,.2f} MXN")

st.sidebar.markdown("---")

# 2. Cascada de Metas Operativas (Costos Fijos vs Utilidad)
st.sidebar.subheader("📈 Meta Mensual y Costos Fijos")

# Supongamos que llevamos ganados $1,500 en el mes para el ejemplo visual
ganancia_mensual = 1500.0  

costo_vps = 300
costo_api = 600
gastos_extra = 400
meta_utilidad = 5000
total_meta = costo_vps + costo_api + gastos_extra + meta_utilidad

progreso = min(ganancia_mensual / total_meta, 1.0)
st.sidebar.progress(progreso, text=f"Progreso Total: ${ganancia_mensual:,.0f} / ${total_meta:,.0f}")

# Desglose en cascada
st.sidebar.caption(f"🖥️ VPS ($300): {'✅ Cubierto' if ganancia_mensual >= costo_vps else '⏳ Pendiente'}")
st.sidebar.caption(f"📡 API ($600): {'✅ Cubierto' if ganancia_mensual >= (costo_vps + costo_api) else '⏳ Pendiente'}")
st.sidebar.caption(f"☕ Extras ($400): {'✅ Cubierto' if ganancia_mensual >= (costo_vps + costo_api + gastos_extra) else '⏳ Pendiente'}")
utilidad_real = max(0, ganancia_mensual - (costo_vps + costo_api + gastos_extra))
st.sidebar.caption(f"💰 Utilidad Neta: ${utilidad_real:,.0f} / ${meta_utilidad:,.0f}")

# ==============================================================================
# PESTAÑA: EN VIVO (TABLERO Y TABS DE JUGADORES)
# ==============================================================================
if menu == "En Vivo (Partidos)":
    st.title("📊 Terminal de Partidos")
    st.write("Análisis algorítmico y ejecución rápida de órdenes.")
    st.markdown("---") 

    # Simulación del filtro principal de partido
    partido_sel = st.selectbox("Filtro Maestro - Seleccione un Partido:", [
        "Washington Nationals (L) vs Atlanta Braves (V)", 
        "Chicago Cubs (L) vs St. Louis Cardinals (V)"
    ])
    st.markdown("---")

    # Contenedores de Proyección Colectiva (Simulados hasta integrar la extracción del motor V2)
    with st.container():
        st.subheader("🔵 Washington Nationals - Local | ✅ Prob: 65%") 
        st.markdown("**🎯 Proyección Ofensiva Colectiva**")
        loc1, loc2, loc3, loc4, loc5, loc6 = st.columns([1.5, 1, 1, 1, 1, 1])
        loc1.write("**Mercado**"); loc2.write("**Racha Eq.**"); loc3.write("**Línea**"); loc4.write("**Momio**"); loc5.write("**Px Real**"); loc6.write("**EV**")
        loc1.write("Total de Hits"); loc2.write("9-7-12-5-8"); loc3.write("+8.5"); loc4.write("-110"); loc5.write("55%"); loc6.write("✅ +4.5%")
        loc1.write("Total Carreras"); loc2.write("4-3-6-2-5"); loc3.write("+4.5"); loc4.write("120"); loc5.write("45%"); loc6.write("❌ -2.1%")
    
    st.markdown("---")
    
    with st.container():
        st.subheader("🔴 Atlanta Braves - Visitante | ❌ Prob: 35%") 
        st.markdown("**🎯 Proyección Ofensiva Colectiva**")
        vis1, vis2, vis3, vis4, vis5, vis6 = st.columns([1.5, 1, 1, 1, 1, 1])
        vis1.write("**Mercado**"); vis2.write("**Racha Eq.**"); vis3.write("**Línea**"); vis4.write("**Momio**"); vis5.write("**Px Real**"); vis6.write("**EV**")
        vis1.write("Total de Hits"); vis2.write("5-4-6-4-5"); vis3.write("+7.5"); vis4.write("-115"); vis5.write("52%"); vis6.write("✅ +1.2%")
        vis1.write("Total Carreras"); vis2.write("2-1-4-1-3"); vis3.write("+3.5"); vis4.write("-105"); vis5.write("48%"); vis6.write("❌ -3.4%")

    st.markdown("---")

    # ----------------------------------------------------------------------
    # TABS: MESA DE EJECUCIÓN POR MERCADOS
    # ----------------------------------------------------------------------
    st.header("🎯 Radar de Jugadores (Filtrado)")
    
    tab_hits, tab_bases, tab_hr = st.tabs(["⚾ 1. HITS", "🏃 2. BASES TOTALES", "🚀 3. HOME RUNS"])

    # Función para renderizar encabezados de tabla
    def renderizar_encabezados(mostrar_input_manual=False):
        if mostrar_input_manual:
            c1, c2, c3, c4, c5, c6, c7 = st.columns([2, 1.5, 1, 1, 1, 1, 1.5])
            c1.write("**Jugador (Equipo)**")
            c2.write("**Ingreso Momio (Américo)**")
            c3.write("**Nueva Px**")
            c4.write("**Nuevo EV**")
            c5.write("**Sug. Kelly**")
            c6.write("**Retorno**")
            c7.write("**Ejecutar Orden**")
            return c1, c2, c3, c4, c5, c6, c7
        else:
            c1, c2, c3, c4, c5, c6, c7, c8, c9 = st.columns([1.5, 1, 1, 1, 1, 1, 1, 1, 1])
            c1.write("**Jugador**"); c2.write("**EV**"); c3.write("**Px**"); c4.write("**Racha**")
            c5.write("**Momio**"); c6.write("**Sug. Kelly**"); c7.write("**Playdoit**"); c8.write("**Winpot**"); c9.write("**Caliente**")
            return c1, c2, c3, c4, c5, c6, c7, c8, c9

    # TAB 1: HITS (Estructura de tabla con botones multicartera)
    with tab_hits:
        c1, c2, c3, c4, c5, c6, c7, c8, c9 = renderizar_encabezados()
        st.markdown("---")
        
        # Fila simulada de jugador 1
        c1.write("Tommy White")
        c2.write("✅ 12.5%")
        c3.write("74.4%")
        c4.write("1-0-2-0-4")
        c5.write("1.43")
        c6.write("$125.00")
        c7.button("PD $", key="pd_h1", help="Apostar con Playdoit")
        c8.button("WP $", key="wp_h1", help="Apostar con Winpot")
        c9.button("CA $", key="ca_h1", help="Apostar con Caliente")
        
        # Fila simulada de jugador 2
        st.write("") # Espaciador
        c1.write("CJ Abrams")
        c2.write("❌ -2.1%")
        c3.write("48.4%")
        c4.write("0-0-1-0-1")
        c5.write("1.85")
        c6.write("$0.00")
        c7.button("PD $", key="pd_h2", disabled=True)
        c8.button("WP $", key="wp_h2", disabled=True)
        c9.button("CA $", key="ca_h2", disabled=True)

    # TAB 2: BASES TOTALES
    with tab_bases:
        c1, c2, c3, c4, c5, c6, c7, c8, c9 = renderizar_encabezados()
        st.markdown("---")
        
        # Fila simulada
        c1.write("Lane Thomas")
        c2.write("✅ 8.4%")
        c3.write("55.0%")
        c4.write("2-1-3-0-2")
        c5.write("1.85")
        c6.write("$210.00")
        c7.button("PD $", key="pd_b1")
        c8.button("WP $", key="wp_b1")
        c9.button("CA $", key="ca_b1")

    # TAB 3: HOME RUNS (INYECCIÓN MANUAL Y CÁLCULO EN RAM)
    with tab_hr:
        st.info("Líneas de Home Runs no publicadas. Ingrese el momio americano (ej. +350) para ejecutar el modelo híbrido 60/40 en tiempo real.")
        c1, c2, c3, c4, c5, c6, c7 = renderizar_encabezados(mostrar_input_manual=True)
        st.markdown("---")
        
        # Datos base puros del modelo matemático (El 60% que ya calculó el motor)
        jugador_hr = "Marcell Ozuna (ATL)"
        px_modelo_puro = 0.285  # 28.5% probabilidad matemática cruda
        
        c1.write(f"{jugador_hr}\n\n*(Px Base: {px_modelo_puro*100:.1f}%)*")
        
        # Ingreso manual del usuario
        momio_manual = c2.number_input("Momio Americano:", value=0, step=50, key="in_hr_ozuna")
        
        if momio_manual != 0:
            # 1. Convertir momio a decimal y sacar la prob del casino (El 40%)
            cuota_dec = americano_a_decimal(momio_manual)
            prob_casino = 1.0 / cuota_dec if cuota_dec > 0 else 0
            
            # 2. Mezcla Híbrida
            nueva_px = (px_modelo_puro * 0.60) + (prob_casino * 0.40)
            
            # 3. Nuevo EV y Kelly
            nuevo_ev = (nueva_px * cuota_dec) - 1.0
            nuevo_kelly = calcular_kelly(nueva_px, cuota_dec, capital_neto)
            retorno_potencial = nuevo_kelly * cuota_dec
            
            color_ev = "green" if nuevo_ev > 0 else "red"
            icono_ev = "✅" if nuevo_ev > 0 else "❌"
            
            # Impresión de resultados dinámicos
            c3.markdown(f"**{nueva_px*100:.1f}%**")
            c4.markdown(f"<span style='color:{color_ev}'>{icono_ev} {nuevo_ev*100:+.1f}%</span>", unsafe_allow_html=True)
            c5.write(f"${nuevo_kelly:,.2f}")
            c6.write(f"${retorno_potencial:,.2f}")
            
            # Botones de ejecución
            with c7:
                if nuevo_ev > 0:
                    st.button("Caliente", key="btn_hr_cal")
                    st.button("Winpot", key="btn_hr_win")
                else:
                    st.button("Descartado", disabled=True, key="btn_hr_fail")
        else:
            c3.write("--")
            c4.write("--")
            c5.write("--")
            c6.write("--")
            c7.write("Esperando momio...")
