import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from urllib.error import URLError


path = 'C:/Users/ADMINISTRADORR/Downloads/pro/ProyectoIntegrador'
df15 = pd.read_csv(path + '/VacanteAnalistaDeDatos.csv')
df1 = pd.read_csv(path + '/Vacantes_Tester.csv', encoding='latin-1')
df2 = pd.read_csv(path + '/Vacantes_GerenteTI.csv',encoding='latin-1')
df3 = pd.read_csv(path + '/Vacantes_Fullstack.csv',encoding='latin-1')
df4 = pd.read_csv(path + '/Vacantes_DesarrolladorWeb.csv',encoding='latin-1')
df5 = pd.read_csv(path + '/Vacantes_DesarrolladorSoftware.csv',encoding='latin-1')
df6 = pd.read_csv(path + '/Vacantes_CientificoDatos.csv',encoding='latin-1')
df7 = pd.read_csv(path + '/Vacantes_Ciberseguridad.csv',encoding='latin-1')
df8 = pd.read_csv(path + '/Vacantes_AdministradorBD.csv',encoding='latin-1')
df9 = pd.read_csv(path + '/VacanteProgramadorPHP.csv',encoding='latin-1')
df10 = pd.read_csv(path + '/VacantedesarrolladorNET.csv',encoding='latin-1')
df11 = pd.read_csv(path + '/VacanteDesarrolladorMoviles.csv',encoding='latin-1')
df12= pd.read_csv(path + '/VacanteDesarrolladorJr.csv',encoding='latin-1')
df13 = pd.read_csv(path + '/VacanteArquitectoTI.csv',encoding='latin-1')
df14 = pd.read_csv(path + '/Vacante_FrontEnd.csv',encoding='latin-1')
df=pd.concat([df1, df2,df3, df4,df5, df6,df7, df8,df9, df10,df11, df12,df13, df14,df15])
dfd=df.reset_index()
dfd.pop("index")


header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

@st.cache
def get_data(url):
    df = pd.read_csv(url)
    return df



with header:
  col1, col2, col3 = st.columns([1,6,1])

  with col1:
      st.image("LOGO_TECNM_BLANCO.png", width=150)

  with col2:
    st.markdown("<h1 style='text-align: center; '>BIENVENIDO</h1>", unsafe_allow_html=True)
    
  with col3:
      st.image("isic.png", width=90)
 
  st.header("Ciencia de Datos aplicada al analisis de vacantes del area de TI")
  
with dataset:
    st.header("Conjunto de datos")    
    st.text("Este es conjunto de datos que se usara en nuestro sistema")
    st.write(df.head())

dEstrellas=pd.DataFrame(dfd["Vacantes_Estrellas"])
dEstrellas.columns=["Estrellas"]
for feature in dEstrellas:
  if dEstrellas[feature].dtype=="float64":
    dEstrellas[feature]=dEstrellas[feature].fillna("0")
  else:
    dEstrellas[feature] =dEstrellas[feature].fillna("-1")
dEstrellas=dEstrellas.reset_index()
dEstrellas.pop("index")

dFecha=dfd["Vacantes_Fecha"].str.split(' +', expand=True)
dFecha.pop(0)
dFecha.pop(2)
dFecha.columns=["Fecha"]
for feature in dFecha:
  if dFecha[feature].dtype=="object":
    dFecha[feature]=dFecha[feature].fillna("0")
  else:
    dFecha[feature] =dFecha[feature].fillna(-1)
for i in range(len(dFecha)):
  col=dFecha.iloc[i,0]
  if col=="publicado":
    dFecha.loc[i]="7"
  if col=="30+":
     dFecha.loc[i]="30"
for j in range(len(dFecha)):
  col=dFecha.iloc[j,0]
  if int(col)!=7:
    dFecha.loc[j]=str(int(dFecha.iloc[j])+7)
  col=dFecha.iloc[j,0]
  if int(col)>=30:
    dFecha.loc[j]="30"

    dLugar=dfd["Vacantes_Lugar"].str.split(',', expand=True)

dLugar.columns = ["municipio", "est"]
for feature in dLugar:
  if dLugar[feature].dtype=="object":
    dLugar[feature]=dLugar[feature].fillna("0")
  else:
    dLugar[feature] =dLugar[feature].fillna(-1)
