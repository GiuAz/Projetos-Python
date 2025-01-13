print("bem vindo ao jogo")

inventario = []

#usar um loop for com um número grande de interações para simular um jogo contínuo
while True:

    print("\n1. ir para cabana")
    print("2. ir para floresta")
    print("3. sair do jogo")
    print("4. ver inventario")

    escolha = int(input("qual sua escolha? "))

    if escolha == 1:
        print("a cabana tem uma espada")
        print("1. pegar a espada")
        print("2. ignorar a espada")
        print("3. ir para floresta")
        
        espada = int(input("Oq vc faz? "))
   
        if espada == 1:
         inventario.append("espada")
         print("voce pegou a espada")

        elif espada == 2: 
         print("voce ignorou a espada")    

        elif espada == 3:
         print("voce chegou na floresta")

        else:
            print("numero invalido")            

    elif escolha == 2: 
        print("voce esta na floresta escura")

    elif escolha == 3:
        print("Voce saiu do jogo")
        break # Encerra o loop e sai do jogo

    elif escolha == 4:
       print("seu inventario")
       for item in inventario: 
          print(f"{item}")

    else: 
        print("voce saiu do jogo")
