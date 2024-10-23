import tkinter as tk
from tkinter import messagebox
from veiculo import Veiculo  # Importa a classe Veiculo

# Lista para armazenar os veículos
veiculos = []

# Função para adicionar veículo
def adicionar_veiculo():
    nome = entry_nome.get()
    ano = entry_ano.get()
    valor_diario = float(entry_valor_diario.get())
    tipo_combustivel = tipo_combustivel_var.get()
    cilindrada = entry_cilindrada.get()

    veiculo = Veiculo(nome, ano, valor_diario, tipo_combustivel, cilindrada)
    veiculos.append(veiculo)
    messagebox.showinfo("Sucesso", f"Veículo '{nome}' adicionado com sucesso!")

    # Limpar campos
    entry_nome.delete(0, tk.END)
    entry_ano.delete(0, tk.END)
    entry_valor_diario.delete(0, tk.END)
    entry_cilindrada.delete(0, tk.END)

# Função para calcular o aluguel
def calcular_aluguel():
    total_aluguel = sum(veiculo.valor_diario for veiculo in veiculos)
    messagebox.showinfo("Total de Aluguel", f"O total de aluguel para todos os veículos é: R$ {total_aluguel:.2f}")

# Interface Tkinter
root = tk.Tk()
root.title("Sistema de Gerenciamento de Veículos")

# Campos e botões da interface
tk.Label(root, text="Nome do Veículo:").grid(row=0, column=0)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1)

tk.Label(root, text="Ano do Veículo:").grid(row=1, column=0)
entry_ano = tk.Entry(root)
entry_ano.grid(row=1, column=1)

tk.Label(root, text="Valor Diário:").grid(row=2, column=0)
entry_valor_diario = tk.Entry(root)
entry_valor_diario.grid(row=2, column=1)

tk.Label(root, text="Tipo de Combustível:").grid(row=3, column=0)
tipo_combustivel_var = tk.StringVar(value="Gasolina")
tipos_combustiveis = ["Gasolina", "Álcool", "Diesel"]
tk.OptionMenu(root, tipo_combustivel_var, *tipos_combustiveis).grid(row=3, column=1)

tk.Label(root, text="Cilindrada:").grid(row=4, column=0)
entry_cilindrada = tk.Entry(root)
entry_cilindrada.grid(row=4, column=1)

tk.Button(root, text="Adicionar Veículo", command=adicionar_veiculo).grid(row=5, column=0)
tk.Button(root, text="Calcular Aluguel", command=calcular_aluguel).grid(row=5, column=1)

root.mainloop()

class Veiculo:
    def __init__(self, nome, ano, valor_diario, tipo_combustivel, cilindrada):
        self.nome = nome
        self.ano = ano
        self.valor_diario = valor_diario
        self.tipo_combustivel = tipo_combustivel
        self.cilindrada = cilindrada

from botcity.web import WebBot, Browser
import time

class Bot(WebBot):
    def action(self, execution=None):
        # Abrir a aplicação GUI
        self.execute("python3", "main.py")
        
        # Esperar a aplicação abrir
        time.sleep(2)

        # Preencher dados do veículo
        veiculos = [
            {"nome": "Fusca", "ano": "1970", "valor_diario": "100", "tipo_combustivel": "Gasolina", "cilindrada": "1300"},
            {"nome": "Civic", "ano": "2020", "valor_diario": "150", "tipo_combustivel": "Álcool", "cilindrada": "1600"}
        ]

        for veiculo in veiculos:
            self.find("input_nome", matching=0.97)
            self.click()
            self.paste(veiculo["nome"])  # Nome do veículo
            
            self.find("input_ano", matching=0.97)
            self.click()
            self.paste(veiculo["ano"])  # Ano do veículo
            
            self.find("input_valor_diario", matching=0.97)
            self.click()
            self.paste(veiculo["valor_diario"])  # Valor diário
            
            self.find("select_combustivel", matching=0.97)
            self.click()
            self.paste(veiculo["tipo_combustivel"])  # Tipo de combustível
            
            self.find("input_cilindrada", matching=0.97)
            self.click()
            self.paste(veiculo["cilindrada"])  # Cilindrada
            
            self.find("btn_adicionar", matching=0.97)
            self.click()  # Clicar no botão Adicionar Veículo

            time.sleep(1)  # Pausar para garantir que o veículo seja adicionado

        # Calcular aluguel
        self.find("btn_calcular", matching=0.97)
        self.click()  # Clicar no botão Calcular Aluguel

    def not_found(self, label):
        print(f"Elemento {label} não encontrado.")

