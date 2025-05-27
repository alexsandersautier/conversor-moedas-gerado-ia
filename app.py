import streamlit as st
import requests
from decouple import config
from datetime import datetime
# Título da página

try:
    api_key = config('API_KEY')
except:
    api_key = st.secrets['API_KEY']

st.title("💱 Conversor de Moedas")

# Sidebar com seletores de moeda
st.sidebar.header("Configurações de Conversão")

# Lista de moedas suportadas
moedas = ["USD", "EUR", "BRL", "JPY", "GBP", "ARS", "BTC"]

moeda_origem = st.sidebar.selectbox("Moeda de Origem", moedas)
moeda_destino = st.sidebar.selectbox("Moeda de Destino", moedas)

# Campo para digitar o valor a ser convertido
valor = st.number_input(f"Digite o valor em {moeda_origem}:", min_value=0.0, format="%.2f")

# Botão de conversão
if st.button("Converter"):
    try:
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{moeda_origem}/{moeda_destino}/{valor}"
        print(url)
        resposta = requests.get(url)
        dados = resposta.json()

        print(dados)

        if resposta.status_code >= 200 and resposta.status_code < 300:
            resultado = dados["conversion_result"]
            st.success(f"{valor:.2f} {moeda_origem} = {resultado:.2f} {moeda_destino}")
        else:
            st.error("Erro ao obter a taxa de câmbio. Tente novamente.")
    except Exception as e:
        st.error(f"Ocorreu um erro: {str(e)}")