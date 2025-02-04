from database import conectar_db
from entities.comprador import cadastrar_comprador
from entities.vendedor import cadastrar_vendedor
from entities.carro import cadastrar_carro

def seed_database():
    conn = conectar_db()
    cursor = conn.cursor()

    # Verifica se já existem dados no banco para evitar duplicação
    cursor.execute('SELECT COUNT(*) FROM comprador')
    if cursor.fetchone()[0] > 0:
        print("O banco de dados já foi populado. Encerrando seeding.")
        conn.close()
        return

    # Cadastrar Compradores
    compradores = [
        ("João Silva", "123.456.789-00", "1990-01-15"),
        ("Maria Souza", "987.654.321-00", "1985-05-20"),
        ("Pedro Almeida", "456.789.123-00", "1995-08-10")
    ]
    for nome, cpf, data_nascimento in compradores:
        cadastrar_comprador(nome, cpf, data_nascimento)

    # Cadastrar Vendedores
    vendedores = [
        ("Carlos Mendes", "321.654.987-00", "1980-03-12"),
        ("Ana Paula", "654.321.987-00", "1975-07-25"),
        ("Roberto Lima", "789.123.456-00", "1988-11-30"),
        ("Juliana Santos", "111.222.333-44", "1990-05-15"),
        ("Marcos Almeida", "222.333.444-55", "1982-09-20"),
        ("Fernanda Costa", "333.444.555-66", "1978-12-05"),
        ("Rafael Silva", "444.555.666-77", "1995-02-10"),
        ("Camila Oliveira", "555.666.777-88", "1987-06-22"),
        ("Lucas Pereira", "666.777.888-99", "1983-08-14"),
        ("Patrícia Souza", "777.888.999-00", "1979-04-18")
    ]
    for nome, cpf, data_nascimento in vendedores:
        cadastrar_vendedor(nome, cpf, data_nascimento)

    # Cadastrar Carros
    carros = [
        ("Fiesta", "Ford", "Hatch", 2018, 45000.00),
        ("Civic", "Honda", "Sedan", 2020, 85000.00),
        ("Corolla", "Toyota", "Sedan", 2019, 90000.00),
        ("Gol", "Volkswagen", "Hatch", 2017, 35000.00),
        ("Onix", "Chevrolet", "Hatch", 2021, 55000.00),
        ("HB20", "Hyundai", "Hatch", 2019, 60000.00),
        ("Renegade", "Jeep", "SUV", 2022, 120000.00),
        ("Compass", "Jeep", "SUV", 2021, 150000.00),
        ("T-Cross", "Volkswagen", "SUV", 2020, 110000.00),
        ("Kwid", "Renault", "Hatch", 2018, 40000.00)
    ]
    for nome, marca, modelo, ano, preco in carros:
        cadastrar_carro(nome, marca, modelo, ano, preco)

    print("Banco de dados populado com sucesso!")
    conn.close()

if __name__ == "__main__":
    seed_database()