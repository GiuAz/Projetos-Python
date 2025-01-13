import tkinter as tk

#Comando para o botão.
def aoClicar():
    texto = entrada.get()
    rotulo.config(text=texto)

#Criar Janela Principal
janela = tk.Tk()
janela.title("Minha primeira janela")
janela.geometry("300x200")

#Criar um rotulo
rotulo = tk.Label(janela, text="Olá mundo")
rotulo.pack()

entrada = tk.Entry(janela)
entrada.pack()

#Criar um botão
botao = tk.Button(janela, text="Clique Aqui", command=aoClicar)
botao.pack()

#Executar a aplicação
janela.mainloop()