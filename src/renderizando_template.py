import processamento_dados 
from jinja2 import FileSystemLoader,Environment
import datetime
import locale
locale.setlocale(locale.LC_ALL,"pt_BR.UTF-8")

#Procesamento de dados:
mes_referencia="2023-01"
df,dir_raiz=processamento_dados.carregar_planilha()
df_filtrado=processamento_dados.filtrar_dados(df,mes_referencia)
tabelas=processamento_dados.criacao_tabelas(df_filtrado)

#Carregando Template:
pasta_template= dir_raiz / "templates" 
carregamento_pasta=FileSystemLoader(pasta_template)
env=Environment(loader=carregamento_pasta)
template=env.get_template("template.jinja")

#Definindo variáveis para renderizar o template:
agora=datetime.datetime.now()

variaveis_template={
    "stylesheet":"",
    "mes_referencia": mes_referencia,
    "dia": agora.strftime("%d-%m-%Y"),
    "hora":agora.strftime("%H:%M"),
}

#Função para formatar tabelas:
def formatar_valor(valor):
    return locale.currency(valor,grouping=True)

#Adicionando tabelas formatadas e convertidas em html para o dicionário variaveis_template:
for nome_tabela,tabela in tabelas.items():
    variaveis_template[nome_tabela]=tabela.to_html(float_format=formatar_valor)

#Adicionando o css ao stylesheet no dicionário:
caminho_css= dir_raiz / "templates" / "tabelas_estilizadas.css"
with open(caminho_css,mode="r") as style:                                               
    css= style.read()
variaveis_template["stylesheet"]=css

template_renderizado=template.render(**variaveis_template)




