from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle

def gerar_nota_fiscal(dados):
    """
    Gera uma nota fiscal em PDF com base nos dados fornecidos.
    
    Parâmetros:
    - dados: Dicionário contendo os dados da venda (id_comprador, id_vendedor, id_carro, valor_total).
    """
    # Define o nome do arquivo PDF
    nome_arquivo = f"Nota_Fiscal_{dados['id_comprador']}_{dados['id_venda']}.pdf"

    # Cria o documento PDF
    doc = SimpleDocTemplate(nome_arquivo, pagesize=letter)
    elementos = []

    # Estilos
    styles = getSampleStyleSheet()
    estilo_titulo = styles["Title"]
    estilo_normal = styles["Normal"]

    # Adiciona o título da nota fiscal
    elementos.append(Paragraph("Nota Fiscal", estilo_titulo))

    # Adiciona os detalhes da venda
    detalhes = [
        f"ID Comprador: {dados['id_comprador']}",
        f"ID Vendedor: {dados['id_vendedor']}",
        f"ID Carro: {dados['id_carro']}",
        f"Valor Total: R$ {dados['valor_total']:.2f}"
    ]

    for detalhe in detalhes:
        elementos.append(Paragraph(detalhe, estilo_normal))

    # Gera o PDF
    doc.build(elementos)