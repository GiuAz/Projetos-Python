import tkinter as tk

def aoClicar():
    texto = entrada.get()
    rotulo.config(text=texto)

janela = tk.Tk()
janela.title("Organização com Frames")
janela.geometry("600x300")

frameSuperior = tk.Frame(janela)
frameSuperior.pack()

frameInferior = tk.Frame(janela)
frameInferior.pack()

rotulo = tk.Label(frameSuperior, text="Digite algo e clique no botão")
rotulo.pack()

entrada = tk.Entry(frameSuperior)
entrada.pack()

botao = tk.Button(frameInferior, text="Clique Aqui", command=aoClicar)
botao.pack()

janela.mainloop()
