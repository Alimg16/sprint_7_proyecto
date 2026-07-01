import pandas as pd
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import streamlit as st

# Encabezado
st.header("Panel de Análisis de Vehículos en Venta")

# Descripción de lo que hace la aplicación
st.write(
    "Esta aplicación permite explorar un conjunto de datos de anuncios "
    "de venta de vehículos usados en Estados Unidos mediante gráficos "
    "interactivos creados con Plotly."
)
# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir gráfico de dispersión')

# Crear boton en la aplicación Streamlit
graf_button = st.button("Mostrar gráfico")


# Lógica a ejecutar cuando se hace clic en el botón "Mostrar histograma"
if graf_button:
    if build_histogram:
        # Escribir un mensaje en la aplicación
        st.write('Este gráfico muestra cómo se distribuye el kilometraje de los coches.')

        # Crear un histograma utilizando plotly.graph_objects
        # Se crea una figura vacía y luego se añade un rastro de histograma
        fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

        # Se añade título y nombre de los ejes al gráfico
        fig.update_layout(title="Distribución del kilometraje de los vehículos", xaxis_title="Odómetro", yaxis_title="Cantidad de vehículos")

        # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
        # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
        st.plotly_chart(fig, use_container_width=True)

    # Lógica a ejecutar cuando se hace clic en el botón "Mostrar gráfico de dispersión"
    if build_scatter:
        # Escribir un mensaje en la aplicación
        st.write('Gráfico de dispersión entre el kilometraje y el precio de los vehículos.')

        # Crear un grafico de dispersión utilizando plotly.graph_objects
        # Se crea una figura vacía y luego se añade un rastro de histograma
        fig = go.Figure(data=[go.Scatter(x=car_data["odometer"],y=car_data["price"],mode="markers")])

        # Se añade título y nombre de los ejes al gráfico
        fig.update_layout(title="Relación entre kilometraje y precio", xaxis_title="Odómetro", yaxis_title="Precio")

        # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
        # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
        st.plotly_chart(fig, use_container_width=True)