# - Criar Modos de Visualização: 
#   1 — Ranking de ações OK
#   2 — Análise de uma ação OK
#   3 — Backtest
#   4 — Portfólio do usuário
#   5 — Alertas
#   6 — Notícias
import os
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import yfinance as yf
from tabulate import tabulate
BASE_DIR = Path(__file__).resolve().parent
dados_path = BASE_DIR.parent / "dados"

dados_acoes = {}

for arquivo in dados_path.glob("dados_brutos_*.csv"):
    
    nome_acao = arquivo.stem.replace("dados_brutos_", "")
    
    dado = pd.read_csv(arquivo, header=1)
    
    dados_acoes[nome_acao] = dado


verde = "\033[92m"
vermelho = "\033[91m"
reset = "\033[0m"
acoes = ["PETR4","VALE3","ITUB4","BBDC4","BBAS3","WEGE3","LREN3","MGLU3","RAIL3","ABEV3"]
z = 0
b = 0
print(dados_path)
print(dados_path.resolve())
print(os.getcwd())
print(dados_acoes.keys())
for a in acoes:

    dados_old = dados_acoes[a]

    ultima_data = pd.to_datetime(dados_old.iloc[-1, 0]).normalize()
    
    hoje = pd.Timestamp.today().normalize()


    if ultima_data != hoje:

        novos = yf.download(f"{a}.SA", start=ultima_data)
        novos.columns = novos.columns.droplevel(1)
        novos.reset_index(inplace=True)
        if ultima_data != novos.iloc[0, 0].normalize():
            dados = pd.concat([dados_old, novos])

            dados = dados.drop_duplicates(subset= [dados.columns[0]])

            dados.to_csv(dados_path / f"dados_brutos_{a}.csv", index=False)
            dados_acoes[a] = dados
            print(f"{a} atualizado")
PETR4 = dados_acoes["PETR4"]
VALE3 = dados_acoes["VALE3"]
ITUB4 = dados_acoes["ITUB4"]
BBDC4 = dados_acoes["BBDC4"]
BBAS3 = dados_acoes["BBAS3"]
WEGE3 = dados_acoes["WEGE3"]
LREN3 = dados_acoes["LREN3"]
RAIL3 = dados_acoes["RAIL3"]
MGLU3 = dados_acoes["MGLU3"]
ABEV3 = dados_acoes["ABEV3"]


def c_p(valor):
    if valor > 0:
        return f"\033[92m+{valor:.2f}%\033[0m"
    elif valor < 0:
        return f"\033[91m{valor:.2f}%\033[0m"
    else:
        return f"{valor:.2f}%"

acoes_dados = [PETR4, VALE3, ITUB4, BBDC4, BBAS3, WEGE3, LREN3, MGLU3, RAIL3, ABEV3]
retornos_1m = []
retornos_6m = []
retornos_12m = []
volatilidades = []
momentums = []
scores = []
for dados in acoes_dados:
    r1 = ((dados.iloc[-1, 1] - dados.iloc[-21, 1]) / dados.iloc[-21, 1])
    r6 = ((dados.iloc[-1, 1] - dados.iloc[-126, 1]) / dados.iloc[-126, 1])
    r12 = ((dados.iloc[-1, 1] - dados.iloc[-252, 1]) / dados.iloc[-252, 1])
    v = dados.iloc[:, 1].pct_change().tail(252).std() * (252 ** 0.5)
    m = r12 - r1
    s = 0.35 * m + 0.30 * r6 + 0.25 * r12 - 0.10 * v
    retornos_1m.append(r1)
    retornos_6m.append(r6)
    retornos_12m.append(r12)
    volatilidades.append(v)
    momentums.append(m)
    scores.append(s)
d = {
"Ação": acoes,
"Retorno 1M": [f"{r*100:+.2f}%" for r in retornos_1m],
"Retorno 6M": [f"{r*100:+.2f}%" for r in retornos_6m],
"Retorno 12M": [f"{r*100:+.2f}%" for r in retornos_12m],
"Volatilidade": [f"{v*100:+.2f}%" for v in volatilidades],
"Momentum": [f"{m*100:+.2f}%" for m in momentums],
"Score": scores
}
df = pd.DataFrame(d)
df["Score"] = df["Score"].round(2)
ranking = df.sort_values(by="Score", ascending=False).reset_index(drop=True)



