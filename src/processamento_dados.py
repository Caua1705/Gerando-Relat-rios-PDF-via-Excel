import pandas as pd
from pathlib import Path

# === Carregamento de Dados ===
def carregar_planilha():
    dir_raiz=Path(__file__).parents[1]
    caminho_planilha=dir_raiz / "dados" / "dados.xlsx"
    df=pd.read_excel(caminho_planilha)
    return df,dir_raiz

# === Filtro de Dados por mês ===
def filtrar_dados(df,mes_referencia):
    filtro=df["Data/Hora"].apply(lambda x:x.strftime("%Y-%m") == mes_referencia)
    df_filtrado=df.loc[filtro]
    return df_filtrado

## === Criação de Tabelas ===
def criacao_tabelas(df_filtrado):
    dados_venda=df_filtrado.pivot_table(index="Vendedor",
                                        columns="Produto",
                                        values="Quantidade",
                                        aggfunc="sum",
                                        margins=True,
                                        margins_name="Total").sort_values(by="Total")
    dados_volume=df_filtrado.pivot_table(index="Vendedor",
                                        columns="Produto",
                                        values="Valor Venda",
                                        aggfunc="sum",
                                        margins=True,
                                        margins_name="Total").sort_values(by="Total")
    ticket_medio=df_filtrado.groupby("Vendedor")[["Valor Venda"]].agg("mean")
    tabelas={"tabela_vendas":dados_venda,"tabela_volume":dados_volume,"tabela_ticket_medio":ticket_medio}
    return tabelas

