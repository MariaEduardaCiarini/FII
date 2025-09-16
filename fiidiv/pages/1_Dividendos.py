import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="💸 Últimos Dividendos", layout="wide")

st.title("💸 Últimos Dividendos de FIIs")

# Lista de FIIs disponíveis
fiis = ["RECR11.SA", "KNCR11.SA", "KNHY11.SA"]

# Barra lateral interativa
st.sidebar.header("Filtros")
fiis_selecionados = st.sidebar.multiselect(
    "Selecione os FIIs", fiis, default=fiis
)

# Dicionário para armazenar dados
dados = {}

for fii in fiis_selecionados:
    ticker = yf.Ticker(fii)
    dividendos = ticker.dividends

    if not dividendos.empty:
        ultimos = dividendos.tail(5)
        total_ano_atual = dividendos[dividendos.index.year == datetime.now().year].sum()
        
        dados[fii] = {
            "Último pagamento": ultimos.index[-1].strftime("%d/%m/%Y"),
            "Último dividendo": round(ultimos.iloc[-1], 2),
            f"Total {datetime.now().year}": round(total_ano_atual, 2)
        }

# Criar DataFrame
if dados:
    df = pd.DataFrame(dados).T
    st.dataframe(df)
else:
    st.warning("Selecione pelo menos um FII com dados disponíveis.")

st.write("💡 Use os filtros na barra lateral para explorar os FIIs selecionados.")
