def cadastrarCliente(nome, email, telefone):
    with open("clientes.txt", "a") as arquivo:
        arquivo.write(f"{nome}, {email}, {telefone}\n")
    print("Cliente cadastrado com sucesso!")

def listarClientes():
    try:
        with open("clientes.txt", "r") as arquivo:
            clientes = arquivo.readlines()
            if not clientes: 
                print("Nenhum cliente encontrado.")
            else:
                print("Lista de clientes cadastrados: ")
                for cliente in clientes:
                    nome, email, telefone = cliente.strip().split(",")
                    print (f"Nome: {nome}, E-mail: {email}, Telefone {telefone}")
    except FileNotFoundError:
        print ("Nenhum cliente cadastrado.")

# Manipulação do arquivo 
def salvarEmArquivo(dados, nomeArquivo):
    with open(nomeArquivo, "w") as arquivo: 
        for dado in dados:
            arquivo.write(f"{dado}\n")

def lerDeArquivo(nomeArquivo):
    try:
        with open(nomeArquivo, "r") as arquivo:
            return arquivo.readlines()
    except FileNotFoundError:
        return []
    
# Testar funções criadas
cadastrarCliente("Giu", "giu@love.com", "1234567")
cadastrarCliente("Rafa", "rafinha@love.com", "7654321")
listarClientes()