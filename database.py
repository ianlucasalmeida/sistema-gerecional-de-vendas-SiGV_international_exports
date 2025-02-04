import sqlite3

# Conexão com o banco de dados
def conectar_db():
    conn = sqlite3.connect('loja.db')
    return conn

# Criação das tabelas
def criar_tabelas():
    conn = conectar_db()
    cursor = conn.cursor()

    # Tabela Comprador
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comprador (
            id_comprador INTEGER PRIMARY KEY AUTOINCREMENT,
            cpf TEXT UNIQUE NOT NULL,
            nome TEXT NOT NULL,
            data_nascimento TEXT NOT NULL
        )
    ''')

    # Tabela Vendedor
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vendedor (
            id_vendedor INTEGER PRIMARY KEY AUTOINCREMENT,
            cpf TEXT UNIQUE NOT NULL,
            nome TEXT NOT NULL,
            data_nascimento TEXT NOT NULL
        )
    ''')

    # Tabela Carro
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS carro (
            id_carro INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            marca TEXT NOT NULL,
            modelo TEXT NOT NULL,
            ano INTEGER NOT NULL,
            preco REAL NOT NULL
        )
    ''')

    # Tabela Venda Veículo
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS venda_veiculo (
            id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
            id_comprador INTEGER NOT NULL,
            id_vendedor INTEGER NOT NULL,
            id_carro INTEGER NOT NULL,
            data_venda TEXT NOT NULL,
            valor_total REAL NOT NULL,
            FOREIGN KEY (id_comprador) REFERENCES comprador (id_comprador),
            FOREIGN KEY (id_vendedor) REFERENCES vendedor (id_vendedor),
            FOREIGN KEY (id_carro) REFERENCES carro (id_carro)
        )
    ''')

    # Tabela Configuração (Nome da Loja)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS configuracao (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_loja TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

# Função para definir o nome da loja
def definir_nome_loja(nome_loja):
    conn = conectar_db()
    cursor = conn.cursor()

    # Verifica se já existe um registro na tabela configuracao
    cursor.execute('SELECT COUNT(*) FROM configuracao')
    if cursor.fetchone()[0] == 0:
        cursor.execute('INSERT INTO configuracao (nome_loja) VALUES (?)', (nome_loja,))
    else:
        cursor.execute('UPDATE configuracao SET nome_loja = ?', (nome_loja,))

    conn.commit()
    conn.close()

# Função para obter o nome da loja
def obter_nome_loja():
    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute('SELECT nome_loja FROM configuracao')
    resultado = cursor.fetchone()
    conn.close()

    return resultado[0] if resultado else "Loja Não Configurada"

# Função para reiniciar o banco de dados
def reiniciar_banco():
    conn = conectar_db()
    cursor = conn.cursor()

    # Pergunta ao usuário se deseja reiniciar o banco de dados
    resposta = input("Deseja reiniciar o banco de dados? Isso apagará todos os dados existentes. (s/n): ").lower()
    if resposta == 's':
        cursor.execute('DROP TABLE IF EXISTS comprador')
        cursor.execute('DROP TABLE IF EXISTS vendedor')
        cursor.execute('DROP TABLE IF EXISTS carro')
        cursor.execute('DROP TABLE IF EXISTS venda_veiculo')
        cursor.execute('DROP TABLE IF EXISTS configuracao')
        print("Banco de dados reiniciado com sucesso!")
    else:
        print("Operação cancelada.")
    
    conn.commit()
    conn.close()

# Inicialização do banco de dados
if __name__ == "__main__":
    criar_tabelas()
    reiniciar_banco()

# Inicialização do banco de dados
if __name__ == "__main__":
    criar_tabelas()