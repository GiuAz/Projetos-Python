import json

class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def mostrarInformacoes(self):
        return f'Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}'

    def to_dict(self):
        return {"nome": self.nome, "telefone": self.telefone, "email": self.email}

    @staticmethod
    def from_dict(data):
        return Contato(data["nome"], data["telefone"], data["email"])

class Agenda:
    def __init__(self, arquivo="C:/Users/giuli/OneDrive/Área de Trabalho/Python/Aula 1/Projeto Classes/agenda.json"):
        self.arquivo = arquivo
        self.contatos = self.carregar_contatos()

    def carregar_contatos(self):
        try:
            with open(self.arquivo, "r") as file:
                contatos_data = json.load(file)
                return [Contato.from_dict(c) for c in contatos_data]
        except FileNotFoundError:
            return []

    def salvar_contatos(self):
        with open(self.arquivo, "w") as file:
            json.dump([c.to_dict() for c in self.contatos], file, indent=4)

    def addContato(self, contato):
        self.contatos.append(contato)
        self.salvar_contatos()

    def listarContato(self):
        self.contatos = self.carregar_contatos()  # Recarrega os contatos do arquivo
        if not self.contatos:
            print("Nenhum contato salvo.")
        else:
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