while z == 0:
    inicio = input("Digite o número do modo de visualização:"
    "1 — Ranking de ações\n"
    "2 — Análise de uma ação\n"
    "3 — Backtest\n"
    "4 — Portfólio do usuário\n"
    "5 — Alertas\n"
    "6 — Notícias\n"
    "0 - Sair\n")
    retornos_1m = []
    retornos_6m = []
    retornos_12m = []
    volatilidades = []
    momentums = []
    scores = []
    pms = []
    vars_ = []

    if inicio == "1":
        print("Ranking de ações")

        for dados in acoes_dados:
            va = ((dados.iloc[-1, 1] - dados.iloc[-2, 1])/ dados.iloc[-2, 1])
            pm = (dados.iloc[-1, 1])
            r1 = ((dados.iloc[-1, 1] - dados.iloc[-21, 1]) / dados.iloc[-21, 1])
            r6 = ((dados.iloc[-1, 1] - dados.iloc[-126, 1]) / dados.iloc[-126, 1])
            r12 = ((dados.iloc[-1, 1] - dados.iloc[-252, 1]) / dados.iloc[-252, 1])
            v = dados.iloc[:, 1].pct_change().tail(252).std() * (252 ** 0.5)
            m = r12 - r1
            s = 0.35 * m + 0.30 * r6 + 0.25 * r12 - 0.10 * v
            retornos_1m.append(r1)
            retornos_6m.append(r6)
            retornos_12m.append(r12)
            volatilidades.append(v)
            momentums.append(m)
            scores.append(s)
            pms.append(pm)
            vars_.append(va)
        d = {
        "Ação": acoes,
        "Preço Médio Atual": [f"{p:.2f}" for p in pms],
        "Variação Diária": [c_p(v*100)for v in vars_],
        "Retorno 1M": [c_p(r*100) for r in retornos_1m],
        "Retorno 6M": [c_p(r*100) for r in retornos_6m],
        "Retorno 12M": [c_p(r*100) for r in retornos_12m],
        "Volatilidade": [c_p(v*100) for v in volatilidades],
        "Momentum": [c_p(m*100) for m in momentums],
        "Score": scores
        }
        df = pd.DataFrame(d)
        df["Score"] = df["Score"].round(2)
        ranking = df.sort_values(by="Score", ascending=False).reset_index()
        top10 = ranking.head(10)
        choice = input("1 - Ranking Completo\n2 - Top 10\n")

        if choice == "1":
            print(tabulate(ranking, headers="keys", tablefmt="fancy_grid", numalign="center", stralign="center"))
            l = int(input("Gostaria de retornar ao menu? (1 - Sim, 0 - Sair)"))
            if l == 1:
                z = 0
            else:
                z = 1
        elif choice == "2":
            print(tabulate(top10, headers="keys", tablefmt="fancy_grid", numalign="center", stralign="center"))
            l = int(input("Gostaria de retornar ao menu? (1 - Sim, 0 - Sair)"))
            if l == 1:
                z = 0
            else:
                z = 1
        else:
            print("Opção inválida")
            z = 0
    elif inicio == "2":
        while True:
            print("Análise de uma ação")
            anal = input("Digite o nome da ação que deseja analisar (PETR4, VALE3, ITUB4, etc): ")
            if anal in acoes:
                print(f"Analisando a ação {anal}.SA")
                dados = pd.read_csv(dados_path / f"dados_brutos_{anal}.csv", header=1)
                preco = dados.iloc[-1, 1]
                r1 = ((dados.iloc[-1, 1] - dados.iloc[-21, 1]) / dados.iloc[-21, 1])
                r6 = ((dados.iloc[-1, 1] - dados.iloc[-126, 1]) / dados.iloc[-126, 1])
                r12 = ((dados.iloc[-1, 1] - dados.iloc[-252, 1]) / dados.iloc[-252, 1])
                v = dados.iloc[:, 1].pct_change().tail(252).std() * (252 ** 0.5)
                m = r12 - r1
                va = ((dados.iloc[-1, 1] - dados.iloc[-2, 1])/ dados.iloc[-2, 1])
                s = 0.35 * m + 0.30 * r6 + 0.25 * r12 - 0.10 * v
                print("" \
                f"""
    ==================================================
                {f"ANÁLISE DA AÇÃO — {anal}.SA":^26}
    ==================================================

    {f"Preço Médio Atual:":<30}{preco:.2f}R$
    {f"Variação Diária:":<30}{c_p(va * 100)}
    {f"Retorno 1M:":<30}{c_p(r1 * 100)}
    {f"Retorno 6M:":<30}{c_p(r6 * 100)}
    {f"Retorno 12M:":<30}{c_p(r12 * 100)}

    ---------------- RETORNOS ----------------

    {f"Volatilidade:":<30}{c_p(v*100)}
    {f"Momentum:":<30}{c_p(m*100)}
    {f"Score:":<30}{s:.2f}
    {f"Ranking:":<30}{ranking[ranking['Ação'] == anal].index[0] + 1}° lugar

    ---------------- ALERTAS ----------------



    ---------------- NOTÍCIAS ----------------



    ---------------- MODELO ----------------






    """)






                xs = pd.to_datetime(dados.iloc[:, 0])
                ys = dados.iloc[:, 1]
                plt.plot(xs, ys , color='blue')
                plt.xlabel("Tempo")
                plt.ylabel("Média do Preço")
                plt.title(f"Análise de Dados da Ação {anal}.SA")
                plt.show()
                k = int(input("Gostaria de analisar outra ação? (1 - Sim, 2 - Menu, 0 - Sair)"))
                if k == 1:
                    pass
                elif k == 0:
                    z = 1
                    break
                elif k == 2:
                    break
                else:
                    print("Opção inválida")
                    k = 0
            else:
                print("Ainda não temos dados dessa ação")
                k = int(input("Gostaria de tentar outra ação? (1 - Sim, 2 - Menu, 0 - Sair)"))
                if k == 1:
                    pass
                elif k == 0:
                    z = 1
                    break
                elif k == 2:
                    break
                else:
                    print("Opção inválida")
                    
    elif inicio == "3":
        print("Backtest")
    elif inicio == "4":
        print("Portfólio do usuário")
        ind = []
        actions = []
        retornos_1m = []
        retornos_6m = []
        retornos_12m = []
        volatilidades = []
        momentums = []
        scores = []
        pms = []
        vars_ = []

        while True:

            ac = input("Digite a ação (PETR4, VALE3, ITUB4, etc.):\n"
            "1 - Mostrar Portifólio\n"
            "0 - Sair ")
            
            if ac == "0":
                break

            elif ac == "1":
            
                for i in ind:
                    va = ((acoes_dados[ind.index(i)].iloc[-1, 1] - acoes_dados[ind.index(i)].iloc[-2, 1])/ acoes_dados[ind.index(i)].iloc[-2, 1])
                    pm = (acoes_dados[ind[i]].iloc[-1, 1])
                    r1 = ((acoes_dados[ind.index(i)].iloc[-1, 1] - acoes_dados[ind.index(i)].iloc[-21, 1]) / acoes_dados[ind.index(i)].iloc[-21, 1])
                    r6 = ((acoes_dados[ind.index(i)].iloc[-1, 1] - acoes_dados[ind.index(i)].iloc[-126, 1]) / acoes_dados[ind.index(i)].iloc[-126, 1])
                    r12 = ((acoes_dados[ind.index(i)].iloc[-1, 1] - acoes_dados[ind.index(i)].iloc[-252, 1]) / acoes_dados[ind.index(i)].iloc[-252, 1])
                    v = acoes_dados[ind.index(i)].iloc[:, 1].pct_change().tail(252).std() * (252 ** 0.5)
                    m = r12 - r1
                    s = 0.35 * m + 0.30 * r6 + 0.25 * r12 - 0.10 * v
                    retornos_1m.append(r1)
                    retornos_6m.append(r6)
                    retornos_12m.append(r12)
                    volatilidades.append(v)
                    momentums.append(m)
                    scores.append(s)
                    pms.append(pm)
                    vars_.append(va)
                    actions.append(acoes[i])
                pla = {
                "Ação": actions,
                "Preço Médio Atual": [f"{pm:.2f}" for pm in pms],
                "Variação Diária": [c_p(va * 100)for va in vars_],
                "Retorno 1M": [c_p(r * 100) for r in retornos_1m],
                "Retorno 6M": [c_p(r * 100) for r in retornos_6m],
                "Retorno 12M": [c_p(r * 100) for r in retornos_12m],
                "Volatilidade": [c_p(v * 100) for v in volatilidades],
                "Momentum": [c_p(m * 100) for m in momentums],
                "Score": scores
                }
                df2 = pd.DataFrame(pla)
                df2["Score"] = df2["Score"].round(2)
                print(tabulate(df2, headers = "keys", tablefmt="simple_grid", numalign="center", stralign="center"))
                break
            elif ac in acoes:
                ind.append(acoes.index(ac))
            else:
                print("Não Possuimos essa ação")
                pass


        
                
    elif inicio == "5":
        print("Alertas")
    elif inicio == "6":
        print("Notícias")
    elif inicio == "0":
        print("Encerrando o programa...")
        z = 1
    else:
        print("Opção inválida")
        z = 0
