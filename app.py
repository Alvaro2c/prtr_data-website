import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("""PRTR Data""")

tab1, tab2 = st.tabs(["PRTR Data", "Más información"])

with tab1:

    components.iframe('https://lookerstudio.google.com/embed/reporting/9fcfa666-8498-4cf2-b7ac-f0fd14a2e762/page/TwupD',
                      height=640, scrolling=True)

with tab2:
    st.title("Acerca del proyecto")
    st.markdown("""
    <div style="text-align: justify;">
    <b>PRTR Data</b> es un proyecto personal de visualización de datos relativos a las licitaciones financiadas por el Mecanismo de Recuperación y Resiliencia (MRR) de la Unión Europea en España, en el marco del Plan de Recuperación, Transformación y Resiliencia (PRTR) del Gobierno de España.
    <br></br>
    Los datos utilizados para realizar este proyecto han sido obtenidos de la base de datos publicada en el <a href="https://planderecuperacion.gob.es/como-acceder-a-los-fondos/convocatorias" target="_blank">sitio</a> de información oficial del Gobierno.
    <br></br>
    El dashboard será actualizado con regularidad. Para una mejor visualización utilice la opción "Pantalla completa" (esquina inferior izquierda del dashboard).
    <br></br>
    <b>Para cualquier consulta, solicitud o sugerencia relativa a este proyecto, puede hacer llegar un correo electrónico a la siguiente dirección: <a href="mailto:prtrdata@gmail.com">prtrdata@gmail.com</a>.</b>
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.markdown("**Un proyecto realizado por: [Alvaro Carranza](https://alvaro2c.github.io/about)**")
