class Membro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.treinos = []

    def addTreino(self, treino):
        self.treinos.append(treino)
    
    def mostrarInfos(self):
        info = f'Nome: {self.nome}, Idade: {self.idade}\nTreinos:'
        for treino in self.treinos:
            info += f'\n- {treino.descricao}'
        return info
    
class Treino:
    def __init__(self, descricao, duracao, data):
        self.descricao = descricao
        self.duracao = duracao
        self.data = data 

    def mostrarInfos(self):
        return f'Descricao: {self.descricao}, Duracao: {self.duracao}, Data: {self.data}'
    
class Academia:
    def __init__(self):
        self.membros = []

    def addMembro(self, membro):
        self.membros.append(membro)

    def listarMembros(self):
        for membro in self.membros:
            print(membro.mostrarInfos())

    def salvarMembrosEmArquivo(self, nomeArquivo):
        with open(nomeArquivo, 'w') as arquivo:
            for membro in self.membros:
                arquivo.write(f'{membro.nome}, {membro.idade}\n')
                for treino in membro.treinos:
                    arquivo.write(f'{treino.descricao}, {treino.duracao}, {treino.data}\n')
        print(f'Membros e treinos salvos no arquivo {nomeArquivo} com sucesso!')

def main():
    academia = Academia()

    while True:
        print("\n1. Adicionar Membro")
        print("2. Adicionar Treino ao Membro")
        print("3. Listar Membros e Treinos")
        print("4. Salvar Membros e Treinos")
        print("5. Sair")
        escolha = input("Escolha uma opcao: ")

        if escolha == '1':
            nome = input("Digite o nome do membro: ")
            idade = input("Digite a idade do membro: ")
            membro = Membro(nome, idade)
            academia.addMembro(membro)
            print("Membro adicionado com sucesso!")
        elif escolha == '2':
            nome = input("Digite o nome do Membro para add treino: ")
            for membro in academia.membros:
                if membro.nome == nome:
                    descricao = input("Digite a descricao do treino: ")
                    duracao = input("Digite a duracao do treino: ")
                    data = input("Digite a data do treino: ")
                    treino = Treino(descricao, duracao, data)
                    membro.addTreino(treino)
                    print("Treino adicionado com sucesso!")
                    break
            else:
                print("Membro nao encontrado.")
        elif escolha == '3':
            print("\nLista de Membros e Treinos:")
            academia.listarMembros()
        elif escolha == '4':
            nomeArquivo = input("Digite o nome do arquivo para salvar: ")
            academia.salvarMembrosEmArquivo(nomeArquivo)
        elif escolha == '5':
            print("Encerrado.")
            break 
        else:
            print("Opcao invalida. Tente novamente.")

if __name__ == "__main__":
    main()