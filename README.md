# Bot Invest

Bot Invest é um projeto em Python criado para coletar, armazenar e analisar dados do mercado financeiro automaticamente.

O objetivo do sistema é construir uma base de dados histórica de ações, calcular métricas financeiras e gerar análises que podem ser utilizadas em estratégias quantitativas de investimento.

---

## Visão Geral

O projeto automatiza todo o fluxo de dados do mercado:

1. Coleta dados históricos de ações
2. Atualiza automaticamente os dados mais recentes
3. Armazena os dados localmente
4. Calcula métricas e indicadores
5. Gera gráficos para análise

Esse sistema foi desenvolvido como base para estudos de análise quantitativa e desenvolvimento de estratégias automatizadas de investimento.

---

## Funcionalidades

* Coleta automática de dados de ações
* Atualização incremental da base de dados
* Armazenamento local de dados históricos
* Cálculo de indicadores financeiros
* Geração de gráficos de análise
* Estrutura preparada para backtests e estratégias quantitativas
* Recomendações de investimento

---

## Dados Coletados

Notícias Semanais.

Para cada ativo o sistema coleta:

* Data
* Open
* High
* Low
* Close
* Volume

Os dados são armazenados localmente em arquivos CSV para facilitar análise posterior.

---

## Indicadores e Métricas

O sistema calcula métricas utilizadas em análise financeira, incluindo:

* Retornos de diferentes períodos
* Volatilidade
* Médias móveis
* Análise histórica de preços

Essas métricas podem ser utilizadas para estudos de comportamento do mercado e desenvolvimento de estratégias quantitativas.

---

## Tecnologias Utilizadas

* Python
* Pandas
* YFinance
* Matplotlib
* Pathlib
* Tabulate

Bibliotecas principais:

* pandas → manipulação de dados
* yfinance → coleta de dados de mercado
* matplotlib → visualização de dados

---

## Estrutura do Projeto

Exemplo simplificado da estrutura do projeto:

bot-invest/

dados/
dados_brutos_....csv
.
.
.

notebooks/
bot_v1.ipynb
software.py

scripts/
vfinal.py

Os dados históricos das ações são armazenados na pasta `data`.

---

## Como Executar o Projeto

1. Clone o repositório

```
git clone https://github.com/seu-usuario/bot-invest.git
```

2. Instale as dependências

```
pip install pandas yfinance matplotlib tabulate pathlib
```

3. Execute o script principal

```
python main.py
```

---

## Objetivo do Projeto

Este projeto foi desenvolvido com foco em aprendizado nas áreas de:

* automação com Python
* coleta e processamento de dados financeiros
* análise quantitativa
* desenvolvimento de sistemas para mercado financeiro

---

## Possíveis Melhorias Futuras

* Implementação de métricas adicionais (Sharpe Ratio, Drawdown)
* Sistema de backtesting
* Geração automática de relatórios
* Dashboard interativo para análise de dados
* Integração com outras fontes de dados
* Gerar recomendações de investimento
* Analisar noticias e dados recentes
