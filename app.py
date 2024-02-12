import os
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="PRTR Data", page_icon="https://i.ibb.co/jDLksmH/prtr-icon.jpg", layout="wide")

logo_path = "https://i.ibb.co/5YX367y/prtr-logo.jpg"
map_gif = "https://s13.gifyu.com/images/SCoJO.gif"
bar_gif = "https://s13.gifyu.com/images/SCoJy.gif"
tab_gif = "https://s13.gifyu.com/images/SCoP2.gif"
sea_gif = "https://s13.gifyu.com/images/SCoPK.gif"
logo_python = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png"
logo_bigquery = "https://cdn.icon-icons.com/icons2/2699/PNG/512/google_bigquery_logo_icon_168150.png"
logo_lookerstudio = "https://seeklogo.com/images/G/google-looker-logo-B27BD25E4E-seeklogo.com.png"
logo_airflow = "https://static-00.iconduck.com/assets.00/airflow-icon-2048x2048-ptyvisqh.png"
logo_streamlit = "https://camo.githubusercontent.com/e7a254c6bc8cad40ef6316da7318414671df3cadb21320c929bd5492511db8ad/68747470733a2f2f696d6167652e706e676161612e636f6d2f3739382f353038343739382d6d6964646c652e706e67"

st.image(logo_path,width=400)

tab1, tab2 = st.tabs(["PRTR Data", "Más información"])

with tab1:

    components.iframe('https://lookerstudio.google.com/embed/reporting/9fcfa666-8498-4cf2-b7ac-f0fd14a2e762/page/TwupD',
                      height=2000, scrolling=True)