for i in range(len(dLugar)):
  cal=dLugar.iloc[i,1]
  if cal=="0":
    dLugar.loc[i,"Estado"]=dLugar.iloc[i,0]
  else:
    dLugar.loc[i,"Estado"]=dLugar.iloc[i,1]
dLugar.pop("municipio")
dLugar.pop("est")
for i in range(len(dLugar)):
  cal=dLugar.iloc[i,0]
  if cal=="Desde casa":
    dLugar.loc[i,"Estado"]="Remoto"
dLugar=dLugar["Estado"].str.split('Remoto', expand=True) 
dLugar.columns = ["Estado", "Remoto"]
for i in range(len(dLugar)):
  cal=dLugar.iloc[i,1]
  if cal=="":
    dLugar.loc[i,"Estado"]="Remoto"
dLugar.pop("Remoto")
dLugar=dLugar["Estado"].str.split('', expand=True) 
dLugar.columns = ["Estado", "algo"]
dLugar.pop("algo")
dLugar=dLugar["Estado"].str.split('+', expand=True) 
dLugar.columns = ["Estado", "+"]
dLugar.pop("+")
dLugar=dLugar["Estado"].str.split('•', expand=True) 
dLugar.columns = ["Estado", "al"]
dLugar.pop("al")
for i in range(len(dLugar)):
  cal=dLugar.iloc[i,0]
  if cal=="Ciudad de México":
    dLugar.loc[i,"Estado"]="CDMX"
  if cal=="Edo. de México" or cal==" Méx.":
    dLugar.loc[i,"Estado"]="Méx."
  if cal=="Baja California Sur":
     dLugar.loc[i,"Estado"]="B.C.S."

dSueldo=dfd ["Vacantes_Sueldo"].str.split('[- ]',expand=True)
dSueldo.pop(1)
dSueldo.pop(4)
for feature in dSueldo:
  if dSueldo[feature].dtype=="object":
    dSueldo[feature]=dSueldo[feature].fillna("0")
  else:
      dSueldo[feature] =dSueldo[feature].fillna(-1)
dSueldo
columnas=[0,3]
dSueldo=dSueldo.replace('\$','',regex=True)
dSueldo=dSueldo.replace('\,','',regex=True)
dSueldo.columns = ["num1", "mese", "num2","mesee"]


for i in range(len(dSueldo)):
    Class = dSueldo.iloc[i,3]
    if Class == '0':
      dSueldo.loc[i,"Sueldo"]=dSueldo.iloc[i,0]
    else:
      dSueldo.loc[i,"Sueldo"]=str((int(dSueldo.iloc[i,0])+int(dSueldo.iloc[i,2]))/2)
    tiempo =dSueldo.iloc[i,1]
    if tiempo=='año':
      dSueldo.loc[i,"Sueldo"]=str(float(dSueldo.iloc[i,4])/12)
    tiempo2 =dSueldo.iloc[i,3]
    if tiempo2=='año':
      dSueldo.loc[i,"Sueldo"]=str(float(dSueldo.iloc[i,4])/12)
    if tiempo=='semana':
      dSueldo.loc[i,"Sueldo"]=str(float(dSueldo.iloc[i,4])*4)
    tiempo2 =dSueldo.iloc[i,3]
    if tiempo2=='semana':
      dSueldo.loc[i,"Sueldo"]=str(float(dSueldo.iloc[i,4])*4)
dSueldo.pop("num1")
dSueldo.pop("mese")
dSueldo.pop("num2")
dSueldo.pop("mesee") 
for i in range(len(dSueldo)):
    Class = dSueldo.iloc[i,0]
    if Class == '0':
      dSueldo.loc[i,"Sueldo"]=0
    if Class=='hace':
      dSueldo.loc[i,"Sueldo"]=0
ceros=0
contar=0.0
for j in range(len(dSueldo)):
    Class = dSueldo.iloc[i,0]
    if ((j+1)%49) == 0:
      contar+=float(dSueldo.iloc[j,0])
      for q in range(j+1):
        Clas = dSueldo.iloc[q,0]
        if Clas == 0:
          ceros+=1
      for k in range(j+1):
        Clss = dSueldo.iloc[k,0]
        if Clss == 0:
          dSueldo.loc[k,"Sueldo"]=contar/(49-ceros)
      ceros=0
      contar=0
    else:
      contar+=float(dSueldo.iloc[j,0])

      dfe=dfd.drop(['Vacantes_Lugar', 'Vacantes_Fecha', 'Vacantes_Sueldo','Vacantes_Estrellas'], axis=1)
