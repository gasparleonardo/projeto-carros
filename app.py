import pandas as pd
import plotly.express as px
import streamlit as st

# título
st.header("Dashboard de Anúncios de Carros Usados")

# carregar dados
car_data = pd.read_csv("vehicles_us.csv")

st.write("Este aplicativo permite explorar dados de anúncios de carros usados.")

# mostrar tabela inicial
if st.checkbox("Mostrar dados do dataset"):
    st.write(car_data.head())

# filtro por tipo de veículo
vehicle_types = car_data["type"].dropna().unique()
selected_type = st.selectbox("Selecione o tipo de veículo", vehicle_types)

filtered_data = car_data[car_data["type"] == selected_type]

st.write(f"Mostrando dados para: {selected_type}")

# histograma de quilometragem
if st.checkbox("Mostrar histograma da quilometragem"):
    fig = px.histogram(filtered_data, x="odometer", title="Distribuição de quilometragem")
    st.plotly_chart(fig, use_container_width=True)

# gráfico de dispersão
if st.checkbox("Mostrar gráfico de dispersão (quilometragem vs preço)"):
    fig = px.scatter(
        filtered_data,
        x="odometer",
        y="price",
        title="Relação entre quilometragem e preço"
    )
    st.plotly_chart(fig, use_container_width=True)