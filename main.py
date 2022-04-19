import streamlit as st
import pandas as pd
import pickle as pk

## carregando dados 
df = pd.read_csv("data/casas.csv")

## pegando paramentros para componentes do streamlit
media_area = float(df["tamanho"].mean())
area_max = float(df["tamanho"].max())
area_min = float(df["tamanho"].min())

media_ano = int(df["ano"].mean())
ano_max = int(df["ano"].max())
ano_min = int(df["ano"].min())

## carregando modelo
with open("models/model_rf.pkl", 'rb') as arquivo:
    modelo_rf = pk.load(arquivo)

## app
st.title("App - Precificação de imóveis")

st.subheader(
    '''Escolha as opções abaixo'''
)

area = st.slider("Área do imóvel (m2)", min_value=area_min, max_value=area_max, value=media_area)

garagem_options = [1, 2, 3]
garagem = st.radio('Número de garagens', options=garagem_options)

bairro = st.text_input("Qual bairro")

ano = st.slider("Ano de construção", min_value=ano_min, max_value=ano_max, value=media_ano)

# st.sidebar.title("Insira suas informações")
# name_user = st.sidebar.text_input("Nome")

dados = {
    'tamanho': [area],
    'ano': [ano],
    'garagem': [garagem]
}

click = st.button("Calcular preço")
if click:
    y_pred = float(modelo_rf.predict(pd.DataFrame(dados))[0])
    y_pred = round(y_pred, 2)
    st.write(f"Com as informações passadas o valor da casa é de US$ {y_pred}")