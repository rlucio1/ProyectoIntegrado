import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
from urllib.error import URLError

@st.cache
def get_UN_data():
AWS_BUCKET_URL = 'C:/ProyectoIntegrador'


df15 = pd.read_csv(AWS_BUCKET_URL +'/VacanteAnalistaDeDatos.csv')
df1 = pd.read_csv(AWS_BUCKET_URL +'/Vacantes_Tester.csv', encoding='latin-1')
df2 = pd.read_csv(AWS_BUCKET_URL +'/Vacantes_GerenteTI.csv',encoding='latin-1')
df3 = pd.read_csv(AWS_BUCKET_URL +'/Vacantes_Fullstack.csv',encoding='latin-1')
df4 = pd.read_csv(AWS_BUCKET_URL + '/Vacantes_DesarrolladorWeb.csv',encoding='latin-1')
df5 = pd.read_csv(AWS_BUCKET_URL +'/Vacantes_DesarrolladorSoftware.csv',encoding='latin-1')
df6 = pd.read_csv(AWS_BUCKET_URL + '/Vacantes_CientificoDatos.csv',encoding='latin-1')
df7 = pd.read_csv(AWS_BUCKET_URL +'/Vacantes_Ciberseguridad.csv',encoding='latin-1')
df8 = pd.read_csv(AWS_BUCKET_URL + '/Vacantes_AdministradorBD.csv',encoding='latin-1')
df9 = pd.read_csv(AWS_BUCKET_URL + '/VacanteProgramadorPHP.csv',encoding='latin-1')
df10 = pd.read_csv(AWS_BUCKET_URL + '/VacantedesarrolladorNET.csv',encoding='latin-1')
df11 = pd.read_csv(AWS_BUCKET_URL + '/VacanteDesarrolladorMoviles.csv',encoding='latin-1')
df12= pd.read_csv(AWS_BUCKET_URL + '/VacanteDesarrolladorJr.csv',encoding='latin-1')
df13 = pd.read_csv(AWS_BUCKET_URL + '/VacanteArquitectoTI.csv',encoding='latin-1')
df14 = pd.read_csv(AWS_BUCKET_URL +'/Vacante_FrontEnd.csv',encoding='latin-1')
df=pd.concat([df1, df2,df3, df4,df5, df6,df7, df8,df9, df10,df11, df12,df13, df14,df15])
dfd=df.reset_index()
dfd.pop("index")

try:
    df = get_UN_data()
    countries = st.multiselect(
        "Choose countries", list(df.index), ["China", "United States of America"]
    )
    if not countries:
        st.error("Please select at least one country.")
    else:
        data = df.loc[countries]
        data /= 1000000.0
        st.write("### Gross Agricultural Production ($B)", data.sort_index())

        data = data.T.reset_index()
        data = pd.melt(data, id_vars=["index"]).rename(
            columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
        )
        chart = (
            alt.Chart(data)
            .mark_area(opacity=0.3)
            .encode(
                x="year:T",
                y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
                color="Region:N",
            )
        )
        st.altair_chart(chart, use_container_width=True)
except URLError as e:
    st.error(
        """
        **This demo requires internet access.**

        Connection error: %s
    """
        % e.reason
    )