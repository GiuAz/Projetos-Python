def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro na divisao"
    return a / b

def menu():
    
    while True:
        print("Selecione a Operacao:")
        print("1. Adicao")
        print("2. Subtracao")
        print("3. Multiplicacao")
        print("4. Divisao")
        print("5. Sair")

        escolha = input("Digite a sua escolha: ")

        if escolha == '5':
            print("Saindo")
            break

        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))

        if escolha == '1':
            print(f"{num1} + {num2} = {somar(num1, num2)}")

        elif escolha == '2':
            print(f"{num1} - {num2} = {subtrair(num1, num2)}")

        elif escolha == '3':
            print(f"{num1} * {num2} = {multiplicar(num1, num2)}")

        elif escolha == '4':
            print(f"{num1} / {num2} = {dividir(num1, num2)}")

        else:
            print("Escolha invalida.")

menu()