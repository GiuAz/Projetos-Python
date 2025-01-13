class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def mostrarInfos(self):
        return f'Titulo: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}'

    @staticmethod
    def from_string(data):
        try:
            titulo, autor, ano = data.strip().split(', ')
            return Livro(titulo, autor, ano)
        except ValueError:
            print(f"Erro ao processar linha do arquivo: {data}")
            return None

import os

class Biblioteca:
    def __init__(self, nomeArquivo="biblioteca.txt"):
        # Use o caminho absoluto do arquivo
        self.nomeArquivo = os.path.abspath(nomeArquivo)
        self.livros = []
        self.carregarLivrosDoArquivo()

    def carregarLivrosDoArquivo(self):
        if not os.path.exists(self.nomeArquivo):
            print(f"O arquivo {self.nomeArquivo} não existe. Será criado ao salvar um livro.")
            open(self.nomeArquivo, 'w').close()  # Cria o arquivo vazio
            return

        try:
            with open(self.nomeArquivo, 'r') as arquivo:
                for linha in arquivo:
                    livro = Livro.from_string(linha)
                    if livro:  # Verifica se o livro foi criado corretamente
                        self.livros.append(livro)
        except Exception as e:
            print(f"Erro ao carregar livros: {e}")




    def addLivros(self, livro):
        self.livros.append(livro)
        self.salvarLivroNoArquivo(livro)

    def listarLivros(self):
        if not self.livros:
            print("Nenhum livro cadastrado.")
        else:
            for livro in self.livros:
                print(livro.mostrarInfos())

    def salvarLivroNoArquivo(self, livro):
        try:
            with open(self.nomeArquivo, 'a') as arquivo:  # Modo "append"
                arquivo.write(f'{livro.titulo}, {livro.autor}, {livro.ano}\n')
        except Exception as e:
            print(f"Erro ao salvar livro: {e}")

def main():
    biblioteca = Biblioteca()

    while True:
        print("\n1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Sair")
        escolha = input("Escolha uma opcao: ")

        if escolha == '1':
            titulo = input("Digite o Titulo do livro: ")
            autor = input("Digite o Autor do Livro: ")
            ano = input("Digite o Ano de Publicacao: ")
            livro = Livro(titulo, autor, ano)
            biblioteca.addLivros(livro)
            print("Livro adicionado com sucesso!")
        elif escolha == '2':
            print("\nLista de Livros:")
            biblioteca.listarLivros()
        elif escolha == '3':
            print("Voce saiu!")
            break
        else:
            print("Opcao invalida! Tente novamente.")

if __name__ == "__main__":
    main()
