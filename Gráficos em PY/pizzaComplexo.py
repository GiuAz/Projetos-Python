import matplotlib.pyplot as plt  # Importa o módulo pyplot do Matplotlib
import numpy as np  # Importa o NumPy

numFatias = int(input("Quantas fatias do grafico quer gerar? "))

labels = []
sizes = []

for i in range(numFatias):
    label = input(f"Digite o rotulo para a fatia {i+1}: ")
    size = float(input(f"Digite o tamanho da fatia {i+1}: "))
    labels.append(label)  
    sizes.append(size)  

# Garantir que a entrada do usuário está dentro dos limites
while True:
    try:
        destacar = int(input(f"Qual fatia voce quer destacar? (1 a {numFatias}) ")) - 1
        if 0 <= destacar < numFatias:
            break
        else:
            print("Numero invalido. Tente novamente.")
    except ValueError:
        print("Entrada invalida. Digite um numero inteiro.")

explode = [0] * numFatias
explode[destacar] = 0.1  # Destacar a fatia escolhida

# Criar o gráfico de pizza
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Gráfico Personalizado')
plt.axis('equal')  # Garante que o gráfico fique circular
plt.show()
