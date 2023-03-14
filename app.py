#--------------------LIBRERÍAS----------------------------#
import streamlit as st 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import plotly_express as px
import plotly.graph_objects as go


#--------------------CONFIGURACIÓN DE LA PÁGINA----------------------------#
#layout="centered" or "wide"
st.set_page_config(page_title="Mi primera APP", layout="wide", page_icon="👋")
st.set_option('deprecation.showPyplotGlobalUse', False)

#--------------------LOGO+CREACIÓN DE COLUMNA----------------------------#
col1,col2,col3 = st.columns(3)
with col1:
    st.title("")
with col2:
    st.image("img/logo.png", width=300)
with col3:
    st.title("")

#--------------------COSAS QUE VAMOS A USAR EN TODA LA APP----------------------------#
df0 = pd.read_csv(r"data/netflixprocesado.csv")
if "Unnamed: 0" in df0:
    df = df0.drop(columns = ['Unnamed: 0']) 
else:
    pass

def genere_selec(genero_select):
    if genero_select:
        return df.loc[df0['Tipo'] == genero_select]
    else:
        return ""

#--------------------TITLE----------------------------#
st.title("Mi primera APP")

#--------------------SIDEBAR----------------------------#
st.sidebar.image("img/logo.png", width=150)
st.sidebar.title("MENÚ")
st.sidebar.subheader("Filtros para utilizar en la tabla")
st.sidebar.write("")

#--------------------SIDEBAR FILTRO1----------------------------#
#creo una variable con el filtro
filtro_pais = st.sidebar.selectbox("País", df0['País'].unique())
#mostramos los cambios del filtro
if filtro_pais:
    df1=df.loc[df0['País'] == filtro_pais]
    
#--------------------SIDEBAR FILTRO2----------------------------#
filtro_genero = st.sidebar.selectbox('Género', df0['Tipo'].unique())
if filtro_genero:
    df1 = df.loc[df0['Tipo'] == filtro_genero]

#-------------------DIBUJAR UN SOLO DATAFRAME CON AMBOS FILTROS APLICADOS--------------------------------#
#mostramos los cambios del filtro
if filtro_pais and filtro_genero:
    df2 = df.loc[(df0['País'] == filtro_pais) & (df0['Tipo'] == filtro_genero)]
    
#Visualizamos el dataframe
st.dataframe(df2)


#--------------------GRÁFICA1 ENRIQUE----------------------------#
st.title("Mis primeros gráficos")
#centramos title con html 
st.markdown("<center><h2><l style='color:white; font-size: 30px;'>Mis primeros gráficos ( título2 )</h2></center>", unsafe_allow_html=True)


col1,col2,col3 = st.columns(3)
with col1:
    top10_paises = df0['País'].value_counts().head(10).to_frame()
    grafica_enr = px.bar(top10_paises, x=top10_paises.index, y='País',template="plotly_dark", width=400, height=400)
    st.plotly_chart(grafica_enr)

with col2:
    cristian = px.scatter(df, 'Fecha_de_estreno', 'País', title='grafica')
    st.plotly_chart(cristian)

with col3:
    country_count = df0['País'].value_counts()
    fig = px.pie(country_count.head(10), values='País', names=country_count.head(10).index, title='Top 10 países con más estrenos en Netflix')
    st.plotly_chart(fig)


#--------------------SECCION DE PESTAÑAS----------------------------#
tab1, tab2, tab3, tab4, tab5 = st.tabs (["Enrique","Guillermo","Pilar","Pedro","Borja"])

with tab1:
    st.header("Enrique")
    proporcion = df0["Tipo"].value_counts()
    fig = go.Figure(
        data=[
            go.Pie(
                labels=(proporcion / len(df0 * 100)).index,
                values=(proporcion / len(df0 * 100)).values,
                text=proporcion.index,
            )
        ]
    )
    fig.update_layout(title="TV Show vs Movie", template="plotly_dark")
    st.plotly_chart(fig)

with tab2:
    st.header("Guillermo")
    guille = px.histogram(df0, x="Puntuación", template="plotly_dark", color="Tipo", title="Histograma de Calidad de Vinos")
    st.plotly_chart(guille)
with tab3:
    st.header("Pilar")
with tab4:
    st.header("Pedro")
with tab5:
    st.header("Borja")
    borja = px.scatter(df, x='País', y='Puntuación')
    st.plotly_chart(borja)
