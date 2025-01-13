class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def mostrarInformacoes(self):
        return f'Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}'

class Agenda:
    def __init__(self):
        self.contatos = []

    def addContato(self, contato):
        self.contatos.append(contato)

    def listarContato(self):
        for contato in self.contatos:
            print(contato.mostrarInformacoes())

def main():
    agenda = Agenda()

    while True:
        print("\n1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Sair")
        escolha = input("Escolha uma opcao: ")

        if escolha == '1':
           nome = input("Digite o nome: ")
           telefone = input("Digite o telefone: ")
           email = input("Digite o email: ")
           contato = Contato(nome, telefone, email)
           agenda.addContato(contato)
           print("Contato Adicionado com Sucesso!") 
        elif escolha == '2':
            print("\nLista de Contatos:")
            agenda.listarContato()
        elif escolha == '3':
            print("Voce Saiu!")
            break
        else:
            print("Opcao invalida. Tente novamente.")

if __name__ == "__main__":
    main()