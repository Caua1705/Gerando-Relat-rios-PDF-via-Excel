import pdfkit
from renderizando_template import mes_referencia,dir_raiz,template_renderizado

#Criação do pdf:
def criacao_pdf(mes_referencia,template_renderizado,dir_raiz):
    nome_relatorio=f"Relatório Mensal - {mes_referencia}.pdf"
    caminho_relatorio=dir_raiz / "output" / nome_relatorio
    caminho_relatorio.parent.mkdir(exist_ok=True)
    config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
    pdfkit.from_string(template_renderizado,output_path=caminho_relatorio,configuration=config)
    return caminho_relatorio

#Adicionando o layout ao pdf:
import pypdf
caminho_relatorio=criacao_pdf(mes_referencia,template_renderizado,dir_raiz)

pagina_conteudo=pypdf.PdfReader(caminho_relatorio).pages[0]
pagina_layout=pypdf.PdfReader(dir_raiz / "templates" / "layout_relatorio.pdf").pages[0]
pagina_conteudo.merge_page(pagina_layout,over=True)

escritor_pdf=pypdf.PdfWriter()
escritor_pdf.add_page(pagina_conteudo)
escritor_pdf.write(caminho_relatorio)
