class Produto:
    def __init__(self, nome, codigo, preco, quantidade):
        self.nome = nome 
        self.codigo = codigo 
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f"Produto: {self.nome}, Codigo: {self.codigo}, Preco: {self.preco:.2f}, Quantidade: {self.quantidade}"
    
estoque = []

def registrarProduto(nome, codigo, preco, quantidade):
    produto = Produto(nome, codigo, preco, quantidade)
    estoque.append(produto)
    print(f"Produto{nome} registrado com sucesso!")

def listarProdutos():
    for produto in estoque:
        print(produto)

registrarProduto("Arroz", "P001", 5.99, 100)
registrarProduto("Feijao", "P002", 4.49, 50)

listarProdutos()

def atualizarEstoque(codigo, quantidade, operacao):
    produto = next((p for p in estoque if p.codigo == codigo), None)
    if produto:
        if operacao == 'adicionar':
            produto.quantidade += quantidade
            print(f"Adicionado {quantidade} unidades do produto {produto.nome}.")
        elif operacao == 'remover' and produto.quantidade >= quantidade:
            produto.quantidade -= quantidade
            print(f"Removido {quantidade} unidades do produto {produto.nome}.")
        else:
            print("Quantidade insuficiente no estoque ou operacao invalida.")
    else:
        print("Produto nao encontrado no estoque.")

atualizarEstoque("P001", 20, "adicionar")
atualizarEstoque("P002", 10, "remover")