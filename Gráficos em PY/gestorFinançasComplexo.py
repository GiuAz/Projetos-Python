import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import os

root = tk.Tk()
root.title("Controle de Finanças")
root.geometry("500x600")

labelValor = tk.Label(root, text="Valor:")
labelValor.pack(pady=5)

entryValor = tk.Entry(root)
entryValor.pack(pady=5)

labelDescricao = tk.Label(root, text="Descrição:")
labelDescricao.pack(pady=5)

entryDescricao = tk.Entry(root)
entryDescricao.pack(pady=5)

buttonReceita = tk.Button(root, text="Adicionar Receita", command=lambda: addTransacao("Receita"))
buttonReceita.pack(pady=10)

buttonDespesa = tk.Button(root, text="Adicionar Despesa", command=lambda: addTransacao("Despesa"))
buttonDespesa.pack(pady=10)

buttonResumo = tk.Button(root, text="Exibir Resumo", command=lambda: exibirResumo())
buttonResumo.pack(pady=10)

buttonGrafico = tk.Button(root, text="Gerar Gráfico", command=lambda: gerarGrafico())
buttonGrafico.pack(pady=10)

transacoes = []

def addTransacao(tipo):
    try:
        valor = float(entryValor.get())
        descricao = entryDescricao.get()
        if not descricao:
            raise ValueError("Descrição Inválida")
    except ValueError as e:
        messagebox.showerror("Erro", f"Entrada Inválida: {e}")
        return
    
    transacao = {"tipo": tipo, "valor": valor, "descricao": descricao}
    transacoes.append(transacao)
    messagebox.showinfo("Sucesso", f"{tipo.capitalize()} adicionada com sucesso!")

    entryValor.delete(0, tk.END)
    entryDescricao.delete(0, tk.END)

def exibirResumo():
    totalReceitas = sum(t['valor'] for t in transacoes if t['tipo'] == 'Receita')
    totalDespesas = sum(t['valor'] for t in transacoes if t['tipo'] == 'Despesa')
    saldo = totalReceitas - totalDespesas

    resumo = f"Total de receitas: R$ {totalReceitas:.2f}\nTotal de despesas: R$ {totalDespesas:.2f}\nSaldo: R$ {saldo:.2f}"
    messagebox.showinfo("Resumo Financeiro", resumo)

def exibirHistorico():
    if not transacoes:
        messagebox.showinfo("Histórico", "Nenhuma transação registrada.")
        return

    historico = "Histórico de Transações:\n\n"
    for t in transacoes:
        historico += f"{t['tipo']}: R$ {t['valor']:.2f} - {t['descricao']}\n"

    messagebox.showinfo("Histórico de Transações", historico)

# Adiciona o botão para exibir o histórico
buttonHistorico = tk.Button(root, text="Exibir Histórico", command=exibirHistorico)
buttonHistorico.pack(pady=10)

def salvarEmExcel():
    if not transacoes:
        messagebox.showwarning("Aviso", "Nenhuma transação para salvar.")
        return

    # Abre uma janela para escolher a pasta
    pasta_destino = filedialog.askdirectory(title="Escolha a pasta para salvar o relatório")
    
    if not pasta_destino:  # Se o usuário cancelar, não faz nada
        return

    nome_arquivo = "relatorio_financeiro.xlsx"  # Nome fixo do arquivo
    caminho_completo = os.path.join(pasta_destino, nome_arquivo)  # Caminho completo

    # Verifica se o arquivo já existe
    if os.path.exists(caminho_completo):
        # Se o arquivo existe, carrega as transações existentes
        df_existente = pd.read_excel(caminho_completo)
        df_novas = pd.DataFrame(transacoes)  # Cria um DataFrame com as novas transações
        df_atualizado = pd.concat([df_existente, df_novas], ignore_index=True)  # Adiciona as novas transações
    else:
        # Se o arquivo não existe, cria um novo DataFrame
        df_atualizado = pd.DataFrame(transacoes)

    # Salva o arquivo com as transações acumuladas
    df_atualizado.to_excel(caminho_completo, index=False)

    messagebox.showinfo("Sucesso", f"Relatório salvo e atualizado em:\n{caminho_completo}")

# Adiciona o botão para salvar em Excel com escolha de pasta
buttonSalvarExcel = tk.Button(root, text="Salvar em Excel", command=salvarEmExcel)
buttonSalvarExcel.pack(pady=10)

def gerarGrafico():
    totalReceitas = sum(t['valor'] for t in transacoes if t['tipo'] == 'Receita')
    totalDespesas = sum(t['valor'] for t in transacoes if t['tipo'] == 'Despesa')

    if totalReceitas == 0 and totalDespesas == 0:
        messagebox.showwarning("Aviso", "Nenhuma transação registrada para gerar o gráfico.")
        return

    # Limpa a figura anterior para evitar sobreposição
    plt.clf()

    # Cria uma nova figura
    fig = plt.Figure(figsize=(5, 5))
    ax = fig.add_subplot(111)
    
    # Cria o gráfico de pizza
    ax.pie([totalReceitas, totalDespesas], labels=["Receitas", "Despesas"], autopct="%1.1f%%", startangle=90)
    ax.set_title("Proporção de Receitas e Despesas")

    # Remove gráficos antigos
    for widget in root.winfo_children():
        if isinstance(widget, FigureCanvasTkAgg):
            widget.get_tk_widget().destroy()

    # Cria o novo canvas com o gráfico
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Atualiza a interface para garantir que o gráfico apareça
    root.update_idletasks()

root.mainloop()