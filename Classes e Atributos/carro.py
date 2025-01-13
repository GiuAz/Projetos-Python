class Carro:
    # Método inicializador (__init__) é chamado quando uma nova instância de classe é criada
    def __init__(self, marca, modelo, ano):
        self.marca = marca # Atributo marca da instância recebe o valor passado ao criar o objeto
        self.modelo = modelo # Atributo modelo da instância recebe o valor passado ao criar o objeto
        self.ano = ano # Atributo ano da instância recebe o valor passado ao criar o objeto

    # Método para exibir as informações do carro
    def exibirInformacoes(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}')

    # Método para calcular a idade do carro com base no ano atual
    def calcularIdade(self, anoAtual):
        return anoAtual - self.ano
    
# Criando Objetos
carro1 = Carro("Toyota", "Corolla", 2015) #Cria uma instância na classe Carro com marca 'Toyota', modelo 'Corolla' e ano '2015'
carro2 = Carro("Honda", "Civic", 2018) #Cria uma instância na classe Carro com marca 'Honda', modelo 'Civic' e ano '2018'

carro1.exibirInformacoes() #Chamo o método exibirInformacoes da instância carro1 
carro2.exibirInformacoes() #Chamo o método exibirInformacoes da instância carro2

# Calcula a idade dos carros usando o método calcularIdade
print(f'Idade do carro 1: {carro1.calcularIdade(2024)} anos')
print(f'Idade do carro 1: {carro2.calcularIdade(2024)} anos')