with tab2:
    st.title("Acerca del proyecto")
    st.markdown("""
    <div style="text-align: justify;">
    <b>PRTR Data</b> es un proyecto personal de visualización de datos relativos a las licitaciones financiadas por el Mecanismo de Recuperación y Resiliencia (MRR) de la Unión Europea en España, en el marco del Plan de Recuperación, Transformación y Resiliencia (PRTR) del Gobierno de España.
    <br></br>
    Los datos utilizados para realizar este proyecto han sido obtenidos de la base de datos publicada en el <a href="https://planderecuperacion.gob.es/como-acceder-a-los-fondos/convocatorias" target="_blank">sitio</a> de información oficial del Gobierno.
    </div>
    """, unsafe_allow_html=True)

    st.title("¿Cómo funciona?")
    st.markdown("""
    <div style="text-align: justify;">
    <b>PRTR Data</b> está dividido en tres pestañas (o reportes) diferentes, según el estado de las licitaciones visualizadas: cerradas, abiertas o próximas licitaciones.
    <br></br>
    En cada pestaña se pueden acceder a los siguientes datos:\n
    - <b>Total de licitaciones:</b> Por defecto, indica el número total de licitaciones en dicha pestaña / en dicho estado (abierta, cerrada o próxima). Se actualiza según los filtros aplicados en los gráficos o en el buscador.
    - <b>Importe total (€):</b> Por defecto, indica el importe total en euros que suman las licitaciones en dicha pestaña / en dicho estado (abierta, cerrada o próxima). Se actualiza según los filtros aplicados en los gráficos o en el buscador.
    - <b>Importe promedio (€):</b> Por defecto, indica el importe promedio en euros de las licitaciones en dicha pestaña / en dicho estado (abierta, cerrada o próxima). Se actualiza según los filtros aplicados en los gráficos o en el buscador.\n
    A los siguientes gráficos:
    - <b>Licitaciones por región (mapa):</b> Por defecto, es un mapa en el que se visualiza la cantidad de licitaciones (en % sobre el total) por región (se puede cambiar de métrica a "Importe total en €" en la esquina superior derecha del mapa). Es posible hacer click en una región para filtrar únicamente las licitaciones de dicha región en la totalidad del reporte. Finalmente, también se actualiza según los filtros aplicados en los otros gráficos o en el buscador.
        </div>
    """, unsafe_allow_html=True)

    left_map, cent_map, right_map = st.columns(3)
    with cent_map:
        st.image(map_gif, width=600)

    st.markdown("""
    <div style="text-align: justify;">
    \n- <b>Tipos de procedimientos (barras horizontales):</b> Por defecto, es un gráfico de barras horizontales en el que se visualiza los tipos de procedimientos en que se han gestionado las licitaciones (en % sobre el total: se puede cambiar de métrica a "Importe total en €" en la esquina superior derecha del gráfico). Es posible hacer click en una barra horizontal para filtrar únicamente las licitaciones de dicho tipo de procedimiento en la totalidad del reporte. Finalmente, también se actualiza según los filtros aplicados en los otros gráficos o en el buscador.
    <br></br>
    </div>
    """, unsafe_allow_html=True)

    left_bar, cent_bar, right_bar = st.columns(3)
    with cent_bar:
        st.image(bar_gif, width=600)

    st.markdown("""
    <div style="text-align: justify;">
    \n- <b>Top 10 licitaciones por importe (tabla):</b> Por defecto, es una tabla en la que se muestran las 10 primeras licitaciones con mayor importe total en euros). Se actualiza según los filtros aplicados en los gráficos o en el buscador.
    <br></br>
    </div>
    """, unsafe_allow_html=True)

    left_tab, cent_tab, right_tab = st.columns(3)
    with cent_tab:
        st.image(tab_gif, width=600)

    st.markdown("""
    <div style="text-align: justify;">
    Y a un buscador: El buscador por "Órgano convocante" (en la esquina superior derecha del reporte) permite igualmente aplicar un filtro general seleccionando un órgano convocante en particular. A tomar en cuenta que varios nombres de órganos convocantes pueden referir al mismo órgano, según la nomenclatura indicada en la información de la licitación.
    </div>
    <br></br>
    """, unsafe_allow_html=True)

    left_sea, cent_sea, right_sea = st.columns(3)
    with cent_sea:
        st.image(sea_gif, width=600)

    st.markdown("""
    <div style="text-align: justify;">
    Para una mejor visualización puede utilizar la opción "Pantalla completa" (esquina inferior izquierda del reporte).
    </div>
    """, unsafe_allow_html=True)

    st.title("Tech stack")
    st.markdown("""
    <div style="text-align: justify;">
    Para realizar este proyecto, se utilizaron las siguientes tecnologías:
    <br></br>
    </div>
    """, unsafe_allow_html=True)

    st.image(logo_python, width=100)
    st.markdown("""
    <div style="text-align: justify;">
    Python: para el scripting a cargo del scraping y la limpieza de los datos.
    <br></br>
    </div>
    """, unsafe_allow_html=True)

    st.image(logo_bigquery, width=100)
    st.markdown("""
    <div style="text-align: justify;">
    BigQuery: para el almacenamiento de dichos datos en tablas SQL en la nuble (Google Cloud Platform).
    <br></br>
    </div>
    """, unsafe_allow_html=True)

    st.image(logo_lookerstudio, width=100)
    st.markdown("""
    <div style="text-align: justify;">
    Looker Studio: para la visualización en reportes, conectado directamente a los datos almacenados en BigQuery.
    <br></br>
    </div>
    """, unsafe_allow_html=True)

    st.image(logo_airflow, width=100)
    st.markdown("""
    <div style="text-align: justify;">
    Airflow: para la orquestación y automatización de flujos de datos para las futuras actualizaciones.
    <br></br>
    </div>
    """, unsafe_allow_html=True)

    st.image(logo_streamlit, width=100)
    st.markdown("""
    <div style="text-align: justify;">
    Streamlit: para el frontend del sitio web.
    <br></br>
    </div>
    """, unsafe_allow_html=True)

    st.title("Contacto")
    st.markdown("""
    <div style="text-align: justify;">
    <b>Para cualquier consulta, solicitud o sugerencia relativa a este proyecto, puede hacer llegar un correo electrónico a la siguiente dirección: <a href="mailto:prtrdata@gmail.com">prtrdata@gmail.com</a>.</b>
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.markdown("**Un proyecto realizado por: [Alvaro Carranza](https://alvaro2c.github.io/about)**")
