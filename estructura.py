import streamlit as st
import pandas as pd
import numpy as np

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
