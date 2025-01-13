class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade

    def latir(self):
        print(f'{self.nome} diz au au!')
    def rosnar(self):
        print(f'{self.nome} rosnou para voce!')
    
cachorro1 = Cachorro("Scooby", 18)
cachorro2 = Cachorro("Thor", 4)

cachorro1.latir()
cachorro2.rosnar()