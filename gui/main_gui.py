import sys
import os

# Adiciona o diretório raiz do projeto ao caminho de busca do Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
from tkinter import ttk, messagebox
from entities.comprador import cadastrar_comprador, listar_compradores
from entities.vendedor import cadastrar_vendedor, listar_vendedores
from entities.carro import cadastrar_carro, listar_carros, buscar_carros_por_faixa_preco
from entities.venda_veiculo import cadastrar_venda, listar_vendas, gerar_relatorio_vendas_pdf
from seed import seed_database
from database import definir_nome_loja, obter_nome_loja

# Funções para Comprador
def cadastrar_comprador_gui():
    nome = entry_nome_comprador.get()
    cpf = entry_cpf_comprador.get()
    data_nascimento = entry_data_nascimento_comprador.get()
    resultado = cadastrar_comprador(nome, cpf, data_nascimento)
    messagebox.showinfo("Resultado", resultado)

def listar_compradores_gui():
    compradores = listar_compradores()
    lista_compradores.delete(0, tk.END)
    for comprador in compradores:
        lista_compradores.insert(tk.END, comprador)

# Funções para Vendedor
def cadastrar_vendedor_gui():
    nome = entry_nome_vendedor.get()
    cpf = entry_cpf_vendedor.get()
    data_nascimento = entry_data_nascimento_vendedor.get()
    resultado = cadastrar_vendedor(nome, cpf, data_nascimento)
    messagebox.showinfo("Resultado", resultado)

def listar_vendedores_gui():
    vendedores = listar_vendedores()
    lista_vendedores.delete(0, tk.END)
    for vendedor in vendedores:
        lista_vendedores.insert(tk.END, vendedor)

# Funções para Carro
def cadastrar_carro_gui():
    nome = entry_nome_carro.get()
    marca = entry_marca_carro.get()
    modelo = entry_modelo_carro.get()
    ano = entry_ano_carro.get()
    preco = entry_preco_carro.get()
    resultado = cadastrar_carro(nome, marca, modelo, int(ano), float(preco))
    messagebox.showinfo("Resultado", resultado)

def listar_carros_gui():
    carros = listar_carros()
    lista_carros.delete(0, tk.END)
    for carro in carros:
        lista_carros.insert(tk.END, carro)

# Funções para Venda
def calcular_valor_total(event):
    id_carro = combo_carro.get().split(" - ")[0]
    carros = listar_carros()
    for carro in carros:
        if str(carro[0]) == id_carro:
            entry_valor_total.delete(0, tk.END)
            entry_valor_total.insert(0, carro[5])  # Preço do carro
            break

def cadastrar_venda_gui():
    id_comprador = combo_comprador.get().split(" - ")[0]
    id_vendedor = combo_vendedor.get().split(" - ")[0]
    id_carro = combo_carro.get().split(" - ")[0]
    data_venda = entry_data_venda.get()
    valor_total = entry_valor_total.get()

    resultado = cadastrar_venda(id_comprador, id_vendedor, id_carro, data_venda, float(valor_total))
    messagebox.showinfo("Resultado", resultado)

def listar_vendas_gui():
    vendas = listar_vendas()
    lista_vendas.delete(0, tk.END)
    for venda in vendas:
        lista_vendas.insert(tk.END, venda)

def gerar_relatorios_gui():
    vendas = listar_vendas()
    resultado = gerar_relatorio_vendas_pdf(vendas)
    messagebox.showinfo("Resultado", resultado)

def configurar_nome_loja():
    nome_loja = entry_nome_loja.get()
    definir_nome_loja(nome_loja)
    messagebox.showinfo("Sucesso", "Nome da loja configurado com sucesso!")

# Interface Principal
root = tk.Tk()
root.title("Sistema de Loja")
root.geometry("800x600")

# Abas
notebook = ttk.Notebook(root)
aba_comprador = ttk.Frame(notebook)
aba_vendedor = ttk.Frame(notebook)
aba_carro = ttk.Frame(notebook)
aba_venda = ttk.Frame(notebook)
aba_busca = ttk.Frame(notebook)
aba_configuracoes = ttk.Frame(notebook)

notebook.add(aba_comprador, text="Comprador")
notebook.add(aba_vendedor, text="Vendedor")
notebook.add(aba_carro, text="Carro")
notebook.add(aba_venda, text="Venda")
notebook.add(aba_busca, text="Busca")
notebook.add(aba_configuracoes, text="Configurações")
notebook.pack(expand=True, fill="both")

# Interface para Comprador
tk.Label(aba_comprador, text="Nome").grid(row=0, column=0)
entry_nome_comprador = tk.Entry(aba_comprador)
entry_nome_comprador.grid(row=0, column=1)

tk.Label(aba_comprador, text="CPF").grid(row=1, column=0)
entry_cpf_comprador = tk.Entry(aba_comprador)
entry_cpf_comprador.grid(row=1, column=1)

tk.Label(aba_comprador, text="Data de Nascimento").grid(row=2, column=0)
entry_data_nascimento_comprador = tk.Entry(aba_comprador)
entry_data_nascimento_comprador.grid(row=2, column=1)

tk.Button(aba_comprador, text="Cadastrar", command=cadastrar_comprador_gui).grid(row=3, column=0)
tk.Button(aba_comprador, text="Listar", command=listar_compradores_gui).grid(row=3, column=1)

