import tkinter as tk

def addTexto(numero):

    entrada.insert(tk.END, numero)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    
    except:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")

def limpar():
    entrada.delete(0, tk.END)

janela = tk.Tk()

janela.title("Calculadora")
janela.geometry("400x400")

entrada = tk.Entry(janela, width=20, font=("Arial", 24), borderwidth=2, relief="solid")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

numeros = [
('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
('0', 4, 1)
]

for (texto, linha, coluna) in numeros:
    botao = tk.Button(janela, text=texto, width=5, height=2, font=("Arial", 18), 
    command=lambda t=texto: addTexto(t))

    botao.grid(row=linha, column=coluna, padx=5, pady=5)

    operacoes = [
        ('+', 1, 3), ('-', 2, 3),
        ('*', 3, 3), ('/', 4, 3),
        ('=', 4, 2), ('C', 4, 0)
    ]

for (texto, linha, coluna) in operacoes:
    if texto == '=':
        botao = tk.Button(janela, text=texto, width=5, height=2, font=("Arial", 18), command=calcular)

    elif texto == 'C':
        botao = tk.Button(janela, text=texto, width=5, height=2, font=("Arial", 18), command=limpar)

    else: 
        botao = tk.Button(janela, text=texto, width=5, height=2, font=("Arial", 18), 
                          command=lambda t=texto: addTexto(t))
    botao.grid(row=linha, column=coluna, padx=5, pady=5)

janela.mainloop()