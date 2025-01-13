def soma(a, b):
    return a + b 

numero1 = int(input("Digete o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

resultado = soma(numero1, numero2)

# Usar o F dentro do () para conseguir chamar variavel.
print(f"Resultado: {resultado}")