#df.insert(loc = 3,column="Estado", value=dLugar["Estado"])
dfe=pd.concat([dfe, dLugar,dSueldo,dFecha,dEstrellas], axis=1)


dfe["Sueldo"] = dfe["Sueldo"].astype('float64')
dfe["Fecha"] = dfe["Fecha"].astype('float64')
dfe["Estrellas"] = dfe["Estrellas"].astype('float64')


medians=dfe["Estrellas"].median()
print("mediana de Columna Estrellas:")
print(medians)
moda=pd.Series(dfe["Estrellas"].values.flatten()).mode()[0]
print("moda de Columna Estrellas:")
print(moda)
media=dfe["Estrellas"].mean()
print("media de Columna Estrellas:")
print(media)
medians=dfe["Fecha"].median()
print("mediana de Columna Estrellas:")
print(medians)
moda=pd.Series(dfe["Fecha"].values.flatten()).mode()[0]
print("moda de Columna Fecha:")
print(moda)
media=dfe["Fecha"].mean()
print("media de Columna Fecha:")
print(media)
medians=dfe["Sueldo"].median()
print("mediana de Columna Sueldo:")
print(medians)
moda=pd.Series(dfe["Sueldo"].values.flatten()).mode()[0]
print("moda de Columna Sueldo:")
print(moda)
media=dfe["Sueldo"].mean()
print("media de Columna Sueldo:")
print(media)
moda=pd.Series(dfe["Estado"].values.flatten()).mode()[0]
print("moda de Columna Estado:")
print(moda)
moda=pd.Series(dfe["Vacantes_name"].values.flatten()).mode()
print("moda de Columna Vacantes:")
print(moda)
moda=pd.Series(dfe["Vacantes_Empresa"].values.flatten()).mode()[0]
print("moda de Columna Empresa:")
print(moda)

dps=dfe['Estrellas'].min()
print("valor minimo de la tabla Estrellas")
print(dps)
print()
dps=dfe['Estrellas'].max()
print("valor maximo de la tabla Estrellas")
print(dps)
print()
dps=dfe['Sueldo'].min()
print("valor minimo de la tabla Sueldo")
print(dps)
print()
dps=dfe['Sueldo'].max()
print("valor maximo de la tabla Sueldo")
print(dps)
print()
dps=dfe['Fecha'].min()
print("valor minimo de la tabla Fecha")
print(dps)
print()
dps=dfe['Fecha'].max()
print("valor maximo de la tabla Fecha")
print(dps)
print()
dps=dfe['Vacantes_name'].min()
print("valor minimo de la tabla Vacantes_name")
print(dps)
print()
dps=dfe['Vacantes_name'].max()
print("valor maximo de la tabla Vacantes_name")
print(dps)
print()
dps=dfe['Vacantes_Empresa'].min()
print("valor minimo de la tabla Vacantes_Empresa")
print(dps)
print()
dps=dfe['Vacantes_Empresa'].max()
print("valor maximo de la tabla Vacantes_Empresa")
print(dps)
print()

freq = dfe.groupby(['Estrellas']).count() 
print(freq)
fre = dfe.groupby(['Fecha']).count() 
print(fre)
fr = dfe.groupby(['Sueldo']).count() 
print(fr)
f = dfe.groupby(['Vacantes_name']).count() 
print(f)
fe = dfe.groupby(['Vacantes_Empresa']).count() 
print(fe)
feb = dfe.groupby(['Perfil']).count() 
print(feb)
febe = dfe.groupby(['Estado']).count() 
print(febe)

#dfr=dLugar.query("Estado=='CDMX'")
#dLugar.head(100)
feb = dfe.groupby(['Estado']).count() 
febe= feb.reset_index()
feb = dfe.groupby(['Perfil']).count() 
febe2= feb.reset_index()
feb = dfe.groupby(['Fecha']).count() 
febe3= feb.reset_index()
#*****************************************************************************
# Comienza graficacion
#*****************************************************************************
st.sidebar.subheader("Menu")
st.sidebar.button("Click me")

