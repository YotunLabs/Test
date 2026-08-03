import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Waals ERP - Cotizador", layout="centered", page_icon="🏭")

st.title("⚡ Centro de Cotizaciones Rápido")
st.write("Generador de precios basado en reglas de manufactura.")

# 1. ZONA DE SELECCIÓN (El embudo)
with st.container(border=True):
    st.subheader("1. Parámetros del Pedido")
    
    col1, col2 = st.columns(2)
    with col1:
        # Aquí luego conectaremos MySQL, por ahora es una lista estática
        familia = st.selectbox("Familia Operativa", ["Sublimación Cilíndricos", "Bordado Plano", "DTF Textil Plano"])
    
    with col2:
        # Lógica simulada: Si elige Cilíndricos, solo muestra Tazas y Termos
        if familia == "Sublimación Cilíndricos":
            producto = st.selectbox("Producto Objetivo", ["Taza Clásica Blanca 11oz", "Termo 30oz Acero", "Taza Mágica"])
        elif familia == "Bordado Plano":
            producto = st.selectbox("Producto Objetivo", ["Parche Pro (Lote 15)", "Sudadera Ejecutiva Bordada"])
        else:
            producto = st.selectbox("Producto Objetivo", ["Playera Blanca Esencial (Logo 12x12)"])

    cantidad = st.number_input("Cantidad de piezas (Volumen)", min_value=1, value=10, step=1)

# 2. ZONA DE DESGLOSE TÉCNICO (El ADN del producto)
# Simulamos los costos que extrajimos de tus reglas de "Cascarón y Fracción"
costo_cascaron = 45.00 # Costo ficticio de una taza mágica virgen
costo_formato = 8.20 * 0.25 # Costo de la hoja A4 dividido en 4 tazas
costo_operativo_total = (costo_cascaron + costo_formato) * cantidad

with st.container(border=True):
    st.subheader("2. Estructura de Costos (BOM)")
    
    st.markdown(f"**Análisis unitario para: {producto}**")
    
    # Usamos columnas pequeñas para los datos crudos
    c1, c2, c3 = st.columns(3)
    c1.metric("Costo Cascarón (Virgen)", f"${costo_cascaron:,.2f}")
    c2.metric("Fracción Insumo (Formato)", f"${costo_formato:,.2f}")
    c3.metric("Costo Unitario Real", f"${(costo_cascaron + costo_formato):,.2f}")
    
    st.info(f"Costo de Producción por lote de {cantidad} piezas: **${costo_operativo_total:,.2f} MXN**")

# 3. ZONA DE RENTABILIDAD Y CIERRE
with st.container(border=True):
    st.subheader("3. Proyección Comercial")
    
    # Aquí puedes jugar con el precio de venta sugerido
    precio_venta_unitario = st.number_input("Precio de Venta Sugerido (Unitario)", min_value=0.0, value=120.00)
    ingreso_bruto = precio_venta_unitario * cantidad
    utilidad_neta = ingreso_bruto - costo_operativo_total
    margen = (utilidad_neta / ingreso_bruto) * 100 if ingreso_bruto > 0 else 0
    
    st.divider()
    
    # Resultados finales con colores de alerta
    r1, r2, r3 = st.columns(3)
    r1.metric("Ingreso Cobrado (Bruto)", f"${ingreso_bruto:,.2f}")
    r2.metric("Utilidad (Libre)", f"${utilidad_neta:,.2f}", f"{margen:.1f}% Margen")
    
    if margen < 30:
        st.error("⚠️ Alerta de Margen: Por debajo del 30% operativo.")
    else:
        st.success("✅ Margen saludable. Listo para aprobar.")
        
    st.button("Generar PDF y Enviar a WhatsApp", type="primary", use_container_width=True)

st.title("Gestión de Proyectos")

# Creamos un contenedor con borde para aislar el proyecto
with st.container(border=True):
    st.subheader("Lote 100 Parches Scouts")
    
    # Metemos columnas DENTRO del contenedor para organizar la data
    col1, col2 = st.columns(2)
    with col1:
        st.write("🏭 **Estatus:** En bordadora")
        st.write("📅 **Entrega:** 20 de Junio")
    with col2:
        st.write("👤 **Responsable:** Gabriela")
        st.write("💰 **Anticipo:** Pagado")
        
    st.progress(75, text="Avance de producción")
    st.button("Marcar como terminado", key="btn_parches")

