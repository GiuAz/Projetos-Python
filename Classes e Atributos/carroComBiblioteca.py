from datetime import datetime

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo 
        self.ano = ano

    def info(self):
        return f'Carro: {self.marca}, Modelo: {self.modelo}, Ano:{self.ano}'
    
    def idadeCarro(self):
        anoAtual = datetime.now().year
        return anoAtual - self.ano

carro1 = Carro("Toyota", "Corolla", 2020) 
carro2 = Carro("Honda", "Civic", 2019)

print(carro1.info(), carro1.idadeCarro())
print(carro2.info(), carro2.idadeCarro())