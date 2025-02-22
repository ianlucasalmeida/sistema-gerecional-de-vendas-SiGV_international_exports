from database import conectar_db
from reports.pdf_reports import gerar_nota_fiscal

def cadastrar_venda(id_comprador, id_vendedor, id_carro, data_venda, valor_total):
    conn = conectar_db()
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO venda_veiculo (id_comprador, id_vendedor, id_carro, data_venda, valor_total) VALUES (?, ?, ?, ?, ?)',
                       (id_comprador, id_vendedor, id_carro, data_venda, valor_total))
        conn.commit()
        return "Venda cadastrada com sucesso!"
    except Exception as e:
        return str(e)
    finally:
        conn.close()

def listar_vendas():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM venda_veiculo')
    vendas = cursor.fetchall()
    conn.close()
    return vendas

def gerar_relatorio_vendas_pdf(vendas):
    """
    Gera notas fiscais em PDF para cada venda na lista de vendas.
    
    Parâmetros:
    - vendas: Lista de tuplas contendo os dados das vendas.
    """
    for venda in vendas:
        # Cria um dicionário com os dados da venda
        nota_fiscal = {
            'id_comprador': venda[1],  # ID do comprador
            'id_vendedor': venda[2],  # ID do vendedor
            'id_carro': venda[3],     # ID do carro
            'valor_total': venda[5]   # Valor total da venda
        }
        # Gera a nota fiscal para esta venda
        gerar_nota_fiscal(nota_fiscal)
    
    return "Relatórios gerados com sucesso!"