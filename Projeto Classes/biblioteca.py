class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def mostrarInfos(self):
        return f'Titulo: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}'
    
class Biblioteca:
    def __init__(self):
        self.livros = []

    def addLivros(self, livro):
        self.livros.append(livro)

    def listarLivros(self):
        for livro in self.livros:
            print(livro.mostrarInfos())

    def salvarLivrosEmArquivo(self, nomeArquivo):
        with open(nomeArquivo, 'w') as arquivo:
            for livro in self.livros:
                arquivo.write(f'{livro.titulo}, {livro.autor}, {livro.ano}\n')
        print(f'Livros salvos no arquivo {nomeArquivo} com sucesso!')

def main():
    biblioteca = Biblioteca()

    while True:
        print("\n1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Salvar Livros")
        print("4. Sair")
        escolha = input("Escolha uma opcao: ")

        if escolha == '1':
            titulo = input("Digite o Titulo do livro: ")
            autor = input("Digite o Autor do Livro: ")
            ano = input("Digite o ano de Publicacao: ")
            livro = Livro(titulo, autor, ano)
            biblioteca.addLivros(livro)
            print("Livro adicionado com Sucesso!")
        elif escolha == '2':
            print("\nLista de Livros:")
            biblioteca.listarLivros()
        elif escolha == '3':
            nomeArquivo = input("Digite o nome do arquivo para salvar os Livros: ")
            biblioteca.salvarLivrosEmArquivo(nomeArquivo)
        elif escolha == '4':
            print("Voce Saiu!")
            break
        else:
            print("Opcao Invalida! Tente novamente.")

if __name__ == "__main__":
    main()
