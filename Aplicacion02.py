import streamlit as st
import pandas as pd

# instalar sklearn       python -m pip install sklearn
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

#anexar estlo
st.markdown(
    """
    <style>
        .main
        {   
            background-color:  rgba(23, 37, 0, 1);;
            font-size: 14px;
            color: Gray;
        }
    </style>    
    """,
    unsafe_allow_html = True
)


header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

@st.cache
def get_data(url):
    df = pd.read_csv(url)
    return df

with header:
    st.title("Nuestra primera aplicación Web con Python")
    st.text("Esta es la primera aplicacion web desarrollada con python  y Streamlit  para mostrar su funcionamiento")

with dataset:
    st.header("Conjunto de datos")    
    st.text("Este es un dataset de ejemplo usado con propositos academicos")
    df = get_data("yellow_tripdata_2021.csv")
    st.write(df.head(10))
    
    st.subheader("ID de localizacion de levantamietos(pick up) de taxis en NYC")
    location_dist = pd.DataFrame(df["PULocationID"].value_counts()).head(50)
    st.bar_chart(location_dist)
    
    
with features:
    st.header("Caracteristicas encontradas/generadas")
    st.markdown("* *** ")
    
with model_training:
    st.header("Momento de entrenar el modelo")
    st.text("Aqui se definen los parametros con los cuales  observaremos el rendimiento del modelo")
    sel_col, disp_col = st.columns(2)
    
    max_depth = sel_col.slider("Cual debe ser el valor máximo para el modelo", min_value = 10, max_value = 100, value = 20 )
    
    n_estimators= sel_col.selectbox("Cuantos Trees deberán  contener?", options =[100,200,300, 'Not limit'], index = 0 )
    
    
    sel_col.write("Aqui hay una lista de las caracteristicas de mi dataSet")
    sel_col.write(df.columns)
    
    sel_col.write("Aqui hay otro ejemplo para listar las caracteristicas de mi dataSet")
    
    feature2 = sel_col.selectbox("Selecicona la caracerística?", options = df.columns.tolist(), index = 0 )
    sel_col.write(feature2)
        
    input_feature = sel_col.text_input("¿Cual caracteritica debe ser usada como caracteristica de entrada?", feature2)
    
    if n_estimators == 'Not limit':
        regr = RandomForestRegressor(max_depth = max_depth)    
    else:        
        regr = RandomForestRegressor(max_depth = max_depth, n_estimators = n_estimators)
    
    x= df[[input_feature]]
    y = df[['trip_distance']]
    
    regr.fit(x,y)
    prediction = regr.predict(y)
    
    disp_col.subheader("El promedio de error absoluto en el modelo es:")
    disp_col.write(mean_absolute_error(y, prediction) )
    
    disp_col.subheader("El promedio del  error cuadratico del modelo es:")
    disp_col.write(mean_squared_error(y, prediction) )
    
    disp_col.subheader("El promedio del  error cuadratico del modelo es:")
    disp_col.write(r2_score(y, prediction) )
    