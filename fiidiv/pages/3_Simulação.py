import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="🧮 Simulação de Dividendos", layout="wide")

st.title("🧮 Simulação de Dividendos de FIIs")

# Lista de FIIs disponíveis
fiis = ["RECR11.SA", "KNCR11.SA", "KNHY11.SA"]

# Barra lateral interativa
st.sidebar.header("Seleção de FIIs e Cotas")
fiis_selecionados = st.sidebar.multiselect("Selecione os FIIs", fiis, default=fiis)

qtd_cotas = {}
for fii in fiis_selecionados:
    qtd_cotas[fii] = st.sidebar.number_input(
        f"Cotas de {fii.replace('.SA','')}",
        min_value=0,
        step=1,
        value=100
    )

# Preparar dados
dados_fiis = {}
ano_atual = datetime.now().year

for fii in fiis_selecionados:
    ticker = yf.Ticker(fii)
    
    # Preço atual (último fechamento)
    preco = ticker.history(period="1d")["Close"].iloc[-1]
    
    # Dividendos históricos
    dividendos = ticker.dividends
    if dividendos.empty:
        continue
    
    # Último dividendo pago
    ultimo_div = dividendos.iloc[-1]
    data_ultimo = dividendos.index[-1].strftime("%d/%m/%Y")
    
    # Dividend yield mensal aproximado
    dy_mensal = ultimo_div / preco * 100
    
    # Dividendos do ano atual
    total_ano_cota = dividendos[dividendos.index.year == ano_atual].sum()
    
    # Simulação
    total_recebido_ano = total_ano_cota * qtd_cotas[fii]
    renda_mensal_estim = ultimo_div * qtd_cotas[fii]
    
    dados_fiis[fii] = {
        "Preço atual": f"R$ {preco:.2f}",
        "Último pagamento": data_ultimo,
        "Último dividendo/cota": f"R$ {ultimo_div:.2f}",
        "Dividend Yield mensal": f"{dy_mensal:.2f}%",
        f"Total por cota {ano_atual}": f"R$ {total_ano_cota:.2f}",
        f"Total com {qtd_cotas[fii]} cotas em {ano_atual}": f"R$ {total_recebido_ano:.2f}",
        "Renda mensal estimada": f"R$ {renda_mensal_estim:.2f}"
    }

# Mostrar tabela
if dados_fiis:
    df = pd.DataFrame(dados_fiis).T
    st.dataframe(df)
    
    # Gráfico da renda anual simulada
    colunas_totais = [c for c in df.columns if "Total com" in c]
    if colunas_totais:
        st.subheader(f"📈 Renda anual estimada em {ano_atual}")
        valores = [float(x.replace("R$ ", "").replace(",", ".")) for x in df[colunas_totais].values.flatten()]
        st.bar_chart(pd.DataFrame(valores, index=df.index, columns=["R$"]))
        st.write("💡 O gráfico mostra a renda anual estimada com base nas cotas inseridas.")
else:
    st.warning("Nenhum dado disponível para os FIIs selecionados.")
