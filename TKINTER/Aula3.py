import tkinter as tk

def addTarefa():
    tarefa = entrada.get()
    if tarefa != "":
        listaTarefas.insert(tk.END, tarefa)
        entrada.delete(0, tk.END)

def removerTarefa():
    try:
        indiceSelecionado = listaTarefas.curselection()[0]
        listaTarefas.delete(indiceSelecionado)
    except:
        pass

janela = tk.Tk()
janela.title("Lista de Tarefas")
janela.geometry("900x400")

frameSuperior = tk.Frame(janela)
frameSuperior.pack(pady=10)

frameInferior = tk.Frame(janela)
frameInferior.pack(pady=10)

rotulo = tk.Label(frameSuperior, text="Digite uma Tarefa e clique em 'Adicionar'")
rotulo.pack()

entrada = tk.Entry(frameSuperior, width=40)
entrada.pack()

botaoAdicionar = tk.Button(frameSuperior, text="Adicionar", command=addTarefa)
botaoAdicionar.pack(pady=5)

listaTarefas = tk.Listbox(frameInferior, width=50, height=10)
listaTarefas.pack()

botaoRemover = tk.Button(frameInferior, text="Remover", command=removerTarefa)
botaoRemover.pack(pady=5)

janela.mainloop()