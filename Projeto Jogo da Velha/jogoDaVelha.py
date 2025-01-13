# Jogo da Velha

tabuleiro = [' ' for _ in range(9)]

def exibirTabuleiro():
    print()
    print(f' {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ')
    print('---|---|---')
    print(f' {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ')
    print('---|---|---')
    print(f' {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ')
    print()
    
def jogada(jogador):
    while True: 
        try:
            posicao = int(input(f'jogador {jogador}, escolha uma posicao entre 1 e 9: ')) - 1
            if posicao < 0 or posicao > 8:
                print("Posicao invalida! Escolha um numero de 1 a 9.")
            elif tabuleiro[posicao] != ' ':
                print("Posicao ja ocupada! Escolha outra.")
            else: 
                tabuleiro[posicao] = jogador
                break
        except ValueError:
            print("Entrada invalida! Por favor, insira um numero de 1 a 9.")

def verificarVitoria(jogador):
    combinacoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], #Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8], #Colunas
        [0, 4, 8], [2, 4, 6] # Diagonais
    ]
    for combinacao in combinacoes:
        if tabuleiro[combinacao[0]] == tabuleiro[combinacao[1]] == tabuleiro[combinacao[2]] == jogador:
            return True
        
    return False

def jogarJogo():
    jogadorAtual = 'X'
    for turno in range(9):
        exibirTabuleiro()
        jogada(jogadorAtual)
        if verificarVitoria(jogadorAtual):
            exibirTabuleiro()
            print(f'Jogador {jogadorAtual} venceu!')
            return
        jogadorAtual = 'O' if jogadorAtual == 'X' else 'X'
    exibirTabuleiro()
    print('Empate!')

jogarJogo()
