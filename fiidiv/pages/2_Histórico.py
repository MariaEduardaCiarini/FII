import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="📅 Histórico de Dividendos", layout="wide")

st.title("📅 Histórico de Dividendos de FIIs")

# Lista de FIIs disponíveis
fiis = ["RECR11.SA", "KNCR11.SA", "KNHY11.SA"]

# Barra lateral interativa
st.sidebar.header("Filtros")
fiis_selecionados = st.sidebar.multiselect(
    "Selecione os FIIs", fiis, default=[fiis[0]]
)

num_meses = st.sidebar.slider(
    "Número de meses para exibir", 1, 24, 12
)

# Coletar dados de dividendos
dados = pd.DataFrame()

for fii in fiis_selecionados:
    ticker = yf.Ticker(fii)
    dividendos = ticker.dividends

    if not dividendos.empty:
        df_fii = dividendos.resample("M").sum().to_frame(name=fii)
        dados = pd.concat([dados, df_fii], axis=1)

if dados.empty:
    st.warning("Nenhum histórico disponível para os FIIs selecionados.")
else:
    # Formatar índice para mês/ano
    dados.index = dados.index.strftime("%Y-%m")
    
    # Mostrar gráfico
    st.line_chart(dados.tail(num_meses))
    
    # Mostrar tabela
    st.dataframe(dados.tail(num_meses))
    
    st.write("O gráfico e a tabela acima mostram o total de dividendos pagos por mês para os FIIs selecionados.")
