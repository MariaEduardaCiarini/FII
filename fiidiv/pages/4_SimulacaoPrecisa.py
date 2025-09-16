import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="🎯 Simulação Precisa de Dividendos", layout="wide")

st.title("🎯 Simulação Precisa de Dividendos de FIIs")

# Lista de FIIs disponíveis
fiis = ["RECR11.SA", "KNCR11.SA", "KNHY11.SA"]

# Barra lateral interativa
st.sidebar.header("Minhas Cotas - Simulação Precisa")
fiis_selecionados = st.sidebar.multiselect("Selecione os FIIs para simular", fiis, default=fiis)

qtd_cotas = {}
for fii in fiis_selecionados:
    qtd_cotas[fii] = st.sidebar.number_input(
        f"Cotas de {fii.replace('.SA','')}",
        min_value=0,
        step=1,
        value=10
    )

# Preparar dados
dados_fiis = {}
ano_atual = datetime.now().year

for fii in fiis_selecionados:
    ticker = yf.Ticker(fii)

    # Preço atual da cota
    preco = ticker.history(period="1d")["Close"].iloc[-1]

    # Histórico de dividendos
    dividendos = ticker.dividends
    if dividendos.empty:
        continue

    # Último dividendo
    ultimo_div = dividendos.iloc[-1]
    data_ultimo = dividendos.index[-1].strftime("%d/%m/%Y")

    # Dividend yield mensal
    dy_mensal = ultimo_div / preco * 100

    # Dividendos acumulados no ano atual
    total_ano_cota = dividendos[dividendos.index.year == ano_atual].sum()

    # Simulações
    total_recebido_ano = total_ano_cota * qtd_cotas[fii]
    renda_mensal_estim = ultimo_div * qtd_cotas[fii]
    renda_anual_estim = renda_mensal_estim * 12  # projeção futura

    # Adicionar emojis para destacar dividendos altos
    emoji = "💰" if renda_mensal_estim > 50 else "🟢"

    dados_fiis[fii] = {
        "Preço atual": f"R$ {preco:.2f}",
        "Último pagamento": data_ultimo,
        "Último dividendo/cota": f"R$ {ultimo_div:.2f} {emoji}",
        "Dividend Yield mensal": f"{dy_mensal:.2f}%",
        f"Total recebido por cota {ano_atual}": f"R$ {total_ano_cota:.2f}",
        f"Total com {qtd_cotas[fii]} cotas em {ano_atual}": f"R$ {total_recebido_ano:.2f}",
        "Renda mensal estimada": f"R$ {renda_mensal_estim:.2f}",
        "Projeção anual estimada": f"R$ {renda_anual_estim:.2f}"
    }

# Exibir tabela
if dados_fiis:
    df = pd.DataFrame(dados_fiis).T
    st.subheader("📊 Resultado da Simulação Precisa")
    st.dataframe(df)

    # Gráfico da projeção anual
    colunas_projecao = ["Projeção anual estimada"]
    valores = [float(x.replace("R$ ", "").replace(",", "")) for x in df[colunas_projecao].values.flatten()]
    st.subheader("📈 Projeção Anual Estimada (base no último dividendo)")
    st.bar_chart(pd.DataFrame(valores, index=df.index, columns=["R$"]))
    st.write("💡 O gráfico mostra a projeção anual estimada com base nas cotas inseridas.")
else:
    st.warning("Nenhum dado disponível para os FIIs selecionados.")
