import streamlit as st
from modelo import resolver_citi

st.set_page_config(page_title='Citi CR', page_icon='💼', layout='wide')
st.title('💼 Citi Costa Rica — Optimizador de Analistas')
st.write('Minimiza el tiempo de ciclo de operaciones bancarias.')

# Parametros ajustables
st.sidebar.header('⚙️ Parametros')
analistas = st.sidebar.slider('Analistas disponibles', 5, 20, 12)
min_s     = st.sidebar.slider('Minimo SWIFT', 1, 8, 4)
min_c     = st.sidebar.slider('Minimo Cartas de Credito', 1, 5, 2)
cap       = st.sidebar.slider('Capacidad minima total', 10, 25, 15)

if st.button('🚀 Optimizar ahora'):
    x1, x2, x3, z = resolver_citi(analistas, min_s, min_c, cap)
    st.success(f'✅ Costo minimo: Z* = {z:.0f} horas de ciclo')
    c1, c2, c3 = st.columns(3)
    c1.metric('🔵 Analistas SWIFT',           int(x1))
    c2.metric('🟠 Analistas Cartas Credito',  int(x2))
    c3.metric('🟢 Analistas Garantias',       int(x3))
    st.bar_chart({'SWIFT': x1, 'Cartas': x2, 'Garantias': x3})
    st.markdown(f"""
    **Interpretacion:**
    La solucion optima asigna **{int(x1)} analistas a SWIFT**, **{int(x2)} a Cartas de Credito**
    y **{int(x3)} a Garantias**, con un costo de ciclo minimo de **{z:.0f} horas**.
    """)