# Configuración de la página (Ancho completo para el ERP)
st.set_page_config(page_title="Waals ERP", layout="wide", page_icon="🏭")

# --- MENÚ LATERAL ---
st.sidebar.title("Estudio Waals")
menu = st.sidebar.radio(
    "Navegación",
    ["📊 Inicio", "🛠️ Producción", "🤝 CRM y Ventas", "💰 Finanzas"]
)

# --- PESTAÑA: INICIO ---
if menu == "📊 Inicio":
    st.title("Panel de Control Principal")
    st.write("Resumen operativo del día.")
    
    # Métricas rápidas
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Proyectos Activos", "12", "+2 desde ayer")
    col2.metric("Cotizaciones Pendientes", "5", "-1 (Cerrada)")
    col3.metric("Ingreso Semanal", "$18,500 MXN", "15% vs meta")
    col4.metric("Nivel DTF UV", "3.5 Metros", "-0.5m (Alerta baja)", delta_color="inverse")
    
    st.divider()
    
    # Progreso de Proyectos
    st.subheader("Proyectos de la Semana")
    st.write("Lote 100 Parches Sublimados (Scouts) - Entrega Jueves")
    st.progress(75, text="En proceso: Corte láser final")
    
    st.write("Sudaderas Full Print (Cliente Corporativo) - Entrega Viernes")
    st.progress(40, text="En proceso: Plancha plana")
    
    st.write("Grabado Termos 30oz - Entrega Hoy")
    st.progress(90, text="En proceso: Empaque y limpieza")

# --- PESTAÑA: CRM Y VENTAS ---
elif menu == "🤝 CRM y Ventas":
    st.title("Seguimiento de Cotizaciones")
    
    # Tabla simulada de estado de clientes
    data = {
        "Cliente": ["Grupo Scout 201", "Empresa XYZ", "Gabriela M.", "Carlos V.", "Evento Social"],
        "Monto": ["$4,500", "$12,000", "$850", "$3,200", "$6,000"],
        "Estado": ["🔴 Sin Respuesta", "🟡 Anticipo Pendiente", "🟢 Pagado", "🟡 Anticipo Pendiente", "🔴 Sin Respuesta"],
        "Último Contacto": ["Hace 2 días", "Hace 4 horas", "Hace 1 día", "Hoy", "Hace 5 días"]
    }
    df = pd.DataFrame(data)
    
    # Mostrar la tabla interactiva
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.button("Recordatorio Automático: Enviar WhatsApp a 'Sin Respuesta'")

# --- PESTAÑA: PRODUCCIÓN ---
elif menu == "🛠️ Producción":
    st.title("Piso de Manufactura")
    st.write("Gestión de máquinas y tareas internas.")
    
    # Kanban básico visual
    col_pend, col_proc, col_listo = st.columns(3)
    
    with col_pend:
        st.error("🔴 Pendiente (Pre-producción)")
        st.info("Preparar bastidores 12x12")
        st.info("Revisar arte tipografía cursiva")
        
    with col_proc:
        st.warning("🟡 En Máquina")
        st.info("Bordadora: Parches (Lote 2/5)")
        
    with col_listo:
        st.success("🟢 Terminado (A Empaque)")
        st.info("Tazas mágicas (15 piezas)")

# --- PESTAÑA: FINANZAS ---
elif menu == "💰 Finanzas":
    st.title("Control de Flujo (Caja Fuerte)")
    
    # Gráfica simulada de ingresos vs egresos
    st.subheader("Balance Mensual")
    chart_data = pd.DataFrame(
        np.random.randn(20, 2) * 1500 + 5000,
        columns=["Ingresos", "Egresos Material"]
    )
    st.line_chart(chart_data)
    
    st.subheader("Registro de Operaciones")
    st.write("Aquí se registrarán las entradas de efectivo, pago de hosting/Airtable/materiales, y el cruce contra el costo de las recetas.")
