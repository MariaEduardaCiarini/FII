import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="📦 Carteira Consolidada de FIIs", layout="wide")

st.title("📦 Carteira Consolidada de FIIs")

# Lista de FIIs disponíveis
fiis = ["RECR11.SA", "KNCR11.SA", "KNHY11.SA"]

# Barra lateral interativa
st.sidebar.header("Minhas Cotas - Carteira Consolidada")
fiis_selecionados = st.sidebar.multiselect("Selecione os FIIs da carteira", fiis, default=fiis)

qtd_cotas = {}
for fii in fiis_selecionados:
    qtd_cotas[fii] = st.sidebar.number_input(
        f"Cotas de {fii.replace('.SA','')}",
        min_value=0,
        step=1,
        value=10
    )

# Inicialização das variáveis
dados_fiis = {}
total_renda_mensal = 0
total_renda_anual = 0
total_investido = 0
ano_atual = datetime.now().year

# Coletar dados de cada FII
for fii in fiis_selecionados:
    ticker = yf.Ticker(fii)

    # Preço atual da cota
    preco = ticker.history(period="1d")["Close"].iloc[-1]
    investimento = preco * qtd_cotas[fii]

    # Dividendos
    dividendos = ticker.dividends
    if dividendos.empty:
        continue

    ultimo_div = dividendos.iloc[-1]
    data_ultimo = dividendos.index[-1].strftime("%d/%m/%Y")
    total_ano_cota = dividendos[dividendos.index.year == ano_atual].sum()

    # Simulações
    renda_mensal = ultimo_div * qtd_cotas[fii]
    renda_anual_real = total_ano_cota * qtd_cotas[fii]
    renda_anual_estim = renda_mensal * 12

    total_renda_mensal += renda_mensal
    total_renda_anual += renda_anual_estim
    total_investido += investimento

    # Emojis para destaque
    emoji = "💰" if renda_mensal > 50 else "🟢"

    dados_fiis[fii] = {
        "Preço atual": f"R$ {preco:.2f}",
        "Investimento total": f"R$ {investimento:.2f}",
        "Último pagamento": data_ultimo,
        "Último dividendo/cota": f"R$ {ultimo_div:.2f} {emoji}",
        f"Total recebido em {ano_atual}": f"R$ {renda_anual_real:.2f}",
        "Renda mensal estimada": renda_mensal,
        "Projeção anual estimada": renda_anual_estim
    }

# Tabela detalhada por FII
if dados_fiis:
    df = pd.DataFrame(dados_fiis).T

    # Destacar maiores e menores rendas mensais
    def color_renda_mensal(val):
        if val == df["Renda mensal estimada"].max():
            color = 'background-color: #d4edda'  # verde claro
        elif val == df["Renda mensal estimada"].min():
            color = 'background-color: #f8d7da'  # vermelho claro
        else:
            color = ''
        return color

    st.subheader("📊 Dividendos por FII")
    st.dataframe(
        df.style.format({
            "Renda mensal estimada": "R$ {:.2f}",
            "Projeção anual estimada": "R$ {:.2f}",
        }).applymap(color_renda_mensal, subset=["Renda mensal estimada"])
    )

    # Resumo consolidado
    st.subheader("📦 Resumo da Carteira Consolidada")
    st.metric("💰 Total Investido", f"R$ {total_investido:,.2f}")
    st.metric("📈 Renda Mensal Estimada", f"R$ {total_renda_mensal:,.2f}")
    st.metric("📅 Projeção Anual Estimada", f"R$ {total_renda_anual:,.2f}")

    # Gráfico comparativo
    st.subheader("📊 Projeção Anual por FII")
    colunas_projecao = ["Projeção anual estimada"]
    valores = df[colunas_projecao]
    st.bar_chart(valores)
    st.write("💡 O gráfico mostra a projeção anual estimada com base nas cotas inseridas.")

else:
    st.warning("Nenhum dado disponível para os FIIs selecionados.")
