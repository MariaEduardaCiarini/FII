import streamlit as st
import yfinance as yf
from datetime import datetime

# ====== CONFIGURAÇÃO DA PÁGINA ======
st.set_page_config(page_title="📊 Meus Fundos Imobiliários", layout="wide")

# ====== ESTILO DARK ======
st.markdown("""
<style>
/* Fundo da página */
body, .main, .block-container {
    background-color: #121212;
    color: #E0E0E0;
    font-family: 'Arial', sans-serif;
}

/* Cards dos FIIs */
.fii-card {
    background-color: #1E1E1E;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    color: #E0E0E0;
    box-shadow: 0 4px 15px rgba(0,0,0,0.4);
    margin-bottom: 20px;
    transition: transform 0.2s ease-in-out;
}
.fii-card:hover {
    transform: scale(1.03);
}

/* Headers e títulos */
h1, h3, p {
    color: #E0E0E0;
}

/* Slider da barra lateral */
.stSlider > div > div > div > div {
    background-color: #333 !important;
}

/* Fundo da sidebar */
.sidebar .sidebar-content {
    background-color: #1A1A1A;
    color: #E0E0E0;
    padding: 20px;
    border-radius: 10px;
}

/* Expander estilo */
.stExpander {
    background-color: #2A2A2A !important;
    color: #E0E0E0 !important;
    border-radius: 8px;
}

/* Botões e selects */
.stButton > button, .stSelectbox > div {
    background-color: #333 !important;
    color: #E0E0E0 !important;
    border-radius: 8px;
}

/* Linha separadora */
hr {
    border-top: 1px solid #333;
}
</style>
""", unsafe_allow_html=True)

# ====== TÍTULO CENTRAL ======
st.markdown("""
<div style="text-align: center;">
    <h1>📊 Dashboard Interativo de FIIs</h1>
    <p style="font-size:16px;">Meus fundos imobiliários em tempo real!</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ====== LISTA DE FIIs ======
FIIS = ["RECR11.SA", "KNCR11.SA", "KNHY11.SA"]

# ====== BARRA LATERAL INTERATIVA ======
st.sidebar.header("⚙️ Configurações da Carteira")
st.sidebar.write("Escolha suas cotas e veja os dividendos estimados:")

cotas = {}
for fii in FIIS:
    with st.sidebar.expander(f"📌 {fii.replace('.SA','')}", expanded=True):
        cotas[fii] = st.slider(
            f"Quantas cotas você possui? 🎟️",
            min_value=0, max_value=100, value=10, step=1,
            help=f"Ajuste o número de cotas do fundo {fii.replace('.SA','')} para atualizar os dividendos."
        )

st.sidebar.markdown("---")
st.sidebar.info("💡 Ajuste suas cotas para atualizar a renda estimada automaticamente!")

# ====== FUNÇÃO PARA PEGAR DADOS ======
def pegar_dados(fii):
    ticker = yf.Ticker(fii)
    preco = ticker.history(period="1d")["Close"].iloc[-1]
    dividendos = ticker.dividends
    if dividendos.empty:
        ultimo_div = 0
        total_ano = 0
    else:
        ultimo_div = dividendos.iloc[-1]
        ano_atual = datetime.now().year
        total_ano = dividendos[dividendos.index.year == ano_atual].sum()
    dy_mensal = (ultimo_div / preco * 100) if preco > 0 else 0
    return preco, ultimo_div, total_ano, dy_mensal

# ====== MOSTRAR CARDS ======
st.subheader("💹 Seus FIIs")
cols = st.columns(len(FIIS))

for i, fii in enumerate(FIIS):
    preco, ultimo_div, total_ano, dy_mensal = pegar_dados(fii)
    qtd = cotas[fii]
    renda_mensal = ultimo_div * qtd
    renda_anual = renda_mensal * 12
    valor_investido = preco * qtd

    with cols[i]:
        st.markdown(f"""
        <div class="fii-card">
            <h3>🏢 {fii.replace('.SA','')}</h3>
            <p>💰 Preço atual: R$ {preco:.2f}</p>
            <p>🎟️ Cotas: {qtd}</p>
            <p>💵 Último dividendo/cota: R$ {ultimo_div:.2f}</p>
            <p>📈 DY mensal: {dy_mensal:.2f}%</p>
            <p>💸 Renda mensal estimada: R$ {renda_mensal:.2f}</p>
            <p>📅 Renda anual estimada: R$ {renda_anual:.2f}</p>
            <p>💼 Valor investido: R$ {valor_investido:.2f}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("🎯 **Use a barra lateral para ajustar suas cotas e atualizar os valores em tempo real!**")
st.markdown("🔍 **Explore cada fundo clicando nos expanders da barra lateral para mais detalhes!**")
