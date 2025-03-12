import tkinter as tk
from tkinter import messagebox
import random

# Criando a janela principal
root = tk.Tk()
root.title("Jogo da Memória")
root.geometry("850x1000")

# Lista de símbolos (8 pares diferentes)
simbolos_base = ["♥", "★", "☀", "☁", "🍀", "🦊", "🐍", "🎵"]

# Variáveis globais
botoes = []  # Armazena os botões para reinicializar
primeiroCartao = None
segundoCartao = None
paresEncontrados = 0
reiniciar_button = None  # Botão de reinício

def iniciarJogo():
    """Inicializa o jogo embaralhando os símbolos e criando os botões"""
    global simbolos, primeiroCartao, segundoCartao, paresEncontrados, botoes, reiniciar_button

    # Resetando variáveis
    primeiroCartao = None
    segundoCartao = None
    paresEncontrados = 0
    simbolos = simbolos_base * 2  # Criando os pares
    random.shuffle(simbolos)  # Embaralhando

    # Limpando os botões antigos
    if botoes:
        for linha in botoes:
            for botao in linha:
                botao.destroy()
        botoes.clear()

    # Criando a grade de botões (4x4)
    for i in range(4):
        linha = []
        for j in range(4):
            simbolo = simbolos.pop()
            botao = criarCartao(root, simbolo, i, j)
            linha.append(botao)
        botoes.append(linha)

    # Removendo o botão de reinício, se existir
    if reiniciar_button:
        reiniciar_button.destroy()

def criarCartao(parent, simbolo, row, col):
    """Cria um botão representando um cartão"""
    button = tk.Button(parent, text="?", width=10, height=5, font=("Arial", 24, "bold"), 
                       command=lambda: revelarCartao(button, simbolo))
    button.grid(row=row, column=col, padx=5, pady=5)
    return button

def revelarCartao(button, simbolo):
    """Mostra o símbolo do cartão ao ser clicado"""
    global primeiroCartao, segundoCartao

    if button["text"] == "?" and segundoCartao is None:
        button.config(text=simbolo)

        if primeiroCartao is None:
            primeiroCartao = (button, simbolo)
        else:
            segundoCartao = (button, simbolo)
            root.after(1000, verificarPares)

def verificarPares():
    """Verifica se os cartões são iguais e desativa se forem pares"""
    global primeiroCartao, segundoCartao, paresEncontrados

    if primeiroCartao and segundoCartao:
        botao1, simbolo1 = primeiroCartao
        botao2, simbolo2 = segundoCartao

        if simbolo1 == simbolo2:
            botao1.config(state="disabled", bg="green")  # Muda a cor para verde
            botao2.config(state="disabled", bg="green")
            paresEncontrados += 1
        else:
            botao1.config(text="?")
            botao2.config(text="?")

    # Reseta as variáveis para o próximo par
    primeiroCartao = None
    segundoCartao = None

    # Verifica se o jogo foi concluído
    if paresEncontrados == 8:
        messagebox.showinfo("Parabéns!", "Você venceu!")
        adicionarBotaoReiniciar()

def adicionarBotaoReiniciar():
    """Adiciona um botão para reiniciar o jogo após a vitória"""
    global reiniciar_button
    reiniciar_button = tk.Button(root, text="Reiniciar Jogo", font=("Arial", 16, "bold"), bg="blue", fg="white",
                                 command=iniciarJogo)
    reiniciar_button.grid(row=4, column=0, columnspan=4, pady=20)  # Centralizando abaixo do jogo

# Iniciar o jogo
iniciarJogo()

# Executando a interface gráfica
root.mainloop()

