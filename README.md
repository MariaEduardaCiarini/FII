# 📊 Simulador de Carteira de FIIs

Dashboard interativo desenvolvido em **Python** para simular uma carteira hipotética de **Fundos de Investimento Imobiliário (FIIs)**, permitindo acompanhar preços, dividendos e estimativas de renda passiva a partir da quantidade de cotas definida pelo usuário.

🔗 **Repositório:** https://github.com/MariaEduardaCiarini/FII

🚀 **Aplicação online:** https://pythonfii.streamlit.app/

---

## 🎯 Sobre o projeto

O projeto foi desenvolvido com o objetivo de aplicar conceitos de **Python, análise de dados, visualização de informações financeiras e desenvolvimento de aplicações web interativas**.

A aplicação permite montar uma carteira hipotética de FIIs e visualizar, de forma dinâmica, informações relevantes sobre os ativos selecionados.

Os dados de mercado são consultados utilizando a biblioteca **yfinance**, permitindo trabalhar com informações atualizadas disponibilizadas para os respectivos ativos.

> **Importante:** este projeto possui finalidade educacional e de simulação. Os dados e cálculos apresentados não constituem recomendação de investimento.

---

## 🚀 Funcionalidades

### 💼 Simulação de carteira

O usuário pode definir a quantidade de cotas que deseja possuir de cada FII através dos controles disponíveis na barra lateral.

Atualmente, a carteira utiliza:

* **RECR11**
* **KNCR11**
* **KNHY11**

A quantidade de cotas pode ser ajustada individualmente para cada fundo.

### 📈 Dados dos FIIs

Para cada ativo, a aplicação consulta e apresenta:

* Preço atual da cota
* Quantidade de cotas
* Último dividendo por cota
* Dividend Yield mensal
* Renda mensal estimada
* Renda anual estimada
* Valor investido

Os dados são obtidos através do `yfinance`.

### 💰 Estimativa de renda

A aplicação utiliza a quantidade de cotas definida pelo usuário para estimar a renda proveniente dos dividendos.

#### Renda mensal

```text
Renda mensal = Último dividendo × Quantidade de cotas
```

#### Renda anual estimada

```text
Renda anual = Renda mensal × 12
```

#### Valor investido

```text
Valor investido = Preço atual × Quantidade de cotas
```

### 📊 Dashboard interativo

A interface foi construída utilizando **Streamlit**, com:

* Layout responsivo
* Barra lateral de configuração
* Cards individuais para os FIIs
* Atualização dinâmica dos valores
* Interface em tema escuro
* Visualização organizada dos principais indicadores

A aplicação publicada utiliza o Streamlit e está disponível online.

---

## 🛠️ Tecnologias utilizadas

| Tecnologia       | Utilização                              |
| ---------------- | --------------------------------------- |
| **Python 3.12+** | Linguagem principal                     |
| **Streamlit**    | Desenvolvimento do dashboard            |
| **yfinance**     | Consulta de dados financeiros           |
| **Pandas**       | Manipulação e análise de dados          |
| **Matplotlib**   | Visualização de dados                   |
| **Scikit-learn** | Recursos de análise/modelagem           |
| **Poetry**       | Gerenciamento do projeto e dependências |
| **Git/GitHub**   | Versionamento                           |

As dependências e a versão mínima do Python estão definidas no `pyproject.toml` do projeto.

---

## 🧱 Estrutura do projeto

```text
FII/
│
├── fiidiv/
│   │
│   ├── pages/
│   │
│   ├── src/
│   │   └── fiidiv/
│   │       └── __init__.py
│   │
│   ├── tests/
│   │
│   ├── Aplicativo.py
│   ├── README.md
│   ├── pyproject.toml
│   └── poetry.lock
│
└── .gitignore
```

A estrutura atual utiliza uma organização baseada em pacote Python, com código em `src`, testes separados e gerenciamento de dependências através do Poetry.

---

## ⚙️ Requisitos

Antes de executar o projeto localmente, é necessário possuir:

* Python **3.12 ou superior**
* Git
* Poetry

A versão mínima do Python está configurada no próprio projeto como `>=3.12`.

---

## 📥 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/MariaEduardaCiarini/FII.git
```

### 2. Acesse o projeto

```bash
cd FII
```

### 3. Entre no diretório da aplicação

```bash
cd fiidiv
```

### 4. Instale as dependências

Utilizando Poetry:

```bash
poetry install
```

Ou, caso prefira utilizar um ambiente virtual tradicional:

```bash
python -m venv .venv
```

#### Windows

```bash
.venv\Scripts\activate
```

Depois:

```bash
pip install pandas scikit-learn streamlit matplotlib yfinance
```

---

## ▶️ Executando a aplicação

Com o ambiente configurado, execute:

```bash
streamlit run Aplicativo.py
```

O Streamlit iniciará o servidor local e disponibilizará o dashboard no navegador.

---

## 🖥️ Como utilizar

### 1. Escolha a quantidade de cotas

Utilize os controles da barra lateral para definir quantas cotas deseja simular para cada FII.

### 2. Consulte os indicadores

O dashboard apresenta automaticamente os dados de cada fundo.

### 3. Analise a renda estimada

A partir da quantidade de cotas selecionada, o sistema calcula:

```text
Quantidade de cotas
        ↓
