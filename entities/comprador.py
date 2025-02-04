from database import conectar_db
from utils import validar_cpf

def cadastrar_comprador(nome, cpf, data_nascimento):
    conn = conectar_db()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO comprador (cpf, nome, data_nascimento)
            VALUES (?, ?, ?)
        ''', (cpf, nome, data_nascimento))
        conn.commit()
        return "Comprador cadastrado com sucesso!"
    except sqlite3.IntegrityError:
        return "Erro: CPF já cadastrado."
    finally:
        conn.close()

def listar_compradores():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM comprador')
    compradores = cursor.fetchall()
    conn.close()
    return compradores

def atualizar_comprador(id_comprador, nome=None, cpf=None, data_nascimento=None):
    conn = conectar_db()
    cursor = conn.cursor()
    try:
        if nome:
            cursor.execute('UPDATE comprador SET nome = ? WHERE id_comprador = ?', (nome, id_comprador))
        if cpf and validar_cpf(cpf):
            cursor.execute('UPDATE comprador SET cpf = ? WHERE id_comprador = ?', (cpf, id_comprador))
        if data_nascimento:
            cursor.execute('UPDATE comprador SET data_nascimento = ? WHERE id_comprador = ?', (data_nascimento, id_comprador))
        conn.commit()
        return "Comprador atualizado com sucesso!"
    except Exception as e:
        return str(e)
    finally:
        conn.close()

def deletar_comprador(id_comprador):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM comprador WHERE id_comprador = ?', (id_comprador,))
    conn.commit()
    conn.close()
    return "Comprador deletado com sucesso!"