lista_compradores = tk.Listbox(aba_comprador, width=100, height=10)
lista_compradores.grid(row=4, column=0, columnspan=2)

# Interface para Vendedor
tk.Label(aba_vendedor, text="Nome").grid(row=0, column=0)
entry_nome_vendedor = tk.Entry(aba_vendedor)
entry_nome_vendedor.grid(row=0, column=1)

tk.Label(aba_vendedor, text="CPF").grid(row=1, column=0)
entry_cpf_vendedor = tk.Entry(aba_vendedor)
entry_cpf_vendedor.grid(row=1, column=1)

tk.Label(aba_vendedor, text="Data de Nascimento").grid(row=2, column=0)
entry_data_nascimento_vendedor = tk.Entry(aba_vendedor)
entry_data_nascimento_vendedor.grid(row=2, column=1)

tk.Button(aba_vendedor, text="Cadastrar", command=cadastrar_vendedor_gui).grid(row=3, column=0)
tk.Button(aba_vendedor, text="Listar", command=listar_vendedores_gui).grid(row=3, column=1)

lista_vendedores = tk.Listbox(aba_vendedor, width=100, height=10)
lista_vendedores.grid(row=4, column=0, columnspan=2)

# Interface para Carro
tk.Label(aba_carro, text="Nome").grid(row=0, column=0)
entry_nome_carro = tk.Entry(aba_carro)
entry_nome_carro.grid(row=0, column=1)

tk.Label(aba_carro, text="Marca").grid(row=1, column=0)
entry_marca_carro = tk.Entry(aba_carro)
entry_marca_carro.grid(row=1, column=1)

tk.Label(aba_carro, text="Modelo").grid(row=2, column=0)
entry_modelo_carro = tk.Entry(aba_carro)
entry_modelo_carro.grid(row=2, column=1)

tk.Label(aba_carro, text="Ano").grid(row=3, column=0)
entry_ano_carro = tk.Entry(aba_carro)
entry_ano_carro.grid(row=3, column=1)

tk.Label(aba_carro, text="Preço").grid(row=4, column=0)
entry_preco_carro = tk.Entry(aba_carro)
entry_preco_carro.grid(row=4, column=1)

tk.Button(aba_carro, text="Cadastrar", command=cadastrar_carro_gui).grid(row=5, column=0)
tk.Button(aba_carro, text="Listar", command=listar_carros_gui).grid(row=5, column=1)

lista_carros = tk.Listbox(aba_carro, width=100, height=10)
lista_carros.grid(row=6, column=0, columnspan=2)

# Interface para Venda
tk.Label(aba_venda, text="Comprador").grid(row=0, column=0)
combo_comprador = ttk.Combobox(aba_venda, state="readonly")
combo_comprador.grid(row=0, column=1)
combo_comprador['values'] = [f"{c[0]} - {c[2]}" for c in listar_compradores()]

tk.Label(aba_venda, text="Vendedor").grid(row=1, column=0)
combo_vendedor = ttk.Combobox(aba_venda, state="readonly")
combo_vendedor.grid(row=1, column=1)
combo_vendedor['values'] = [f"{v[0]} - {v[2]}" for v in listar_vendedores()]

tk.Label(aba_venda, text="Carro").grid(row=2, column=0)
combo_carro = ttk.Combobox(aba_venda, state="readonly")
combo_carro.grid(row=2, column=1)
combo_carro['values'] = [f"{car[0]} - {car[1]} ({car[5]:.2f})" for car in listar_carros()]
combo_carro.bind("<<ComboboxSelected>>", calcular_valor_total)

tk.Label(aba_venda, text="Data da Venda").grid(row=3, column=0)
entry_data_venda = tk.Entry(aba_venda)
entry_data_venda.grid(row=3, column=1)

tk.Label(aba_venda, text="Valor Total").grid(row=4, column=0)
entry_valor_total = tk.Entry(aba_venda)
entry_valor_total.grid(row=4, column=1)

tk.Button(aba_venda, text="Cadastrar Venda", command=cadastrar_venda_gui).grid(row=5, column=0)
tk.Button(aba_venda, text="Listar Vendas", command=listar_vendas_gui).grid(row=5, column=1)
tk.Button(aba_venda, text="Gerar Relatório", command=gerar_relatorios_gui).grid(row=6, column=0, columnspan=2)

lista_vendas = tk.Listbox(aba_venda, width=100, height=10)
lista_vendas.grid(row=7, column=0, columnspan=2)


# Interface para Configurações
tk.Label(aba_configuracoes, text="Nome da Loja").grid(row=0, column=0)
entry_nome_loja = tk.Entry(aba_configuracoes)
entry_nome_loja.grid(row=0, column=1)

tk.Button(aba_configuracoes, text="Salvar", command=configurar_nome_loja).grid(row=1, column=0, columnspan=2)

# Exibe o nome atual da loja
nome_loja_atual = obter_nome_loja()
tk.Label(aba_configuracoes, text=f"Nome Atual: {nome_loja_atual}").grid(row=2, column=0, columnspan=2)


# Botão para Popular o Banco de Dados
tk.Button(root, text="Popular Banco de Dados", command=seed_database).pack(side=tk.BOTTOM, pady=10)

root.mainloop()

    