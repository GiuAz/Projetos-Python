"""
Produto: Para representar os itens do menu. 
Pedido: Para gerenciar os pedidos.
Restaurante: Para gerenciar o menu e os pedidos.
"""

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def mostrarInfos(self):
        return f'Produto: {self.nome}, Preco: {self.preco}'
    
class Pedido:
    def __init__(self):
        self.itens = []

    def addProduto(self, produto):
        self.itens.append(produto)

    def calcularTotal(self):
        total = sum(produto.preco for produto in self.itens)
        return total
    
    def mostrarInfos(self):
        info = 'Itens do Pedido:\n'
        for produto in self.itens:
            info += f'- {produto.mostrarInfos()}\n'
        info += f'Total: R${self.calcularTotal():.2f}'
        return info
    
class Restaurante:
    def __init__(self):
        self.menu = []

    def addProdutoAoMenu(self, produto):
        self.menu.append(produto)

    def listarMenu(self):
        for produto in self.menu:
            print(produto.mostrarInfos())

    def criarPedido(self):
        return Pedido()
    
def main():
    restaurante = Restaurante()

    # Adicionando produtos ao menu
    restaurante.addProdutoAoMenu(Produto("Hamburguer", 15.50))
    restaurante.addProdutoAoMenu(Produto("Pizza", 25.00))
    restaurante.addProdutoAoMenu(Produto("Refrigerante", 5.00))
    restaurante.addProdutoAoMenu(Produto("Suco", 7.00))

    pedido = restaurante.criarPedido()

    while True:
        print("\n1. Mostrar menu")
        print("2. Adicionar Produto ao pedido")
        print("3. Mostrar o pedido e total")
        print("4. Sair")
        escolha = input("Escolha uma opcao: ")

        if escolha == '1':
            print("\nMenu:")
            restaurante.listarMenu()
        elif escolha == '2':
            nomeProduto = input("Digite o nome do produto que deseja adicionar ao pedido: ")
            for produto in restaurante.menu:
                if produto.nome.lower() == nomeProduto.lower():
                    pedido.addProduto(produto)
                    print(f"{produto.nome} adicionado ao pedido.")
                    break
            else:
                print("Produto não encontrado no menu.")
        elif escolha == '3':
            print("\nResumo do Pedido:")
            print(pedido.mostrarInfos())
        elif escolha == '4':
            print("Encerrando.")
            break
        else:
            print("Opcao invalida. Tente novamente.")

if __name__ == "__main__":
    main()