Último dividendo
        ↓
Renda mensal estimada
        ↓
Renda anual estimada
```

### 4. Compare a carteira

O usuário pode modificar a quantidade de cotas e observar como a composição hipotética da carteira altera a renda estimada.

---

## 🧮 Exemplo de simulação

Supondo:

```text
FII: RECR11
Quantidade: 100 cotas
Último dividendo: R$ 0,80
```

A estimativa seria:

```text
Renda mensal
100 × R$ 0,80
= R$ 80,00
```

E, utilizando a mesma referência mensal:

```text
Renda anual estimada
R$ 80,00 × 12
= R$ 960,00
```

Os valores reais apresentados pelo sistema dependem dos dados retornados para o ativo no momento da consulta.

---

## 📌 Arquitetura simplificada

```text
                 ┌─────────────────────┐
                 │      Usuário        │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │      Streamlit      │
                 │    Dashboard Web    │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │      yfinance       │
                 │   Dados dos FIIs    │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │  Processamento      │
                 │       Python        │
                 └──────────┬──────────┘
                            │
                            ▼
              ┌─────────────────────────────┐
              │ Indicadores da carteira     │
              │                             │
              │ • Preço                     │
              │ • Dividendos                │
              │ • DY                        │
              │ • Renda mensal              │
              │ • Renda anual               │
              │ • Valor investido           │
              └─────────────────────────────┘
```

---

## 🧪 Testes

O projeto possui um diretório dedicado a testes:

```text
tests/
```

A estrutura de testes está separada do código principal para facilitar a manutenção e evolução da aplicação.

---

## 📚 Conceitos aplicados

Este projeto envolve conceitos importantes de desenvolvimento e análise de dados:

* Programação em Python
* Manipulação de dados
* Consumo de dados financeiros
* APIs e bibliotecas de dados
* Cálculos financeiros
* Desenvolvimento de dashboards
* Visualização de informações
* Interface interativa
* Ambientes virtuais
* Gerenciamento de dependências
* Estruturação de projetos Python
* Testes automatizados
* Versionamento com Git

---

## 🔮 Próximas melhorias

Algumas funcionalidades que podem ser adicionadas futuramente:

* [ ] Permitir que o usuário adicione qualquer FII pelo ticker
* [ ] Cadastro persistente da carteira
* [ ] Histórico de patrimônio
* [ ] Gráficos de evolução dos FIIs
* [ ] Gráfico de distribuição da carteira
* [ ] Comparação entre diferentes FIIs
* [ ] Rentabilidade acumulada
* [ ] Dividend Yield histórico
* [ ] Reinvestimento automático dos dividendos
* [ ] Simulação de aportes mensais
* [ ] Simulação de juros compostos
* [ ] Comparação com CDI e IPCA
* [ ] Backtesting de estratégias
* [ ] Exportação dos resultados para CSV/Excel
* [ ] Sistema de autenticação
* [ ] Banco de dados para armazenamento das carteiras

---

## ⚠️ Disclaimer

Este projeto foi desenvolvido para **fins educacionais e de estudo de programação, análise de dados e simulação financeira**.

As informações apresentadas são obtidas de fontes externas e podem apresentar atrasos, inconsistências ou diferenças em relação aos dados oficiais.

**Nenhuma informação apresentada pela aplicação deve ser interpretada como recomendação, indicação ou aconselhamento financeiro.**

Antes de tomar qualquer decisão de investimento, consulte fontes oficiais e profissionais devidamente habilitados.

---

## 👩‍💻 Autora

**Maria Eduarda Ciarini**

Desenvolvedora com foco em **Backend, Python, Java e desenvolvimento de aplicações orientadas a dados**.

### Tecnologias

```text
Python • Java • Spring Boot • Django • PostgreSQL
Git • GitHub • Docker • Streamlit • SQL
```

---

## 🔗 Links

* **GitHub:** https://github.com/MariaEduardaCiarini
* **Projeto:** https://github.com/MariaEduardaCiarini/FII
* **Aplicação:** https://pythonfii.streamlit.app/

---

⭐ Se este projeto foi útil ou interessante, considere deixar uma estrela no repositório!
