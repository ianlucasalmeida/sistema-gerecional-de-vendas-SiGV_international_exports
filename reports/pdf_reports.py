from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from database import obter_nome_loja

def gerar_nota_fiscal(dados):
    """
    Gera uma nota fiscal detalhada e bem formatada em PDF.
    
    Parâmetros:
    - dados: Dicionário contendo os dados da venda (id_comprador, id_vendedor, id_carro, valor_total).
    """
    # Obtém o nome da loja
    nome_loja = obter_nome_loja()

    # Define o nome do arquivo PDF
    nome_arquivo = f"Nota_Fiscal_Comprador_{dados['id_comprador']}.pdf"

    # Cria o documento PDF
    doc = SimpleDocTemplate(nome_arquivo, pagesize=letter)
    elementos = []

    # Estilos
    styles = getSampleStyleSheet()
    estilo_titulo = styles["Title"]
    estilo_normal = styles["Normal"]

    # Adiciona o cabeçalho da loja
    elementos.append(Paragraph(f"Loja: {nome_loja}", estilo_titulo))

    # Adiciona o título da nota fiscal
    elementos.append(Paragraph("Nota Fiscal", estilo_titulo))

    # Adiciona os detalhes da venda
    detalhes = [
        ["ID Comprador:", str(dados['id_comprador'])],
        ["ID Vendedor:", str(dados['id_vendedor'])],
        ["ID Carro:", str(dados['id_carro'])],
        ["Valor Total:", f"R$ {dados['valor_total']:.2f}"]
    ]

    # Cria a tabela
    tabela = Table(detalhes)

    # Estiliza a tabela
    estilo_tabela = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])

    tabela.setStyle(estilo_tabela)
    elementos.append(tabela)

    # Gera o PDF
    doc.build(elementos)