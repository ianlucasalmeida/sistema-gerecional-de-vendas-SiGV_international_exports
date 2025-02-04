from database import conectar_db
from utils import validar_cpf

def cadastrar_vendedor(nome, cpf, data_nascimento):
    """
    Cadastra um novo vendedor no banco de dados.
    
    Parâmetros:
    - nome: Nome do vendedor.
    - cpf: CPF do vendedor.
    - data_nascimento: Data de nascimento do vendedor.
    
    Retorna:
    - Uma mensagem indicando sucesso ou falha no cadastro.
    """
    conn = conectar_db()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO vendedor (cpf, nome, data_nascimento)
            VALUES (?, ?, ?)
        ''', (cpf, nome, data_nascimento))
        conn.commit()
        return "Vendedor cadastrado com sucesso!"
    except Exception as e:
        conn.rollback()
        return f"Erro ao cadastrar vendedor: {str(e)}"
    finally:
        conn.close()

def listar_vendedores():
    """
    Lista todos os vendedores cadastrados no banco de dados.
    
    Retorna:
    - Uma lista de tuplas contendo os dados dos vendedores.
    """
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM vendedor')
    vendedores = cursor.fetchall()
    conn.close()
    return vendedores

def listar_vendedores():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM vendedor')
    vendedores = cursor.fetchall()
    conn.close()
    return vendedores

def atualizar_vendedor(id_vendedor, nome=None, cpf=None, data_nascimento=None):
    conn = conectar_db()
    cursor = conn.cursor()
    try:
        if nome:
            cursor.execute('UPDATE vendedor SET nome = ? WHERE id_vendedor = ?', (nome, id_vendedor))
        if cpf and validar_cpf(cpf):
            cursor.execute('UPDATE vendedor SET cpf = ? WHERE id_vendedor = ?', (cpf, id_vendedor))
        if data_nascimento:
            cursor.execute('UPDATE vendedor SET data_nascimento = ? WHERE id_vendedor = ?', (data_nascimento, id_vendedor))
        conn.commit()
        return "Vendedor atualizado com sucesso!"
    except Exception as e:
        return str(e)
    finally:
        conn.close()

def deletar_vendedor(id_vendedor):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM vendedor WHERE id_vendedor = ?', (id_vendedor,))
    conn.commit()
    conn.close()
    return "Vendedor deletado com sucesso!"