st.subheader('Cantidad de vacantes en el dia')

#Grafica de Vacantes en el dia
dFs=dfe.groupby('Fecha').count()
dFs.pop("Perfil")
dFs.pop("Vacantes_name")
dFs.pop("Vacantes_Descripcion")
dFs.pop("Vacantes_Empresa")
dFs.pop("Sueldo")
dFs.pop("Estrellas")
dFs.columns=["Vacantes"]
# st.line_chart(data = dFs, x = "Fecha", y = "Perfil", color = "green")
st.title("Cantidad de Convocatorias por dia")
chart_data = pd.DataFrame(
    data = dFs
    )
st.line_chart(chart_data)

# Grafica para mostrar cantidad de vacantes por perfil por cada estado
st.title("Cantidad de Vacantes por Perfil por Estado")
option = st.selectbox( 'Perfil a consultar',
(febe['Estado']))
st.write('Seleccionaste:', option)
febe1 = dfe[dfe.Estado==option].groupby(['Perfil']).count()
febe1.pop("Vacantes_Empresa")
febe1.pop("Vacantes_Descripcion")
febe1.pop("Estado")
febe1.pop("Sueldo")
febe1.pop("Fecha")
febe1.pop("Estrellas")
febe1.columns=["Vacantes"] 
febe=febe1.reset_index()
febe.columns=["Perfil","Vacantes"] 
febe
chart_data = pd.DataFrame(data = febe1.Vacantes)
st.bar_chart(chart_data)
st.vega_lite_chart(febe, {
    'mark': { "type": "bar"},
     'encoding': {
         'x': {'field': 'Perfil',"type": "ordinal"},
         'y': {'field': 'Vacantes'},
         'color': {'field': 'Perfil'},
     },
 })

 # Grafica para mostrar cantidad de vacantes por perfil por cada estado
st.title("Cantidad de Vacantes por Perfil por Estado")
option = st.selectbox( 'Perfil a consultar',
(febe2['Perfil']))
st.write('Seleccionaste:', option)
d=dfe[dfe.Perfil==option].groupby(['Estado']).count().idxmax()[0]
f1 = dfe[dfe.Perfil==option].groupby(['Estado']).count()
f1.pop("Vacantes_Empresa")
f1.pop("Vacantes_Descripcion")
f1.pop("Perfil")
f1.pop("Sueldo")
f1.pop("Fecha")
f1.pop("Estrellas")
f1.columns=["Vacantes"] 
f=f1.reset_index()
f.columns=["Estado","Vacantes"] 
f
st.write('El estado con mayor cantidad convocatorias de ', option," es ",d)
chart_data = pd.DataFrame(data = f1.Vacantes)
st.bar_chart(chart_data)
st.vega_lite_chart(f, {
    'mark': { "type": "bar"},
     'encoding': {
         'x': {'field': 'Estado',"type": "ordinal"},
         'y': {'field': 'Vacantes'},
         'color': {'field': 'Estado'},
     },
 })
 # Grafica para mostrar cantidad de vacantes por perfil por cada estado
st.title("Vacantes por dependiendo el dia de lanzamiento")
option = st.selectbox( 'Dia a consutar (30 significa mas de un mes)',
(febe3['Fecha']))
st.write('Seleccionaste:', option)
d=dfe[dfe.Fecha==option].groupby(['Perfil']).count().idxmax()[0]
f1=dfe[dfe.Fecha==option].groupby(['Perfil']).count()
f1.pop("Vacantes_Empresa")
f1.pop("Vacantes_Descripcion")
f1.pop("Fecha")
f1.pop("Sueldo")
f1.pop("Estrellas")
f1.pop("Vacantes_name")
f1.columns=["Vacantes"] 
f=f1.reset_index()
f.columns=["Perfil","Vacantes"] 
f
st.write('El estado con mayor cantidad convocatorias de ', option," es ",d)
chart_data = pd.DataFrame(data = f1.Vacantes)
st.bar_chart(chart_data)
st.vega_lite_chart(f, {
    'mark': { "type": "bar"},
     'encoding': {
         'x': {'field': 'Estado',"type": "ordinal"},
         'y': {'field': 'Vacantes'},
         'color': {'field': 'Estado'},
     },
 })