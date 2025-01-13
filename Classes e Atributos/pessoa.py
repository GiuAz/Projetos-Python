class Pessoa:
    # Método inicializador (__init__) é chamado quando uma nova instância de classe é criada
    def __init__(self, nome, idade):
        self.nome = nome # Atributo nome da instância recebe o valor passado ao criar o objeto
        self.idade = idade # Atributo idade da instância recebe o valor passado ao criar o objeto

    # Método para exibir informações de pessoa
    def exibirInformacoes(self):
        print(f'Nome: {self.nome}, Idade: {self.idade}')

# Criando objetos
pessoa1 = Pessoa("Alice", 30) # Cria uma instância da classe Pessoa com nome 'Alice' e idade 30
pessoa2 = Pessoa("Bob", 25) #Cria uma instância da classe Pessoa com nome 'Bob' e idade 25

pessoa1.exibirInformacoes() # Chama o método exibirInformacoes da instância pessoa1 
pessoa2.exibirInformacoes() # Chama o método exibirInformacoes da instância pessoa2

