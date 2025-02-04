from database import conectar_db

def cadastrar_carro(nome, marca, modelo, ano, preco):
    conn = conectar_db()
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO carro (nome, marca, modelo, ano, preco) VALUES (?, ?, ?, ?, ?)', (nome, marca, modelo, ano, preco))
        conn.commit()
        return "Carro cadastrado com sucesso!"
    except Exception as e:
        return str(e)
    finally:
        conn.close()

def listar_carros():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM carro')
    carros = cursor.fetchall()
    conn.close()
    return carros

def atualizar_carro(id_carro, nome=None, marca=None, modelo=None, ano=None, preco=None):
    conn = conectar_db()
    cursor = conn.cursor()
    try:
        if nome:
            cursor.execute('UPDATE carro SET nome = ? WHERE id_carro = ?', (nome, id_carro))
        if marca:
            cursor.execute('UPDATE carro SET marca = ? WHERE id_carro = ?', (marca, id_carro))
        if modelo:
            cursor.execute('UPDATE carro SET modelo = ? WHERE id_carro = ?', (modelo, id_carro))
        if ano:
            cursor.execute('UPDATE carro SET ano = ? WHERE id_carro = ?', (ano, id_carro))
        if preco:
            cursor.execute('UPDATE carro SET preco = ? WHERE id_carro = ?', (preco, id_carro))
        conn.commit()
        return "Carro atualizado com sucesso!"
    except Exception as e:
        return str(e)
    finally:
        conn.close()

def deletar_carro(id_carro):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM carro WHERE id_carro = ?', (id_carro,))
    conn.commit()
    conn.close()
    return "Carro deletado com sucesso!"

def buscar_carros_por_faixa_preco(preco_min, preco_max):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM carro WHERE preco BETWEEN ? AND ?', (preco_min, preco_max))
    carros = cursor.fetchall()
    conn.close()
    return carros