from pathlib import Path

caminhoDoCliente = Path("clientesBiblioteca.txt")

caminhoLivro = Path("livrosClientes.txt")

while True: 

    print("\n1. Cadastrar Cliente")
    print("2. Adicionar Livros")
    print("3. Verificar Livros")
    print("4. Cancelar")

    escolha = int(input("qual sua escolha? "))

    if escolha == 1:

        # Gerando o número do cartão baseado na quantidade de linhas no arquivo de clientes
        try:
            with caminhoDoCliente.open() as arquivo:
                linhas = arquivo.readlines()
                numeroCartao = len(linhas) + 1

        except FileNotFoundError:
            numeroCartao = 1

        # Solicitando dados do cliente
        nome = input("Digite seu nome: ")
        telefone = input("Digite seu telefone: ")

        # Abrindo o arquivo no modo 'a' (append)
        with caminhoDoCliente.open(mode='a') as arquivo:
            # Escrevendo os dados no arquivo
            arquivo.write(f"{nome}, {telefone}, {numeroCartao}\n")

        print(f"Cliente cadastrado com sucesso! Seu numero de cartao: {numeroCartao}")

    elif escolha == 2: 

        # Solicitação do número do cartão 
        numeroCartao = int(input("Digite seu numero de cartao: "))
        livros = input("Digite os livros que voce quer pegar (Separados por virgula): ")

        # Abrindo o arquivo no modo 'a' (append)
        with caminhoLivro.open(mode='a') as arquivo: 
            arquivo.write(f"{numeroCartao}, {livros}\n")

        print("Livros adicionados com sucesso!")

    elif escolha == 3: 

        # Solicitação do número do cartão 
        numeroCartao = int(input("Digite seu numero de cartao: "))

        # Lendo o arquivo de livros e verificando os livros pegos pelos clientes
        try: 
            with caminhoLivro.open() as arquivo:
                linhas = arquivo.readlines()
                encontrou = False
                for linha in linhas:
                    numCartao, livros = linha.strip().split(', ', 1)
                    if int(numCartao) == numeroCartao:
                        print(f"Livros pegos: {livros}")
                        encontrou = True
                if not encontrou: 
                    print("Nenhum livro encontrado para este numero de cartao.")
        except FileNotFoundError:
            print("Nenhum registro encontrado.")

    else:
        print("Voce Saiu.")
        break # Encerra o loop